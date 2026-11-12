"""Exporta el STL en milímetros y un JSON con parámetros y comprobación."""

from __future__ import annotations

import json
import os
import struct
from pathlib import Path

import numpy as np

from .Excepciones import ExportacionFallida, MallaNoValida, ModeloNoGenerado
from .InstantaneaExportacion import MallaEvaluada, PublicacionArchivos
from .ValidacionMalla import ValidadorMalla
from .ValidacionSolido import ValidadorSolido
from .constants.Nombres import PROP_CONFIG, UNIDADES_STL
from .util.Utilidades import Registro


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
        triangulos = caras if caras.ndim == 2 and caras.shape[1] == 3 else ValidadorSolido._Triangulos(caras)
        coords = puntos[triangulos]
        arista_a = coords[:, 1] - coords[:, 0]
        arista_b = coords[:, 2] - coords[:, 0]
        normal = np.cross(arista_a, arista_b)
        longitud = np.linalg.norm(normal, axis=1)
        normal = normal / np.maximum(longitud, 1e-12)[:, None]
        registro = np.dtype([("normal", "<f4", (3,)), ("vertices", "<f4", (3, 3)), ("atributo", "<u2")])
        datos = np.zeros(len(triangulos), dtype=registro)
        limite = np.finfo(np.float32).max
        if not np.all(np.isfinite(coords)) or np.any(np.abs(coords) > limite):
            raise ExportacionFallida(str(destino), "Coordenadas no finitas o fuera de float32.")
        datos["normal"] = normal.astype(np.float32)
        datos["vertices"] = coords.astype(np.float32)
        if not np.all(np.isfinite(datos["normal"])) or not np.all(np.isfinite(datos["vertices"])):
            raise ExportacionFallida(str(destino), "La conversión a float32 perdió finitud.")
        cabecera = b"OrtesisLab cascaron geometrico".ljust(80, b"\0")
        cuerpo = cabecera + struct.pack("<I", len(triangulos)) + datos.tobytes()
        destino.write_bytes(cuerpo)
        return len(triangulos)

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
