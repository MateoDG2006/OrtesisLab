"""Backend de arrays NumPy/CuPy del núcleo."""

import os
import unittest

import numpy as np


class ArraysBackend(unittest.TestCase):
    def test_numpy_por_defecto(self):
        os.environ.pop("ORTESISLAB_ARRAY", None)
        from OrtesisLabPlugin.util import Arrays as modulo

        # Reimporta limpio si el módulo ya se cargó con otro backend.
        import importlib

        importlib.reload(modulo)
        self.assertEqual(modulo.Arrays.nombre(), "numpy")
        puntos = np.array([[0.0, 0.0], [1.0, 1.0]])
        out = modulo.Arrays.to_numpy(modulo.Arrays.asarray(puntos))
        np.testing.assert_allclose(out, puntos)

    def test_distancia_cuadricula_coincide(self):
        from OrtesisLabPlugin.constants.Paterns import Patron

        uv = np.array([[0.0, 0.0], [5.0, 0.0], [2.5, 2.5]])
        d = Patron.DistanciaCuadricula(uv, 10.0)
        self.assertEqual(len(d), 3)
        self.assertTrue(np.all(np.isfinite(d)))
