"""Validación numérica previa a STL web."""

import unittest

import numpy as np

from GenerateModelsApp.Excepciones import CoordenadasFueraDeFloat32
from GenerateModelsApp.ValidacionSolido import ValidadorSolido
from web.GeneradorWeb import GeneradorWeb


def _cubo():
    puntos = np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
        ],
        dtype=np.float64,
    )
    caras = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [3, 0, 4, 7],
    ]
    return puntos, caras


class ExportacionValidada(unittest.TestCase):
    def test_rechaza_dos_piezas_separadas(self):
        a, caras_a = _cubo()
        b = a + np.array([3.0, 0.0, 0.0])
        puntos = np.vstack([a, b])
        caras = list(caras_a) + [[int(v) + 8 for v in cara] for cara in caras_a]
        informe = ValidadorSolido.Comprobar(puntos, caras, intersections=False)
        self.assertGreater(informe["components"], 1)
        self.assertFalse(informe["ok"])

    def test_rechaza_cara_colapsada(self):
        puntos = np.array([[0, 0, 0], [1, 0, 0], [0.5, 1e-9, 0]], dtype=np.float64)
        caras = [[0, 1, 2]]
        informe = ValidadorSolido.Comprobar(puntos, caras, intersections=False)
        self.assertGreater(informe["degenerate_faces"], 0)
        self.assertFalse(informe["ok"])

    def test_stl_rechaza_coordenadas_fuera_de_float32(self):
        puntos = np.array([[0, 0, 0], [4e38, 0, 0], [0, 1, 0]], dtype=np.float64)
        caras = [[0, 1, 2]]
        with self.assertRaises(CoordenadasFueraDeFloat32):
            GeneradorWeb.Stl(puntos, caras)


if __name__ == "__main__":
    unittest.main()
