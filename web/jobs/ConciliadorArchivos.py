"""Conciliación entre filas de ``file_assets`` y objetos del bucket.

Los plazos están en ``config/trabajador.yaml`` (``conciliador``).

- Filas ``staged`` con más de ``horas_staged``: el objeto (si llegó a subirse)
  se borra y la fila pasa a ``deleted``.
- Imports rechazados con más de ``dias_rechazo``: se borran sus objetos.
- Filas ``ready`` sin objeto: pasan a ``missing`` y su export también.
- Objetos sin fila con más de ``horas_staged``: se borran.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID

from GenerateModelsApp.util.Utilidades import Registro
from web.ConfiguracionBackend import ConfiguracionBackend
from web.enums import EstadoAsset
from web.persistence.ConexionPostgres import ConexionPostgres
from web.persistence.repositorios import RepositorioAssets, RepositorioHistorial, RepositorioImports, RepositorioUsuarios
from web.storage.AlmacenamientoPrivado import Almacen

_CONFIG = ConfiguracionBackend.Cargar("trabajador")["conciliador"]
HORAS_STAGED = _CONFIG["horas_staged"]
DIAS_RECHAZO = _CONFIG["dias_rechazo"]
LOTE_COMPROBACION = _CONFIG["lote_comprobacion"]
EXPLORAR_BUCKET = bool(_CONFIG["explorar_bucket"])


class ConciliadorArchivos:
    def __init__(self):
        self._cursor: UUID | None = None

    def Ejecutar(self) -> dict[str, int]:
        cuenta = {
            "staged": 0,
            "rechazados": 0,
            "ausentes": 0,
            "huerfanos": 0,
            "imports_colgados": 0,
            "sesiones_purgadas": 0,
            "eventos_purgados": 0,
        }
        almacen = Almacen.Actual()
        self._PurgarRetencion(cuenta)

        for asset in ConexionPostgres.Ejecutar(lambda c: RepositorioAssets.StagedVencidos(c, HORAS_STAGED)):
            if almacen.Existe(asset.storage_key):
                almacen.Borrar(asset.storage_key)
            ConexionPostgres.Ejecutar(lambda c, a=asset: RepositorioAssets.MarcarEstado(c, a.id, EstadoAsset.DELETED))
            cuenta["staged"] += 1

        for asset in ConexionPostgres.Ejecutar(lambda c: RepositorioAssets.RechazadosVencidos(c, DIAS_RECHAZO)):
            almacen.Borrar(asset.storage_key)
            ConexionPostgres.Ejecutar(lambda c, a=asset: RepositorioAssets.MarcarEstado(c, a.id, EstadoAsset.DELETED))
            cuenta["rechazados"] += 1

        # Recorre los ready por tramos para no cargar todo el catálogo en una pasada.
        listos = ConexionPostgres.Ejecutar(
            lambda c: RepositorioAssets.ListosParaComprobar(c, self._cursor, LOTE_COMPROBACION)
        )
        self._cursor = listos[-1].id if len(listos) == LOTE_COMPROBACION else None
        for asset in listos:
            if almacen.Existe(asset.storage_key):
                continue

            def marcar(conexion, a=asset) -> None:
                RepositorioAssets.MarcarEstado(conexion, a.id, EstadoAsset.MISSING)
                RepositorioAssets.MarcarExportsFaltantes(conexion, a.id)

            ConexionPostgres.Ejecutar(marcar)
            Registro.Obtener("conciliacion").warning("Objeto ausente para el asset %s.", asset.id)
            cuenta["ausentes"] += 1

        for colgado in ConexionPostgres.Ejecutar(
            lambda c: RepositorioImports.ColgadosVencidos(c, HORAS_STAGED)
        ):
            def limpiar(conexion, imp=colgado) -> None:
                RepositorioImports.MarcarRechazado(
                    conexion,
                    imp.user_id,
                    imp.id,
                    "import_timeout",
                    f"Import en {imp.status} sin cerrar tras {HORAS_STAGED} h.",
                )
                for asset_id in (imp.original_asset_id, imp.normalized_asset_id):
                    if asset_id is None:
                        continue
                    try:
                        asset = RepositorioAssets.Obtener(conexion, imp.user_id, asset_id)
                        if almacen.Existe(asset.storage_key):
                            almacen.Borrar(asset.storage_key)
                        RepositorioAssets.MarcarEstado(conexion, asset_id, EstadoAsset.DELETED)
                    except Exception:
                        RepositorioAssets.MarcarEstado(conexion, asset_id, EstadoAsset.DELETED)

            ConexionPostgres.Ejecutar(limpiar)
            cuenta["imports_colgados"] += 1

        if EXPLORAR_BUCKET:
            limite = datetime.now(timezone.utc) - timedelta(hours=HORAS_STAGED)
            pendientes: list[tuple[str, datetime]] = []
            for clave, modificado in almacen.Claves("usuarios/"):
                pendientes.append((clave, modificado))
                if len(pendientes) >= 500:
                    cuenta["huerfanos"] += self._BorrarHuerfanos(pendientes, limite)
                    pendientes = []
            cuenta["huerfanos"] += self._BorrarHuerfanos(pendientes, limite)
        return cuenta

    @staticmethod
    def _PurgarRetencion(cuenta: dict[str, int]) -> None:
        retencion = ConfiguracionBackend.Cargar("persistencia")["retencion"]

        def purgar(conexion) -> tuple[int, int]:
            sesiones = RepositorioUsuarios.PurgarSesionesVencidas(conexion, retencion["sesiones_dias"])
            eventos = RepositorioHistorial.PurgarAntiguos(conexion, retencion["eventos_historial_dias"])
            return sesiones, eventos

        sesiones, eventos = ConexionPostgres.Ejecutar(purgar)
        cuenta["sesiones_purgadas"] = sesiones
        cuenta["eventos_purgados"] = eventos

    @staticmethod
    def _BorrarHuerfanos(objetos: list[tuple[str, datetime]], limite: datetime) -> int:
        if not objetos:
            return 0
        registradas = ConexionPostgres.Ejecutar(
            lambda c: RepositorioAssets.ClavesRegistradas(c, [clave for clave, _ in objetos])
        )
        borrados = 0
        for clave, modificado in objetos:
            if clave not in registradas and modificado < limite:
                Almacen.Actual().Borrar(clave)
                borrados += 1
        return borrados
