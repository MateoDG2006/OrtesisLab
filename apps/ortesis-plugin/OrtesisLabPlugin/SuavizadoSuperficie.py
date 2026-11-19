"""Suavizado Taubin del ruido de malla en el interior de la superficie.

Quita oscilaciones locales (facetas, hoyuelos de escaneo) sin mover el contorno
ni aplanar la curvatura anatómica principal. El desplazamiento acumulado por
vértice queda acotado.
"""

from __future__ import annotations

import numpy as np

from .Malla import AnalizadorMalla
from .SuavizadoBorde import SuavizadoBorde
from .util.Utilidades import Configuracion, Registro


class SuavizadoSuperficie:
    """Taubin λ/μ sobre vértices interiores; el borde queda fijado."""

    @staticmethod
    def Aplicar(vertices, caras, normales):
        logger = Registro.Obtener("malla")
        puntos = np.array(vertices, dtype=np.float64, copy=True)
        normales_salida = np.array(normales, dtype=np.float64, copy=True)
        iteraciones = int(Configuracion.ValorLimite("surface_smooth_iterations"))
        lam = float(Configuracion.ValorLimite("surface_smooth_lambda"))
        mu = float(Configuracion.ValorLimite("surface_smooth_mu"))
        if iteraciones <= 0 or lam <= 0 or len(puntos) == 0:
            return puntos, normales_salida, 0.0

        caras_idx = np.asarray(caras, dtype=np.int32)
        todas = np.vstack(
            (caras_idx[:, [0, 1]], caras_idx[:, [1, 2]], caras_idx[:, [2, 0]])
        )
        aristas, cuentas = np.unique(np.sort(todas, axis=1), axis=0, return_counts=True)
        contorno = aristas[cuentas == 1]
        borde = np.zeros(len(puntos), dtype=bool)
        if len(contorno):
            borde[np.unique(contorno.ravel())] = True
        interior = ~borde
        if not np.any(interior):
            return puntos, normales_salida, 0.0

        originales = puntos.copy()
        tope = float(Configuracion.ValorLimite("surface_smooth_max_mm"))
        area_minima = Configuracion.ValorLimite("degenerate_area")
        referencia = np.cross(
            puntos[caras_idx[:, 1]] - puntos[caras_idx[:, 0]],
            puntos[caras_idx[:, 2]] - puntos[caras_idx[:, 0]],
        )

        for _ in range(iteraciones):
            for factor in (lam, mu):
                if factor == 0.0:
                    continue
                laplaciano = SuavizadoSuperficie._Laplaciano(puntos, aristas)
                delta = np.zeros_like(puntos)
                delta[interior] = factor * laplaciano[interior]
                if np.isfinite(tope) and tope > 0:
                    propuesto = puntos + delta
                    desde_origen = propuesto - originales
                    distancia = np.linalg.norm(desde_origen, axis=1)
                    exceso = distancia > tope
                    if np.any(exceso):
                        desde_origen[exceso] *= (tope / distancia[exceso])[:, None]
                        delta = (originales + desde_origen) - puntos
                    paso = np.linalg.norm(delta, axis=1)
                    largo = paso > tope
                    if np.any(largo):
                        delta[largo] *= (tope / paso[largo])[:, None]
                delta[np.linalg.norm(delta, axis=1) < 1e-9] = 0.0
                delta = SuavizadoSuperficie._SinVoltear(
                    puntos, delta, caras_idx, referencia, area_minima, interior, logger
                )
                puntos = puntos + delta

        # Tras mover puntos, las normales siguen a las caras (acuerdo A-04).
        normales_salida = AnalizadorMalla.NormalesDeCaras(puntos, caras_idx)

        desplazamiento = float(np.linalg.norm(puntos - originales, axis=1).max())
        if desplazamiento > 0:
            logger.info(
                "Interior suavizado (Taubin): desplazamiento máximo %.3f mm.",
                desplazamiento,
            )
        return puntos, normales_salida, desplazamiento

    @staticmethod
    def _Laplaciano(puntos: np.ndarray, aristas: np.ndarray) -> np.ndarray:
        suma = np.zeros_like(puntos)
        grado = np.zeros(len(puntos), dtype=np.float64)
        np.add.at(suma, aristas[:, 0], puntos[aristas[:, 1]])
        np.add.at(suma, aristas[:, 1], puntos[aristas[:, 0]])
        np.add.at(grado, aristas[:, 0], 1.0)
        np.add.at(grado, aristas[:, 1], 1.0)
        grado = np.maximum(grado, 1.0)
        return suma / grado[:, None] - puntos

    @staticmethod
    def _SinVoltear(puntos, delta, caras, referencia, area_minima, interior, logger):
        for _ in range(12):
            if not SuavizadoBorde._CarasRotas(puntos + delta, caras, referencia, area_minima):
                return delta
            culpables = np.unique(
                caras[
                    SuavizadoBorde._MascaraRota(
                        puntos + delta, caras, referencia, area_minima
                    )
                ]
            )
            culpables = culpables[interior[culpables]]
            if len(culpables) == 0:
                break
            delta[culpables] *= 0.5
        else:
            rotas = SuavizadoBorde._MascaraRota(
                puntos + delta, caras, referencia, area_minima
            )
            if np.any(rotas):
                culpables = np.unique(caras[rotas])
                culpables = culpables[interior[culpables]]
                delta[culpables] = 0.0
                logger.warning(
                    "Parte del interior no se pudo suavizar sin voltear caras."
                )
        return delta
