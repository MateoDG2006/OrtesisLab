"""Caché refinada y métricas del modelo."""

import io
import unittest

import numpy as np
from OrtesisLabPlugin.Modeling import Model3DForPrinting
from OrtesisLabPlugin.util.Utilidades import Configuracion
from web.cache.CacheRedis import CacheRedis


class CacheYMetricas(unittest.TestCase):
    def test_recargar_vuelve_a_leer_limites(self):
        datos = Configuracion.Limites()
        datos["min_cell_mm"] = -1
        Configuracion._CACHE["limites.json"] = datos
        Configuracion.Recargar()
        self.assertGreater(Configuracion.ValorLimite("min_cell_mm"), 0)

    def test_leer_tupla_devuelve_copia(self):
        original = np.array([1.0, 2.0, 3.0])
        cuerpo = io.BytesIO()
        np.savez(cuerpo, a0=original)
        payload = cuerpo.getvalue()

        class FakeRedis:
            def get(self, _clave):
                return payload

        CacheRedis.Usar(FakeRedis())
        try:
            leida = CacheRedis.LeerTupla("clave")
            self.assertIsNotNone(leida)
            leida[0][0] = 99.0
            self.assertEqual(float(original[0]), 1.0)
        finally:
            CacheRedis.Usar(None)

    def test_volumen_se_recalcula_al_cambiar_vertices(self):
        modelo = Model3DForPrinting()
        modelo.vertices = np.array(
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        )
        modelo.faces = [(0, 1, 2), (0, 3, 1), (0, 2, 3), (1, 3, 2)]
        self.assertAlmostEqual(modelo.CalculateVolume(), 1.0 / 6.0)
        modelo.vertices = np.array(
            [[0.0, 0.0, 0.0], [2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]]
        )
        self.assertAlmostEqual(modelo.CalculateVolume(), 8.0 / 6.0)


if __name__ == "__main__":
    unittest.main()
