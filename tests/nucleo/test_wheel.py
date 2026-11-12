"""Comprueba el punto de entrada declarado en pyproject."""

import unittest
from pathlib import Path
import tomllib


class EntradaConsola(unittest.TestCase):
    def test_pyproject_declara_ortesislab(self):
        raiz = Path(__file__).resolve().parents[2]
        datos = tomllib.loads((raiz / "pyproject.toml").read_text(encoding="utf-8"))
        scripts = datos["project"]["scripts"]
        self.assertIn("ortesislab", scripts)
        self.assertEqual(scripts["ortesislab"], "GenerateModelsApp.consola:main")

    def test_main_imprimible(self):
        from GenerateModelsApp.consola import main

        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
