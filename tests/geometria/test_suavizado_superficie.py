"""Regresiones del suavizado Taubin de ruido en el interior."""

from __future__ import annotations

import unittest

import numpy as np

from OrtesisLabPlugin.SuavizadoSuperficie import SuavizadoSuperficie
from OrtesisLabPlugin.util.Utilidades import Configuracion


class SuavizadoDeInterior(unittest.TestCase):
    def _PlanoConRuido(self, columnas=41, filas=41, amplitud=0.35):
        eje_x = np.linspace(0.0, 40.0, columnas)
        eje_y = np.linspace(0.0, 40.0, filas)
        grilla_x, grilla_y = np.meshgrid(eje_x, eje_y, indexing="xy")
        ruido = amplitud * ((np.arange(columnas * filas) % 3) - 1).reshape(filas, columnas)
        ruido = ruido.astype(np.float64)
        # Alternar signos en damero de alta frecuencia.
        damero = ((np.arange(filas)[:, None] + np.arange(columnas)[None, :]) % 2) * 2 - 1
        z = ruido * damero
        puntos = np.column_stack(
            (grilla_x.ravel(), grilla_y.ravel(), z.ravel())
        )
        caras = []
        for fila in range(filas - 1):
            for columna in range(columnas - 1):
                inicio = fila * columnas + columna
                caras.append((inicio, inicio + 1, inicio + columnas))
                caras.append((inicio + 1, inicio + 1 + columnas, inicio + columnas))
        caras = np.asarray(caras, dtype=np.int32)
        normales = np.tile([0.0, 0.0, 1.0], (len(puntos), 1))
        return puntos, caras, normales, columnas, filas

    def _MascaraInterior(self, columnas, filas):
        mascara = np.zeros(columnas * filas, dtype=bool)
        for fila in range(1, filas - 1):
            mascara[fila * columnas + 1 : (fila + 1) * columnas - 1] = True
        return mascara

    def test_reduce_ruido_de_alta_frecuencia(self):
        puntos, caras, normales, columnas, filas = self._PlanoConRuido()
        interior = self._MascaraInterior(columnas, filas)
        residual_antes = float(np.std(puntos[interior, 2]))
        suaves, _, desplazamiento = SuavizadoSuperficie.Aplicar(puntos, caras, normales)
        residual_despues = float(np.std(suaves[interior, 2]))
        self.assertLess(residual_despues, 0.45 * residual_antes)
        self.assertGreater(desplazamiento, 0.0)
        self.assertLess(desplazamiento, 0.41)

    def test_el_contorno_no_se_mueve(self):
        puntos, caras, normales, columnas, filas = self._PlanoConRuido()
        interior = self._MascaraInterior(columnas, filas)
        suaves, _, _ = SuavizadoSuperficie.Aplicar(puntos, caras, normales)
        borde = ~interior
        np.testing.assert_allclose(suaves[borde], puntos[borde], atol=1e-12)

    def test_iterations_cero_no_cambia(self):
        puntos, caras, normales, _c, _f = self._PlanoConRuido()
        original = Configuracion.ValorLimite

        def tope(clave: str) -> float:
            if clave == "surface_smooth_iterations":
                return 0.0
            return original(clave)

        Configuracion.ValorLimite = staticmethod(tope)  # type: ignore[assignment]
        try:
            suaves, normales_suaves, desplazamiento = SuavizadoSuperficie.Aplicar(
                puntos, caras, normales
            )
        finally:
            Configuracion.ValorLimite = staticmethod(original)  # type: ignore[assignment]
        np.testing.assert_array_equal(suaves, puntos)
        np.testing.assert_array_equal(normales_suaves, normales)
        self.assertEqual(desplazamiento, 0.0)

    def test_conserva_la_curvatura_macro_de_un_cilindro(self):
        # Semicilindro suave + ruido normal; el radio medio interior casi no cambia.
        angulos = np.linspace(0.0, np.pi, 48)
        ejes = np.linspace(0.0, 30.0, 25)
        angulo_g, eje_g = np.meshgrid(angulos, ejes, indexing="xy")
        radio = 12.0
        ruido = 0.3 * (((np.arange(angulo_g.size) % 2) * 2) - 1).reshape(angulo_g.shape)
        r = radio + ruido
        puntos = np.column_stack(
            (r.ravel() * np.cos(angulo_g.ravel()), eje_g.ravel(), r.ravel() * np.sin(angulo_g.ravel()))
        )
        filas, columnas = angulo_g.shape
        caras = []
        for fila in range(filas - 1):
            for columna in range(columnas - 1):
                inicio = fila * columnas + columna
                caras.append((inicio, inicio + 1, inicio + columnas))
                caras.append((inicio + 1, inicio + 1 + columnas, inicio + columnas))
        caras = np.asarray(caras, dtype=np.int32)
        centro = np.array([0.0, 0.0, 0.0])
        normals = puntos - centro
        # Normal radial en XZ (cilindro en Y).
        normals[:, 1] = 0.0
        normals /= np.maximum(np.linalg.norm(normals, axis=1)[:, None], 1e-12)
        interior = np.ones(len(puntos), dtype=bool)
        # Fijar anillos extremos como "borde" topológico del abanico abierto.
        interior[:columnas] = False
        interior[-columnas:] = False
        interior[::columnas] = False
        interior[columnas - 1 :: columnas] = False

        suaves, _, _ = SuavizadoSuperficie.Aplicar(puntos, caras, normals)
        radio_antes = np.linalg.norm(puntos[interior][:, [0, 2]], axis=1).mean()
        radio_despues = np.linalg.norm(suaves[interior][:, [0, 2]], axis=1).mean()
        self.assertLess(abs(radio_despues - radio_antes), 0.15)
        self.assertLess(
            float(np.std(np.linalg.norm(suaves[interior][:, [0, 2]], axis=1))),
            float(np.std(np.linalg.norm(puntos[interior][:, [0, 2]], axis=1))),
        )


if __name__ == "__main__":
    unittest.main()
