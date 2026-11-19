"""Patrones de nervadura.

La distancia se mide en la proyección XY, en milímetros, hasta el eje
de la nervadura. HoneyComb y Square conservan su nombre de catálogo;
su código geométrico es HEX y SQUARE.
TRIANGLE y MINIMALISTIC se rechazan: no hay geometría para esos nombres.
"""

from __future__ import annotations

import math

import numpy as np

from ..Excepciones import PatronNoImplementado, PatronNoReconocido, PresupuestoExcedido
from ..util.Arrays import Arrays
from ..util.Utilidades import Configuracion


class Patron:
    """Distancia al eje de la nervadura, y si el patrón tiene celosía o semilla."""

    codigo = ""
    celosia = True
    semilla = False

    def __init__(self):
        self.name = ""

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        # Las subclases que generan malla reemplazan este método.
        raise PatronNoImplementado(self.name or type(self).__name__)

    @staticmethod
    def RotarXy(puntos, anguloGrados: float):
        # Gira la proyección XY. El macizo no la usa.
        angulo = math.radians(anguloGrados)
        coseno, seno = math.cos(angulo), math.sin(angulo)
        xp = Arrays.xp()
        xy = Arrays.asarray(puntos[:, :2])
        matriz = Arrays.asarray([[coseno, -seno], [seno, coseno]])
        return Arrays.to_numpy(xy @ matriz)

    @staticmethod
    def DistanciaCuadricula(uv, celda: float):
        # Distancia al eje más cercano de una retícula cuadrada.
        xp = Arrays.xp()
        puntos = Arrays.asarray(uv)
        return Arrays.to_numpy(xp.min(xp.abs((puntos + celda * 0.5) % celda - celda * 0.5), axis=1))

    @staticmethod
    def DistanciaSemillas(uv, celda: float, semilla: int, organico: bool):
        """Entrada: puntos XY y celda en mm. Proceso: evalúa semillas próximas
        y verifica una cota antes de descartar las lejanas. Salida: distancia al
        borde de celda original. Errores: parámetros geométricos inválidos.
        Efectos secundarios: ninguno.
        """
        bajo = uv.min(0) - 3 * celda
        alto = uv.max(0) + 3 * celda
        area = float(np.prod(np.maximum(alto - bajo, 0.0)))
        tope_area = Configuracion.ValorLimite("max_seed_area_mm2")
        if area > tope_area:
            raise PresupuestoExcedido(
                f"El área de siembra ({area:.0f} mm²) supera el máximo de {tope_area:g} mm²."
            )
        paso_y = celda * math.sqrt(3) / 2
        generador = np.random.default_rng(semilla)
        jitter = Configuracion.ValorLimite("voronoi_jitter")
        epsilon = Configuracion.ValorLimite("seed_separation_epsilon")
        lote = int(Configuracion.ValorLimite("pattern_batch"))
        if lote <= 0:
            raise PresupuestoExcedido("pattern_batch debe ser un entero positivo.")
        semillas = []
        for fila, y in enumerate(np.arange(bajo[1], alto[1] + paso_y, paso_y)):
            for x in np.arange(bajo[0], alto[0] + celda, celda):
                punto = np.array([x + (fila % 2) * celda * 0.5, y])
                if organico:
                    punto = punto + generador.uniform(-jitter, jitter, 2) * celda
                semillas.append(punto)
        semillas = np.array(semillas)
        resultado = np.empty(len(uv))
        orden = np.argsort(uv[:, 0], kind="stable")
        margen = 3 * celda
        for inicio in range(0, len(uv), lote):
            indices = orden[inicio : inicio + lote]
            puntos = uv[indices]
            inferior = puntos.min(axis=0) - margen
            superior = puntos.max(axis=0) + margen
            cercanas = semillas[
                np.all((semillas >= inferior) & (semillas <= superior), axis=1)
            ]
            if len(cercanas) < 2:
                distancias, _radio = Patron._DistanciaPlanos(puntos, semillas, epsilon)
            else:
                distancias, radio = Patron._DistanciaPlanos(puntos, cercanas, epsilon)
                # Una semilla excluida dista al menos margen del punto.
                # Su bisectriz queda a >= (margen - radio) / 2; si la
                # distancia local es menor, el resultado ya es exacto.
                pendientes = radio + 2 * distancias >= margen
                if np.any(pendientes):
                    distancias[pendientes], _radio = Patron._DistanciaPlanos(
                        puntos[pendientes], semillas, epsilon
                    )
            resultado[indices] = distancias
        return resultado

    @staticmethod
    def _DistanciaPlanos(puntos, semillas, epsilon):
        """Entrada: puntos y semillas XY. Proceso: calcula la bisectriz más
        cercana de la semilla vecina. Salida: distancias y radio al centro.
        Efectos secundarios: ninguno. Usa CuPy si ``ORTESISLAB_ARRAY=cupy``.
        """
        xp = Arrays.xp()
        puntos_x = Arrays.asarray(puntos)
        semillas_x = Arrays.asarray(semillas)
        distancias2 = xp.sum((puntos_x[:, None, :] - semillas_x[None, :, :]) ** 2, axis=2)
        cercano = xp.argmin(distancias2, axis=1)
        centro = semillas_x[cercano]
        separacion = xp.linalg.norm(semillas_x[None, :, :] - centro[:, None, :], axis=2)
        denominador = xp.where(separacion > epsilon, 2 * separacion, 1)
        indice = xp.arange(len(puntos_x))
        plano = (distancias2 - distancias2[indice, cercano, None]) / denominador
        plano[indice, cercano] = xp.inf
        return (
            Arrays.to_numpy(xp.min(plano, axis=1)),
            Arrays.to_numpy(xp.sqrt(distancias2[indice, cercano])),
        )

    @staticmethod
    def Geometricos() -> dict[str, Patron]:
        # Solo los patrones que sí construyen malla.
        return {
            "VORONOI": Voronoi(),
            "HEX": HoneyComb(),
            "DIAMOND": Diamond(),
            "SQUARE": Square(),
            "SOLID": Solid(),
        }

    @staticmethod
    def Obtener(codigoONombre: str) -> Patron:
        # Acepta el código (HEX) o el nombre de catálogo (HoneyComb, macizo).
        if not isinstance(codigoONombre, str) or not codigoONombre.strip():
            raise PatronNoReconocido()
        clave = codigoONombre.strip().upper()
        if clave in {"TRIANGLE", "MINIMALISTIC"}:
            raise PatronNoImplementado(codigoONombre.strip())
        clave = _ALIAS.get(clave, clave)
        tabla = Patron.Geometricos()
        if clave not in tabla:
            raise PatronNoReconocido()
        return tabla[clave]

    @staticmethod
    def Celosia(codigo: str) -> bool:
        patron = Patron.Geometricos().get(str(codigo))
        if patron is None:
            return True
        return patron.celosia

    @staticmethod
    def PideSemilla(codigo: str) -> bool:
        patron = Patron.Geometricos().get(str(codigo))
        return patron is not None and patron.semilla


