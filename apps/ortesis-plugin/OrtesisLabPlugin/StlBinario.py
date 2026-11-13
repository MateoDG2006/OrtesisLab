"""STL binario del cascarón, en milímetros, sin Blender.

La web, el lector de superficies y el exportador del complemento escriben y
leen este mismo registro. El visor del navegador recorre el archivo por su
cuenta porque corre en otro proceso.
"""

from __future__ import annotations

import struct

import numpy as np

from .Excepciones import CoordenadasFueraDeFloat32

CABECERA = b"OrtesisLab cascaron geometrico".ljust(80, b"\0")
REGISTRO = np.dtype([("normal", "<f4", (3,)), ("vertices", "<f4", (3, 3)), ("atributo", "<u2")])
BYTES_CARA = int(REGISTRO.itemsize)


class StlBinario:
    @staticmethod
    def Triangulos(caras) -> np.ndarray:
        salida = []
        for cara in caras:
            indices = [int(vertice) for vertice in cara]
            if len(indices) < 3:
                continue
            for posicion in range(1, len(indices) - 1):
                salida.append((indices[0], indices[posicion], indices[posicion + 1]))
        return np.asarray(salida, dtype=np.int64)

    @staticmethod
    def Bytes(vertices, caras) -> bytes:
        puntos = np.asarray(vertices, dtype=np.float64)
        triangulos = StlBinario.Triangulos(caras)
        coords = puntos[triangulos]
        arista_a = coords[:, 1] - coords[:, 0]
        arista_b = coords[:, 2] - coords[:, 0]
        normal = np.cross(arista_a, arista_b)
        longitud = np.linalg.norm(normal, axis=1)
        normal = normal / np.maximum(longitud, 1e-12)[:, None]
        limite = np.finfo(np.float32).max
        if not np.all(np.isfinite(coords)) or np.any(np.abs(coords) > limite):
            raise CoordenadasFueraDeFloat32()
        datos = np.zeros(len(triangulos), dtype=REGISTRO)
        datos["normal"] = normal.astype(np.float32)
        datos["vertices"] = coords.astype(np.float32)
        if not np.all(np.isfinite(datos["normal"])) or not np.all(np.isfinite(datos["vertices"])):
            raise CoordenadasFueraDeFloat32()
        return CABECERA + struct.pack("<I", len(triangulos)) + datos.tobytes()

    @staticmethod
    def Contar(contenido: bytes) -> int:
        return struct.unpack_from("<I", contenido, 80)[0]

    @staticmethod
    def VerticesSiBinario(contenido: bytes) -> np.ndarray | None:
        if len(contenido) < 84:
            return None
        cantidad = struct.unpack_from("<I", contenido, 80)[0]
        if 84 + cantidad * BYTES_CARA != len(contenido):
            return None
        datos = np.frombuffer(contenido, dtype=REGISTRO, count=cantidad, offset=84)
        return np.array(datos["vertices"], dtype=np.float64, copy=True)
