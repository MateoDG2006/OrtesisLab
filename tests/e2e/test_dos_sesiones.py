"""Aislamiento de claves por usuario en el bucket."""

import unittest
from uuid import uuid4

from web.storage.AlmacenamientoPrivado import Almacen


@unittest.skip("Requiere base y bucket reales")
class DosSesiones(unittest.TestCase):
    def test_claves_distintas_por_usuario(self):
        usuario_a, usuario_b = uuid4(), uuid4()
        asset = uuid4()
        clave_a = Almacen.Clave(usuario_a, asset, stl_publico=True)
        clave_b = Almacen.Clave(usuario_b, asset, stl_publico=True)
        self.assertNotEqual(clave_a, clave_b)


if __name__ == "__main__":
    unittest.main()
