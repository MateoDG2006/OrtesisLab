"""Humo: la web y el trabajador deben importar sin ImportError."""

from __future__ import annotations

import unittest


class HumoImport(unittest.TestCase):
    def test_importa_aplicacion_web(self):
        import web.GenerateModelsApp  # noqa: F401

    def test_importa_trabajador(self):
        import web.jobs.TrabajadorGeneracion  # noqa: F401


if __name__ == "__main__":
    unittest.main()
