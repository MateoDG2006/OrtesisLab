"""Presupuestos de carga NPZ y validación de límites (A-01, A-03, A-11)."""

from __future__ import annotations

import io
import struct
import unittest
import zipfile

import numpy as np

from OrtesisLabPlugin.Excepciones import ArchivoSuperficieIlegible, ConfiguracionInvalida
from OrtesisLabPlugin.InspeccionNpz import InspeccionNpz
from OrtesisLabPlugin.util.Utilidades import Configuracion
from web.LectorSuperficie import LectorSuperficie


def _Npy(arreglo: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    np.save(buffer, arreglo, allow_pickle=False)
    return buffer.getvalue()


def _NpzMentiroso(shape_vertices: tuple[int, ...]) -> bytes:
    """NPZ pequeño cuya cabecera de vertices declara una forma enorme."""
    vertices = np.zeros((2, 3), dtype=np.float64)
    faces = np.array([[0, 1, 0]], dtype=np.int32)
    normals = np.zeros((2, 3), dtype=np.float64)
    verdadero = _Npy(vertices)
    # Reescribe la cabecera con un shape mentiroso y payload corto.
    magia = verdadero[:8]
    meta = f"{{'descr': '<f8', 'fortran_order': False, 'shape': {shape_vertices}, }}"
    meta_b = meta.encode("latin1")
    meta_b = meta_b + b" " * (64 - (len(meta_b) % 64))
    mentiroso = magia + struct.pack("<H", len(meta_b)) + meta_b + b"\0" * 16
    salida = io.BytesIO()
    with zipfile.ZipFile(salida, "w") as archivo:
        archivo.writestr("vertices.npy", mentiroso)
        archivo.writestr("faces.npy", _Npy(faces))
        archivo.writestr("normals.npy", _Npy(normals))
    return salida.getvalue()


class CargaYPresupuesto(unittest.TestCase):
    def test_rechaza_cabecera_npy_con_shape_incoherente(self):
        contenido = _NpzMentiroso((10**9, 3))
        with self.assertRaises(ArchivoSuperficieIlegible):
            InspeccionNpz.VerificarContenido(contenido, "mentira.npz", 134217728)

    def test_presupuesto_de_vertices(self):
        vertices = np.zeros((10, 3))
        caras = np.zeros((5, 3), dtype=np.int32)
        with self.assertRaises(ArchivoSuperficieIlegible):
            # Tope efectivo vía monkeypatch del límite.
            original = Configuracion.ValorLimite

            def falso(clave: str) -> float:
                if clave == "max_surface_vertices":
                    return 3.0
                if clave == "max_surface_faces":
                    return 1000.0
                return original(clave)

            Configuracion.ValorLimite = staticmethod(falso)  # type: ignore[assignment]
            try:
                InspeccionNpz.VerificarPresupuesto(vertices, caras, "test.npz")
            finally:
                Configuracion.ValorLimite = staticmethod(original)  # type: ignore[assignment]

    def test_limites_rechazan_pattern_batch_cero(self):
        Configuracion.Recargar()
        datos = Configuracion.Limites()
        datos["pattern_batch"] = 0
        with self.assertRaises(ConfiguracionInvalida):
            Configuracion._ValidarLimites(datos)

    def test_limites_rechazan_minimo_mayor_que_maximo(self):
        datos = Configuracion.Limites()
        datos["min_plausible_surface_extent_mm"] = 2000
        datos["max_plausible_surface_extent_mm"] = 100
        with self.assertRaises(ConfiguracionInvalida):
            Configuracion._ValidarLimites(datos)

    def test_npz_valido_pasa_inspeccion(self):
        vertices = np.array([[0.0, 0.0, 0.0], [10.0, 0.0, 0.0], [0.0, 10.0, 0.0]], dtype=np.float64)
        faces = np.array([[0, 1, 2]], dtype=np.int32)
        normals = np.array([[0.0, 0.0, 1.0]] * 3, dtype=np.float64)
        buffer = io.BytesIO()
        np.savez(buffer, vertices=vertices, faces=faces, normals=normals)
        InspeccionNpz.VerificarContenido(buffer.getvalue(), "ok.npz", 134217728)
        leidos, _info = LectorSuperficie.Preparar("ok.npz", buffer.getvalue())
        self.assertEqual(len(leidos[0]), 3)


if __name__ == "__main__":
    unittest.main()
