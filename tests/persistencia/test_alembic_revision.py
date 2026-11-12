"""Humo de la revisión inicial de Alembic (sin exigir base en vivo)."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


class RevisionAlembic(unittest.TestCase):
    def test_upgrade_y_downgrade_existen(self):
        ruta = (
            Path(__file__).resolve().parents[2]
            / "db"
            / "alembic"
            / "versions"
            / "20261112_1200_esquema_inicial.py"
        )
        self.assertTrue(ruta.is_file(), f"Falta la revisión: {ruta}")
        nombre = "ortesislab_esquema_inicial_revision"
        spec = importlib.util.spec_from_file_location(nombre, ruta)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertEqual(modulo.down_revision, None)
        self.assertTrue(callable(modulo.upgrade))
        self.assertTrue(callable(modulo.downgrade))


if __name__ == "__main__":
    unittest.main()
