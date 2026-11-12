"""Valores ajustables del backend, leídos de ``config/<area>.yaml`` en la raíz.

Los secretos y las URL van en el entorno (``Ajustes``); aquí solo hay límites,
tiempos y tamaños. Un archivo o una clave ausente es un error de despliegue.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

CARPETA = Path(__file__).resolve().parent.parent / "config"
AREAS = ("trabajador", "persistencia", "web", "cache", "almacen", "sesion")


class ConfiguracionInvalida(Exception):
    """YAML ausente, tipo incorrecto o relaciones incoherentes entre áreas."""


class ConfiguracionBackend:
    @staticmethod
    @lru_cache(maxsize=None)
    def Cargar(area: str) -> dict:
        ruta = CARPETA / f"{area}.yaml"
        if not ruta.is_file():
            raise ConfiguracionInvalida(f"No existe config/{area}.yaml.")
        with ruta.open(encoding="utf-8") as archivo:
            datos = yaml.safe_load(archivo)
        if not isinstance(datos, dict):
            raise ConfiguracionInvalida(f"config/{area}.yaml debe ser un objeto YAML.")
        ConfiguracionBackend._ValidarArea(area, datos)
        return datos

    @staticmethod
    def ValidarEnArranque() -> None:
        """Carga todas las áreas y comprueba relaciones entre ellas."""
        for area in AREAS:
            ConfiguracionBackend.Cargar(area)
        lotes = ConfiguracionBackend.Cargar("persistencia")["lotes"]["maximo_items"]
        variantes = ConfiguracionBackend.Cargar("web")["maximo_variantes"]
        if variantes > lotes:
            raise ConfiguracionInvalida(
                f"web.maximo_variantes ({variantes}) no puede superar persistencia.lotes.maximo_items ({lotes})."
            )
        lease = ConfiguracionBackend.Cargar("trabajador")["lease_s"]
        latido = ConfiguracionBackend.Cargar("trabajador")["latido_s"]
        if latido >= lease:
            raise ConfiguracionInvalida(f"trabajador.latido_s ({latido}) debe ser menor que lease_s ({lease}).")

    @staticmethod
    def _ValidarArea(area: str, datos: dict) -> None:
        esquemas: dict[str, dict[str, type | tuple[type, ...]]] = {
            "trabajador": {
                "lease_s": int,
                "latido_s": int,
                "supervision_s": (int, float),
                "conciliacion_s": (int, float),
                "max_concurrent_geometry": int,
                "capacidad_variante_s": (int, float),
                "max_items_por_usuario": int,
                "conciliador": dict,
            },
            "persistencia": {
                "conexion": dict,
                "lotes": dict,
                "historial": dict,
                "cuotas": dict,
                "retencion": dict,
            },
            "web": {
                "intervalo_progreso_s": (int, float),
                "maximo_variantes": int,
                "espera_crear_s": (int, float),
                "maximo_bytes": int,
                "maximo_descomprimido_bytes": int,
                "max_normalizaciones_concurrentes": int,
                "patrones": dict,
                "ejes": dict,
                "estados_visibles": dict,
            },
            "cache": {
                "ttl_s": int,
                "reintento_s": (int, float),
                "timeout_s": (int, float),
                "max_entrada_bytes": int,
            },
            "almacen": {
                "timeout_conexion_s": (int, float),
                "timeout_lectura_s": (int, float),
                "intentos": int,
            },
            "sesion": {
                "duracion_horas": (int, float),
                "intercambio_oidc_s": int,
            },
        }
        if area not in esquemas:
            return
        requeridas = esquemas[area]
        for clave, tipos in requeridas.items():
            if clave not in datos:
                raise ConfiguracionInvalida(f"config/{area}.yaml: falta la clave «{clave}».")
            if not isinstance(datos[clave], tipos):
                esperado = tipos if isinstance(tipos, tuple) else (tipos,)
                nombres = ", ".join(t.__name__ for t in esperado)
                raise ConfiguracionInvalida(
                    f"config/{area}.yaml: «{clave}» debe ser {nombres}, no {type(datos[clave]).__name__}."
                )
        if area == "trabajador":
            conc = datos["conciliador"]
            for clave in ("horas_staged", "dias_rechazo", "lote_comprobacion", "explorar_bucket"):
                if clave not in conc:
                    raise ConfiguracionInvalida(f"config/trabajador.yaml conciliador: falta «{clave}».")
            if not isinstance(conc["explorar_bucket"], bool):
                raise ConfiguracionInvalida("config/trabajador.yaml conciliador.explorar_bucket debe ser bool.")
        if area == "persistencia":
            lotes = datos["lotes"]
            for clave in ("maximo_items", "maximo_pendientes", "maximo_intentos", "espera_reintento_s"):
                if clave not in lotes:
                    raise ConfiguracionInvalida(f"config/persistencia.yaml lotes: falta «{clave}».")
            cuotas = datos["cuotas"]
            for clave in ("max_bytes_usuario", "max_imports_ready", "max_subidas_por_hora"):
                if clave not in cuotas or not isinstance(cuotas[clave], int):
                    raise ConfiguracionInvalida(f"config/persistencia.yaml cuotas: «{clave}» debe ser entero.")
            ret = datos["retencion"]
            for clave in ("sesiones_dias", "eventos_historial_dias"):
                if clave not in ret or not isinstance(ret[clave], int):
                    raise ConfiguracionInvalida(f"config/persistencia.yaml retencion: «{clave}» debe ser entero.")

    @staticmethod
    def _EnteroPositivo(valor: Any, ruta: str) -> int:
        if not isinstance(valor, int) or valor <= 0:
            raise ConfiguracionInvalida(f"{ruta} debe ser un entero positivo.")
        return valor
