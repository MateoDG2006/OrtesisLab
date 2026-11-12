"""Contratos compartidos de superficie y sidecar."""

import json
import unittest

import numpy as np

from OrtesisLabPlugin import contratos


class CompatibilidadContratos(unittest.TestCase):
    def test_sidecar_valido(self):
        documento = {
            "parameters": {"pattern": "HEX"},
            "validation": {
                "open_edges": 0,
                "nonmanifold_edges": 0,
                "degenerate_faces": 0,
                "triangles": 12,
                "components": 1,
                "triangle_crossings": 0,
                "ok": True,
            },
            "stl_units": "mm",
        }
        contratos.ValidarSidecarStl(documento)

    def test_tupla_superficie(self):
        vertices = np.zeros((4, 3))
        caras = np.array([[0, 1, 2], [0, 2, 3]], dtype=np.int32)
        normales = np.zeros((4, 3))
        borde = np.zeros(4)
        contratos.ValidarTuplaSuperficie((vertices, caras, normales, borde))

    def test_version_expuesta(self):
        self.assertTrue(contratos.VERSION.startswith("OrtesisLab-contratos"))


if __name__ == "__main__":
    unittest.main()
