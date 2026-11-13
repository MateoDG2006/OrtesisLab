"""Exporta el STL en milímetros y un JSON con parámetros y comprobación."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .constants.Nombres import PROP_CONFIG, UNIDADES_STL
from .Excepciones import CoordenadasFueraDeFloat32, ExportacionFallida, MallaNoValida, ModeloNoGenerado
from .InstantaneaExportacion import MallaEvaluada, PublicacionArchivos
from .StlBinario import StlBinario
from .util.Utilidades import Registro
from .ValidacionMalla import ValidadorMalla
from .ValidacionSolido import ValidadorSolido


class ExportadorStl:
    """Escribe el STL solo si la malla pasó la comprobación."""

    @staticmethod
    def _ValidarMetadatos(ob) -> dict:
        if PROP_CONFIG not in ob:
            raise ExportacionFallida(
                "",
                "El objeto no tiene la configuración ol_config. Genere el modelo de nuevo.",
            )
        try:
            parametros = json.loads(ob[PROP_CONFIG])
        except (TypeError, json.JSONDecodeError) as exc:
            raise ExportacionFallida("", f"La configuración ol_config no es JSON válido: {exc}") from exc
        if not isinstance(parametros, dict):
            raise ExportacionFallida("", "La configuración ol_config debe ser un objeto JSON.")
        return parametros

    @staticmethod
    def _EscribirStl(puntos: np.ndarray, caras: np.ndarray, destino: Path) -> int:
        try:
            cuerpo = StlBinario.Bytes(puntos, caras)
        except CoordenadasFueraDeFloat32 as exc:
            raise ExportacionFallida(str(destino), str(exc)) from exc
        destino.write_bytes(cuerpo)
        return StlBinario.Contar(cuerpo)

    @staticmethod
    def Exportar(ob, path):
        # El JSON hermano guarda los parámetros y el informe, en milímetros.
        logger = Registro.Obtener("exportacion")
        if ob is None:
            raise ModeloNoGenerado()
        destino = Path(path)
        parametros = ExportadorStl._ValidarMetadatos(ob)
        puntos, caras = MallaEvaluada.Extraer(ob)
        informe = ValidadorSolido.Comprobar(puntos, caras)
        if not informe["ok"]:
            raise MallaNoValida(json.dumps(informe))
        ValidadorMalla.GuardarInforme(ob, informe)

        stl_temp, json_temp = PublicacionArchivos.RutasTemporales(destino)
        PublicacionArchivos.Descartar(stl_temp, json_temp)
        logger.info("Exportando STL en milímetros (instantánea evaluada): %s", destino)
        try:
            ExportadorStl._EscribirStl(puntos, caras, stl_temp)
            sidecar_payload = {
                "parameters": parametros,
                "validation": informe,
                "stl_units": UNIDADES_STL,
            }
            json_temp.write_text(json.dumps(sidecar_payload, indent=2), encoding="utf-8")
        except (OSError, TypeError, json.JSONDecodeError, ExportacionFallida) as exc:
            PublicacionArchivos.Descartar(stl_temp, json_temp)
            raise ExportacionFallida(str(destino), str(exc)) from exc

        try:
            PublicacionArchivos.Confirmar(stl_temp, json_temp, destino)
        except OSError as exc:
            PublicacionArchivos.Descartar(stl_temp, json_temp)
            raise ExportacionFallida(str(destino), str(exc)) from exc
        logger.info("Parámetros publicados en %s.json", destino)
        return informe
