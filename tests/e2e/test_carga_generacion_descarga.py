"""Contrato de lectura anónima solo para STL."""

import re
import unittest

from web.storage.AlmacenamientoPrivado import Almacen

POLITICA = re.compile(
    r"^usuarios/[0-9a-f-]{36}/assets/[0-9a-f-]{36}(\.stl)?$"
)


class PoliticaAlmacenamiento(unittest.TestCase):
    def test_stl_publico_permite_clave_anonima(self):
        from uuid import uuid4

        clave = Almacen.Clave(uuid4(), uuid4(), stl_publico=True)
        self.assertTrue(clave.endswith(".stl"))
        self.assertTrue(POLITICA.match(clave))

    def test_npz_no_lleva_sufijo_stl(self):
        from uuid import uuid4

        clave = Almacen.Clave(uuid4(), uuid4(), stl_publico=False)
        self.assertFalse(clave.endswith(".stl"))


if __name__ == "__main__":
    unittest.main()
