"""Caché refinada y métricas del modelo."""

import io
import unittest
import numpy as np

from OrtesisLabPlugin.Modeling import Model3DForPrinting
from OrtesisLabPlugin.util.Utilidades import Configuracion
from web.cache.CacheRedis import CacheRedis


class CacheYMetricas(unittest.TestCase):
    def test_recargar_limpia_cache_json(self):
        Configuracion._CACHE["limites.json"] = {"marcador": 1}
        Configuracion.Recargar()
        self.assertEqual(len(Configuracion._CACHE), 0)

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

    def test_volumen_se_invalida_al_cambiar_vertices(self):
        modelo = Model3DForPrinting()
        modelo._volumen_mm3 = 5.0
        modelo.vertices = np.zeros((3, 3))
        self.assertIsNone(modelo._volumen_mm3)


if __name__ == "__main__":
    unittest.main()
