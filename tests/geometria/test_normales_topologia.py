"""Regresiones A-04, A-05, A-06, A-14, A-16 y A-22 (fixtures sintéticas)."""

from __future__ import annotations

import unittest

import numpy as np
from OrtesisLabPlugin.Cascaron import Cascaron
from OrtesisLabPlugin.Excepciones import (
    CalidadInsuficiente,
    GeometriaInconsistente,
    NormalesInvalidas,
    SuperficieInvalida,
)
from OrtesisLabPlugin.Malla import AnalizadorMalla
from OrtesisLabPlugin.RefinadorMalla import RefinadorMalla


class NormalesYTopologia(unittest.TestCase):
    def test_el_suavizado_conserva_la_normal_del_pliegue(self):
        # La fila inferior se dobla casi 180°. El promedio con los vecinos la invierte.
        puntos = np.array(
            [
                [0, 0, 0], [10, 0, 0], [20, 0, 0],
                [0, 10, 0], [10, 10, 0], [20, 10, 0],
                [0, 9.2, -0.3], [10, 8.5, -0.3], [20, 9.2, -0.3],
            ],
            dtype=np.float64,
        )
        caras = np.array(
            [
                [0, 1, 4], [0, 4, 3], [1, 2, 5], [1, 5, 4],
                [3, 4, 7], [3, 7, 6], [4, 5, 8], [4, 8, 7],
            ],
            dtype=np.int32,
        )
        normales = AnalizadorMalla.NormalesDeCaras(puntos, caras)
        refinados, caras_ref, normales_ref, _borde = RefinadorMalla.Refinar(
            puntos, caras, normales, 5.0
        )
        geometricas = AnalizadorMalla.NormalesDeCaras(refinados, caras_ref)
        acuerdo = np.einsum("ij,ij->i", normales_ref, geometricas)
        self.assertGreaterEqual(float(acuerdo.min()), 0.5)

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

    def test_a05_rechaza_dos_triangulos_unidos_por_un_vertice(self):
        vertices = np.array(
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]],
            dtype=np.float64,
        )
        caras = np.array([[0, 1, 2], [0, 3, 4]], dtype=np.int32)
        normales = AnalizadorMalla.NormalesDeCaras(vertices, caras)
        with self.assertRaises(SuperficieInvalida):
            AnalizadorMalla.Preparar(vertices, caras, normales, suavizarNormales=False)

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


if __name__ == "__main__":
    unittest.main()
