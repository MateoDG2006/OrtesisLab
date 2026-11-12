"""Diagnóstico de unidades para una superficie de ortesis.

STL no guarda unidades. Esta clase solo corrige errores decimales inequívocos;
si ninguna potencia de diez deja la base en el rango configurado, devuelve una
advertencia para que la persona confirme las dimensiones.

Si otra potencia de diez, todavía dentro del rango, sí alcanza el paso, se usa
esa. El límite de vértices no encoge la ortesis: la subdivisión se detiene ahí.
"""

from __future__ import annotations

import math

from .Excepciones import CalidadInsuficiente, SuperficieInvalida
from .util.Utilidades import Configuracion, Registro


class EscalaMalla:
    """Decide si el eje mayor parece expresado en una unidad distinta de mm."""

    EXPONENTE_MINIMO = -6
    EXPONENTE_MAXIMO = 6

    @staticmethod
    def Candidatos(dimensionMaximaMm: float) -> list[float]:
        # De la corrección más pequeña a la mayor. Incluye 1 cuando ya está en milímetros.
        minimo = Configuracion.ValorLimite("min_plausible_surface_extent_mm")
        maximo = Configuracion.ValorLimite("max_plausible_surface_extent_mm")
        dimension = float(dimensionMaximaMm)
        if not math.isfinite(dimension) or dimension <= 0:
            return []
        factores = []
        for exponente in range(EscalaMalla.EXPONENTE_MINIMO, EscalaMalla.EXPONENTE_MAXIMO + 1):
            factor = 10.0 ** exponente
            if minimo <= dimension * factor <= maximo:
                factores.append((exponente, factor))
        factores.sort(key=lambda item: (abs(item[0]), -item[0]))
        return [factor for _exponente, factor in factores]

    @staticmethod
    def Diagnosticar(dimensionMaximaMm: float) -> dict:
        minimo = Configuracion.ValorLimite("min_plausible_surface_extent_mm")
        maximo = Configuracion.ValorLimite("max_plausible_surface_extent_mm")
        dimension = float(dimensionMaximaMm)
        resultado = {
            "factor": 1.0,
            "dimension_antes_mm": dimension,
            "dimension_despues_mm": dimension,
            "advertencia": "",
        }
        if not math.isfinite(dimension) or dimension <= 0:
            resultado["advertencia"] = "No se pudo determinar una dimensión válida para revisar la escala."
            return resultado

        candidatos = EscalaMalla.Candidatos(dimension)
        if candidatos:
            factor = candidatos[0]
            resultado["factor"] = factor
            resultado["dimension_despues_mm"] = dimension * factor
            return resultado

        resultado["advertencia"] = (
            f"La malla mide {dimension:.2f} mm en su eje mayor, fuera del rango "
            f"esperado de {minimo:g} a {maximo:g} mm. Revise las unidades antes de generar."
        )
        return resultado

    @staticmethod
    def AlcanzaPaso(aristaMaxima: float, pasoMm: float, factor: float) -> bool:
        # 16 mitades tienen que dejar la arista más larga por debajo del paso.
        if not math.isfinite(aristaMaxima) or aristaMaxima <= 0:
            return True
        if not math.isfinite(pasoMm) or pasoMm <= 0:
            return True
        rondas = int(Configuracion.ValorLimite("surface_subdivision_iterations"))
        return aristaMaxima * factor <= pasoMm * 1.001 * (2 ** rondas)

    @staticmethod
    def Presupuesto(aristaMaxima: float, pasoMm: float, nCaras: int, factor: float) -> bool:
        # Cada pasada puede cuadruplicar los triángulos. Eso no debe arrancar.
        if not EscalaMalla.AlcanzaPaso(aristaMaxima, pasoMm, factor):
            return False
        if nCaras <= 0:
            return True
        limite = int(Configuracion.ValorLimite("max_surface_vertices"))
        if nCaras > limite:
            return False
        longitud = float(aristaMaxima) * float(factor)
        tope = float(pasoMm) * 1.001
        if longitud <= tope:
            return True
        niveles = math.ceil(math.log2(longitud / tope))
        if niveles >= 12:
            return False
        return nCaras <= limite / (4 ** niveles)

    @staticmethod
    def EsFalloDePaso(exc: BaseException) -> bool:
        # El paso no cupo: faltaron rondas o el detalle superó el límite de vértices.
        if isinstance(exc, CalidadInsuficiente):
            return True
        return isinstance(exc, SuperficieInvalida) and "paso de superficie" in str(exc)

    @staticmethod
    def Aplicar(
        dimensionMaximaMm: float,
        autoescalar: bool,
        operacion,
        *,
        arista_maxima: float | None = None,
        paso_mm: float | None = None,
        n_caras: int | None = None,
    ):
        """Decide la escala una sola vez y la mantiene. Un paso inalcanzable
        no reduce el tamaño físico de una base ya expresada en mm."""
        dimension = float(dimensionMaximaMm)
        diagnostico = dict(EscalaMalla.Diagnosticar(dimension))
        candidatos = EscalaMalla.Candidatos(dimension)
        if autoescalar:
            factor = candidatos[0] if candidatos else float(diagnostico["factor"])
            diagnostico["factor"] = factor
            diagnostico["factor_sugerido"] = factor
            diagnostico["dimension_despues_mm"] = dimension * factor
            if factor != 1.0:
                diagnostico["advertencia"] = ""
        else:
            sugerido = candidatos[0] if candidatos else float(diagnostico["factor"])
            factor = 1.0
            diagnostico["factor"] = 1.0
            diagnostico["factor_sugerido"] = sugerido
            diagnostico["dimension_despues_mm"] = dimension
            if sugerido != 1.0:
                diagnostico["advertencia"] = (
                    "Autoescalado desactivado. "
                    f"La corrección sugerida es ×{sugerido:g}: "
                    f"{dimension:.2f} a {dimension * sugerido:.2f} mm."
                )

        if (
            arista_maxima is not None
            and paso_mm is not None
            and not EscalaMalla.AlcanzaPaso(arista_maxima, float(paso_mm), factor)
        ):
            raise CalidadInsuficiente(
                f"El paso {float(paso_mm):.3f} mm no se alcanza con la escala ×{factor:g}."
            )
        if (
            n_caras
            and arista_maxima is not None
            and paso_mm is not None
            and not EscalaMalla.Presupuesto(
                arista_maxima, float(paso_mm), int(n_caras), factor
            )
        ):
            # La escala ya está fijada. El refinador rechazará si el paso no cabe.
            Registro.Obtener("escala").info(
                "La escala x%g puede no alcanzar el paso dentro del límite de vértices. "
                "Se mantiene el tamaño.",
                factor,
            )

        resultado = operacion(factor)
        diagnostico["factor"] = float(factor)
        diagnostico["dimension_despues_mm"] = dimension * float(factor)
        return resultado, diagnostico

    @staticmethod
    def Resolver(dimensionMaximaMm: float, autoescalar: bool = True) -> dict:
        """Devuelve el factor aplicado y conserva el factor sugerido para informar."""
        diagnostico = dict(EscalaMalla.Diagnosticar(dimensionMaximaMm))
        sugerido = float(diagnostico["factor"])
        diagnostico["factor_sugerido"] = sugerido
        if autoescalar:
            return diagnostico

        diagnostico["factor"] = 1.0
        diagnostico["dimension_despues_mm"] = diagnostico["dimension_antes_mm"]
        if sugerido != 1.0:
            diagnostico["advertencia"] = (
                "Autoescalado desactivado. "
                f"La corrección sugerida es ×{sugerido:g}: "
                f"{diagnostico['dimension_antes_mm']:.2f} a "
                f"{dimensionMaximaMm * sugerido:.2f} mm."
            )
        return diagnostico
