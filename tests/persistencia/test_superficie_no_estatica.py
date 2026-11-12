"""A-02: el import no escribe en uploaded_files/ servido por Reflex."""

from __future__ import annotations

import io
import unittest
from pathlib import Path

import numpy as np

from tests.persistencia.apoyo_persistencia import (
    Conectar,
    CrearUsuario,
    EntornoServicios,
    requiere_base,
)


@requiere_base
class SuperficieNoEstatica(unittest.TestCase):
    def test_import_usa_bucket_y_no_uploaded_files(self):
        raiz = Path(__file__).resolve().parents[2]
        estaticos = raiz / "uploaded_files"
        antes = set(estaticos.rglob("*")) if estaticos.exists() else set()

        vertices = np.array([[0, 0, 0], [30, 0, 0], [0, 30, 0]], dtype=np.float64)
        faces = np.array([[0, 1, 2]], dtype=np.int32)
        normals = np.array([[0, 0, 1]] * 3, dtype=np.float64)
        buffer = io.BytesIO()
        np.savez(buffer, vertices=vertices, faces=faces, normals=normals)
        contenido = buffer.getvalue()

        with EntornoServicios():
            with Conectar() as conexion:
                usuario = CrearUsuario(conexion, "NoEstatica")
            from web.persistence.ConexionPostgres import ConexionPostgres
            from web.persistence.repositorios import RepositorioAssets
            from web.services.ContextoUsuario import ContextoUsuario
            from web.services.ServicioImports import ServicioImports

            with ContextoUsuario.Activar(usuario):
                importacion, _info = ServicioImports.Importar(
                    usuario, "placa.npz", contenido, autoescalar=False
                )
            asset = ConexionPostgres.Ejecutar(
                lambda c: RepositorioAssets.Obtener(
                    c, usuario.user_id, importacion.normalized_asset_id
                )
            )
            self.assertTrue(asset.storage_key.startswith("usuarios/"))
            self.assertNotIn("uploaded_files", asset.storage_key)

        despues = set(estaticos.rglob("*")) if estaticos.exists() else set()
        self.assertEqual(antes, despues)


if __name__ == "__main__":
    unittest.main()
