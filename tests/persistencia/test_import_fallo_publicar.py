"""Import rechazado si falla la publicación al bucket (B-06)."""

from __future__ import annotations

import unittest
import uuid
from unittest.mock import MagicMock, patch

from web.persistence.Contratos import UsuarioAutenticado
from web.services.ServicioImports import ServicioImports
from web.storage.AlmacenamientoPrivado import AlmacenamientoNoDisponible


class PublicarFalla(unittest.TestCase):
    def setUp(self):
        self.usuario = UsuarioAutenticado(uuid.uuid4(), "Prueba", None, uuid.uuid4())
        self.contenido = (
            b"\x00" * 80
            + (4).to_bytes(4, "little")
            + b"\x00" * 50
        )

    def test_publicar_falla_marca_rechazado(self):
        import_id = uuid.uuid4()
        rechazos: list[tuple[str, str]] = []

        def ejecutar(funcion):
            conexion = MagicMock()
            nombre = getattr(funcion, "__name__", "")
            if nombre == "rechazar_fallo" or "rechazar" in str(funcion):
                return None
            with (
                patch("web.services.ServicioImports.RepositorioLotes.BloquearUsuario"),
                patch("web.services.ServicioImports.RepositorioImports.ListoPorOriginal", return_value=None),
                patch("web.services.ServicioImports.RepositorioImports.ContarReady", return_value=0),
                patch("web.services.ServicioImports.RepositorioImports.ContarSubidasRecientes", return_value=0),
                patch("web.services.ServicioImports.RepositorioAssets.BytesUsuarioReady", return_value=0),
                patch("web.services.ServicioImports.RepositorioAssets.CrearStaged"),
                patch("web.services.ServicioImports.RepositorioImports.Crear"),
                patch("web.services.ServicioImports.RepositorioHistorial.Evento"),
            ):
                if "admitir" in str(funcion):
                    return import_id, uuid.uuid4()
            with patch(
                "web.services.ServicioImports.RepositorioImports.MarcarRechazado",
                side_effect=lambda _c, _u, _i, codigo, mensaje: rechazos.append((codigo, mensaje)),
            ):
                with patch("web.services.ServicioImports.RepositorioHistorial.Evento"):
                    return funcion(conexion)

        almacen = MagicMock()
        almacen.Publicar.side_effect = AlmacenamientoNoDisponible("caída simulada")

        with (
            patch("web.services.ServicioImports.ConexionPostgres.Ejecutar", side_effect=ejecutar),
            patch("web.services.ServicioImports.Almacen.Actual", return_value=almacen),
        ):
            with self.assertRaises(AlmacenamientoNoDisponible):
                ServicioImports._Registrar(
                    self.usuario,
                    "pieza.stl",
                    self.contenido,
                    "upload",
                    "stl_binary",
                    "model/stl",
                    lambda _b: (([[0, 0, 0]], [[0, 1, 2]], [[0, 0, 1]], [0.0])),
                )
        self.assertTrue(rechazos)


if __name__ == "__main__":
    unittest.main()
