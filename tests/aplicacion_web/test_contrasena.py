"""Hash de contraseña: la misma clave coincide y otra no."""

from __future__ import annotations

import unittest

from web.services.ContextoUsuario import HashContrasena, NormalizarUsuario, VerificarContrasena


class Contrasena(unittest.TestCase):
    def test_la_misma_clave_coincide(self):
        huella = HashContrasena("clave-de-prueba")
        self.assertTrue(VerificarContrasena("clave-de-prueba", huella))
        self.assertFalse(VerificarContrasena("otra-clave-distinta", huella))
        self.assertFalse(VerificarContrasena("clave-de-prueba", None))

    def test_rechaza_clave_corta_y_usuario_vacio(self):
        with self.assertRaises(ValueError):
            HashContrasena("corta")
        with self.assertRaises(ValueError):
            NormalizarUsuario("  ")
        self.assertEqual(NormalizarUsuario(" Ana "), "ana")


if __name__ == "__main__":
    unittest.main()
