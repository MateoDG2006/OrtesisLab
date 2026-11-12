"""Diagnóstico de unidades de una superficie antes de usar Blender."""

import unittest

from GenerateModelsApp.EscalaMalla import EscalaMalla
from GenerateModelsApp.Excepciones import CalidadInsuficiente, SuperficieInvalida


class DiagnosticoEscala(unittest.TestCase):
    def test_conserva_una_dimension_ya_expresada_en_mm(self):
        resultado = EscalaMalla.Diagnosticar(357.1)
        self.assertEqual(resultado["factor"], 1)
        self.assertEqual(resultado["advertencia"], "")

    def test_corrige_el_stl_pequeno_por_una_potencia_de_diez(self):
        resultado = EscalaMalla.Diagnosticar(1.65943133)
        self.assertEqual(resultado["factor"], 100)
        self.assertAlmostEqual(resultado["dimension_despues_mm"], 165.943133)

    def test_corrige_una_exportacion_demasiado_grande(self):
        resultado = EscalaMalla.Diagnosticar(5000)
        self.assertEqual(resultado["factor"], 0.1)
        self.assertEqual(resultado["dimension_despues_mm"], 500)

    def test_advierte_si_no_hay_una_correccion_decimal_plausible(self):
        resultado = EscalaMalla.Diagnosticar(0)
        self.assertEqual(resultado["factor"], 1)
        self.assertTrue(resultado["advertencia"])

    def test_autoescalado_se_puede_desactivar_sin_perder_la_sugerencia(self):
        resultado = EscalaMalla.Resolver(1.65943133, autoescalar=False)
        self.assertEqual(resultado["factor"], 1)
        self.assertEqual(resultado["factor_sugerido"], 100)
        self.assertAlmostEqual(resultado["dimension_despues_mm"], 1.65943133)
        self.assertIn("Autoescalado desactivado", resultado["advertencia"])

    def test_corrige_mas_de_tres_decimales_cuando_hace_falta(self):
        resultado = EscalaMalla.Diagnosticar(5_000_000)
        self.assertEqual(resultado["factor"], 0.0001)
        self.assertAlmostEqual(resultado["dimension_despues_mm"], 500)

    def test_no_encoge_una_base_en_mm_para_alcanzar_el_paso(self):
        # A-14: 800 mm ya está en rango; un paso inalcanzable no baja a 80 mm.
        with self.assertRaises(CalidadInsuficiente):
            EscalaMalla.Aplicar(
                800,
                True,
                lambda _factor: "listo",
                arista_maxima=800,
                paso_mm=0.001,
            )

    def test_rechaza_si_la_escala_decimal_no_alcanza_el_paso(self):
        with self.assertRaises(CalidadInsuficiente):
            EscalaMalla.Aplicar(
                800_000,
                True,
                lambda _factor: "listo",
                arista_maxima=800_000,
                paso_mm=0.01,
            )

    def test_sin_autoescala_el_paso_sigue_siendo_un_error(self):
        with self.assertRaises(CalidadInsuficiente):
            EscalaMalla.Aplicar(
                2_000_000,
                False,
                lambda _factor: "listo",
                arista_maxima=2_000_000,
                paso_mm=1.0,
            )

    def test_una_malla_ya_en_mm_no_se_encoge_por_debajo_del_rango(self):
        def intentar(_factor):
            raise SuperficieInvalida(
                "No se alcanzó el paso de superficie. "
                "Aumente el paso o revise las unidades en mm."
            )

        with self.assertRaises(SuperficieInvalida):
            EscalaMalla.Aplicar(
                150,
                True,
                intentar,
                arista_maxima=150,
                paso_mm=1.0,
            )

    def test_el_limite_de_vertices_no_cambia_la_escala(self):
        llamadas = []

        def intentar(factor):
            llamadas.append(factor)
            return "listo"

        _resultado, diagnostico = EscalaMalla.Aplicar(
            800,
            True,
            intentar,
            arista_maxima=800,
            paso_mm=1.0,
            n_caras=2,
        )
        self.assertEqual(llamadas, [1.0])
        self.assertEqual(diagnostico["factor"], 1.0)
        self.assertAlmostEqual(diagnostico["dimension_despues_mm"], 800)

    def test_una_superficie_en_centimetros_conserva_el_factor_decimal(self):
        llamadas = []

        def intentar(factor):
            llamadas.append(factor)
            return "listo"

        _resultado, diagnostico = EscalaMalla.Aplicar(
            16.55737066,
            True,
            intentar,
            arista_maxima=2.14003,
            paso_mm=0.933,
            n_caras=1852,
        )
        self.assertEqual(llamadas, [10.0])
        self.assertEqual(diagnostico["factor"], 10.0)
        self.assertAlmostEqual(diagnostico["dimension_despues_mm"], 165.5737066, places=3)


if __name__ == "__main__":
    unittest.main()
