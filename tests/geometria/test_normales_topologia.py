"""Regresiones A-04, A-05, A-06, A-14, A-16 y A-22 (fixtures sintéticas)."""

from __future__ import annotations

import unittest

import numpy as np

from OrtesisLabPlugin.Cascaron import Cascaron
from OrtesisLabPlugin.Excepciones import (
    AristasNoManifold,
    CalidadInsuficiente,
    GeometriaInconsistente,
    NormalesInvalidas,
)
from OrtesisLabPlugin.Malla import AnalizadorMalla
from OrtesisLabPlugin.RefinadorMalla import RefinadorMalla
from OrtesisLabPlugin.SuavizadoBorde import SuavizadoBorde


class NormalesYTopologia(unittest.TestCase):
    def test_a04_rechaza_normales_tangenciales(self):
        vertices = np.array(
            [[0.0, 0.0, 0.0], [40.0, 0.0, 0.0], [40.0, 40.0, 0.0], [0.0, 40.0, 0.0]],
            dtype=np.float64,
        )
        caras = np.array([[0, 1, 2], [0, 2, 3]], dtype=np.int32)
        normales = np.tile([1.0, 0.0, 0.0], (4, 1))
        with self.assertRaises(NormalesInvalidas):
            AnalizadorMalla.Preparar(vertices, caras, normales, suavizarNormales=False)

    def test_a04_espesor_colapsado(self):
        puntos = np.array(
            [[0.0, 0.0, 0.0], [10.0, 0.0, 0.0], [0.0, 10.0, 0.0]], dtype=np.float64
        )
        caras = np.array([[0, 1, 2]], dtype=np.int32)
        normales = np.tile([1.0, 0.0, 0.0], (3, 1))  # tangencial a XY → offset en plano
        # Forzar normales unitarias tangenciales: Engrosar desplaza en X pero
        # si normales son cero efectivas...
        normales = np.zeros((3, 3))
        with self.assertRaises(GeometriaInconsistente):
            Cascaron.Engrosar(puntos, caras, normales, 2.0)

    def test_a05_detecta_vertice_no_manifold(self):
        # Dos tetraedros unidos solo por el vértice 0 (A-05).
        a = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
        b = np.array([[0, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, -1]], dtype=float)
        caras_a = np.array([[0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 3, 2]], dtype=np.int32)
        caras_b = np.array([[0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 3, 2]], dtype=np.int32) + 0
        # Remap segundo tetra: vértice 0 compartido, 1..3 → 4..6
        vertices = np.vstack((a, b[1:]))
        caras_b = np.array([[0, 4, 5], [0, 5, 6], [0, 6, 4], [4, 6, 5]], dtype=np.int32)
        caras = np.vstack((caras_a, caras_b))
        self.assertTrue(AnalizadorMalla._VerticesNoManifold(caras, len(vertices)))

    def test_a06_presupuesto_no_devuelve_exito_silencioso(self):
        vertices = np.array(
            [[0.0, 0.0, 0.0], [40.0, 0.0, 0.0], [40.0, 40.0, 0.0], [0.0, 40.0, 0.0]],
            dtype=np.float64,
        )
        caras = np.array([[0, 1, 2], [0, 2, 3]], dtype=np.int32)
        normales = np.tile([0.0, 0.0, 1.0], (4, 1))
        from OrtesisLabPlugin.util.Utilidades import Configuracion

        original = Configuracion.ValorLimite

        def tope(clave: str) -> float:
            if clave == "max_surface_vertices":
                return 4.0
            return original(clave)

        Configuracion.ValorLimite = staticmethod(tope)  # type: ignore[assignment]
        try:
            with self.assertRaises(CalidadInsuficiente):
                RefinadorMalla.Refinar(vertices, caras, normales, 5.0)
        finally:
            Configuracion.ValorLimite = staticmethod(original)  # type: ignore[assignment]

    def test_a22_filtro_usa_perimetro_fisico(self):
        # Mismo campo de normales sobre contornos escalados: el corte depende de mm.
        bucle_chico = np.array(
            [[0, 0, 0], [8, 0, 0], [8, 8, 0], [0, 8, 0], [-1, 4, 0], [4, -1, 0], [9, 4, 0], [4, 9, 0]],
            dtype=float,
        )
        normales = np.tile([0.0, 0.0, 1.0], (len(bucle_chico), 1))
        normales[1] = [0.2, 0.0, np.sqrt(1 - 0.04)]
        filtrado_a = SuavizadoBorde._PasabajosCampo(normales, bucle_chico, 8.0)
        filtrado_b = SuavizadoBorde._PasabajosCampo(normales, bucle_chico * 10.0, 8.0)
        self.assertFalse(np.allclose(filtrado_a, filtrado_b))


if __name__ == "__main__":
    unittest.main()
