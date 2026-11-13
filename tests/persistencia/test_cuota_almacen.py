"""Cuotas de almacenamiento en importación (B-05)."""

from __future__ import annotations

import unittest
import uuid
from unittest.mock import MagicMock, patch

from web.persistence.Contratos import CuotaExcedida, UsuarioAutenticado
from web.services.ServicioImports import ServicioImports


class CuotaAlmacen(unittest.TestCase):
    def setUp(self):
        self.usuario = UsuarioAutenticado(uuid.uuid4(), "Prueba", None, uuid.uuid4())
        self.contenido = b"solid test\nendsolid\n"

    def test_rechaza_cuota_de_bytes(self):
        def ejecutar(funcion):
            conexion = MagicMock()
            with (
                patch("web.services.ServicioImports.RepositorioLotes.BloquearUsuario"),
                patch("web.services.ServicioImports.RepositorioImports.ListoPorOriginal", return_value=None),
                patch("web.services.ServicioImports.RepositorioImports.ContarReady", return_value=0),
                patch("web.services.ServicioImports.RepositorioImports.ContarSubidasRecientes", return_value=0),
                patch(
                    "web.services.ServicioImports.RepositorioAssets.BytesUsuarioReady",
                    return_value=10**15,
                ),
            ):
                return funcion(conexion)

        with patch("web.services.ServicioImports.ConexionPostgres.Ejecutar", side_effect=ejecutar):
            with self.assertRaises(CuotaExcedida):
                ServicioImports.Importar(self.usuario, "pieza.stl", self.contenido)


if __name__ == "__main__":
    unittest.main()