class HoneyComb(Patron):
    # Hexágonos regulares. En la geometría el código es HEX.
    codigo = "HEX"

    def __init__(self):
        super().__init__()
        self.name = "HoneyComb"

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        return Patron.DistanciaSemillas(Patron.RotarXy(puntos, anguloGrados), celdaMm, semilla, False)


class Square(Patron):
    codigo = "SQUARE"

    def __init__(self):
        super().__init__()
        self.name = "Square"

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        return Patron.DistanciaCuadricula(Patron.RotarXy(puntos, anguloGrados), celdaMm)


class Diamond(Patron):
    codigo = "DIAMOND"

    def __init__(self):
        super().__init__()
        self.name = "Diamond"

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        # La cuadrícula se gira 45° para que las celdas queden en rombo.
        uv = Patron.RotarXy(puntos, anguloGrados)
        diagonal = math.sqrt(0.5)
        uv = uv @ np.array([[diagonal, -diagonal], [diagonal, diagonal]])
        return Patron.DistanciaCuadricula(uv, celdaMm)


class Voronoi(Patron):
    codigo = "VORONOI"
    semilla = True

    def __init__(self):
        super().__init__()
        self.name = "Voronoi"

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        return Patron.DistanciaSemillas(Patron.RotarXy(puntos, anguloGrados), celdaMm, semilla, True)


class Solid(Patron):
    codigo = "SOLID"
    celosia = False

    def __init__(self):
        super().__init__()
        self.name = "Solid"

    def Distancia(self, puntos, celdaMm: float, anguloGrados: float, semilla: int):
        # El macizo no tiene huecos: la distancia al eje es cero en todos los puntos.
        return np.zeros(len(puntos))


_ALIAS = {
    "HONEYCOMB": "HEX",
    "ROMBOS": "DIAMOND",
    "CUADRICULA": "SQUARE",
    "CUADRÍCULA": "SQUARE",
    "MACIZO": "SOLID",
    "ORGANICO": "VORONOI",
    "ORGÁNICO": "VORONOI",
    "VORONOI": "VORONOI",
    "HEX": "HEX",
    "DIAMOND": "DIAMOND",
    "SQUARE": "SQUARE",
    "SOLID": "SOLID",
}
