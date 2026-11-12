"""Instantánea evaluada de mallas Blender y publicación atómica de archivos."""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np


class MallaEvaluada:
    """Instantánea de la malla con modificadores y transformación aplicados."""

    @staticmethod
    def Extraer(ob) -> tuple[np.ndarray, np.ndarray]:
        """Entrada: objeto Blender. Salida: vértices world-space y caras triangulares."""
        from .ApiBlender import bpy

        depsgraph = bpy.context.evaluated_depsgraph_get()
        evaluado = ob.evaluated_get(depsgraph)
        malla = None
        try:
            malla = bpy.data.meshes.new_from_object(evaluado, depsgraph=depsgraph)
            malla.calc_loop_triangles()
            coordenadas = np.empty(len(malla.vertices) * 3, dtype=np.float64)
            malla.vertices.foreach_get("co", coordenadas)
            puntos = coordenadas.reshape(-1, 3)
            matriz = np.array(evaluado.matrix_world, dtype=np.float64)
            if matriz.shape == (4, 4):
                homogeneos = np.concatenate([puntos, np.ones((len(puntos), 1), dtype=np.float64)], axis=1)
                puntos = (homogeneos @ matriz.T)[:, :3]
            caras = np.array(
                [tri.vertices[:] for tri in malla.loop_triangles],
                dtype=np.int32,
            )
            return puntos, caras
        finally:
            if malla is not None:
                bpy.data.meshes.remove(malla)


class PublicacionArchivos:
    """Publicación atómica del par STL + JSON desde archivos temporales."""

    @staticmethod
    def RutasTemporales(destino: Path) -> tuple[Path, Path]:
        destino = Path(destino)
        return destino.with_suffix(destino.suffix + ".part"), Path(str(destino) + ".json.part")

    @staticmethod
    def Confirmar(stl_temp: Path, json_temp: Path, destino: Path) -> None:
        sidecar = Path(str(destino) + ".json")
        os.replace(stl_temp, destino)
        os.replace(json_temp, sidecar)

    @staticmethod
    def Descartar(stl_temp: Path, json_temp: Path) -> None:
        for ruta in (stl_temp, json_temp):
            if ruta.is_file():
                ruta.unlink(missing_ok=True)
