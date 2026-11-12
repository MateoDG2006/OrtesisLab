"""Validación de mallas sólidas solo con NumPy (sin Blender).

Entrada: vértices (N,3) y caras poligonales o triángulos.
Proceso: triangula, mide aristas, componentes y degeneración opcional.
Salida: dict con conteos y ``ok`` (una sola pieza cerrada y manifold).
"""

from __future__ import annotations

from collections import defaultdict

import numpy as np

from .util.Utilidades import Configuracion

_TOPE_CRUCES_HEURISTICA = 800


class ValidadorSolido:
    """Comprueba topología de un sólido triangular antes de publicar."""

    @staticmethod
    def _Triangulos(caras) -> np.ndarray:
        salida = []
        for cara in caras:
            indices = [int(vertice) for vertice in cara]
            if len(indices) < 3:
                continue
            for posicion in range(1, len(indices) - 1):
                salida.append((indices[0], indices[posicion], indices[posicion + 1]))
        return np.asarray(salida, dtype=np.int64)

    @staticmethod
    def _ContarComponentes(triangulos: np.ndarray) -> int:
        if len(triangulos) == 0:
            return 0
        padre = {}

        def buscar(nodo):
            raiz = padre.setdefault(nodo, nodo)
            if raiz != nodo:
                padre[nodo] = buscar(raiz)
            return padre[nodo]

        def unir(a, b):
            ra_a, ra_b = buscar(a), buscar(b)
            if ra_a != ra_b:
                padre[ra_b] = ra_a

        for a, b, c in triangulos:
            unir(a, b)
            unir(b, c)
            unir(a, c)
        return len({buscar(vertice) for vertice in padre})

    @staticmethod
    def _ContarAristas(triangulos: np.ndarray) -> tuple[int, int]:
        conteo: dict[tuple[int, int], int] = defaultdict(int)
        for a, b, c in triangulos:
            for i, j in ((a, b), (b, c), (c, a)):
                arista = (i, j) if i < j else (j, i)
                conteo[arista] += 1
        abiertas = sum(veces == 1 for veces in conteo.values())
        no_manifold = sum(veces > 2 for veces in conteo.values())
        return abiertas, no_manifold

    @staticmethod
    def _CarasDegeneradas(puntos: np.ndarray, triangulos: np.ndarray, area_minima: float) -> int:
        degeneradas = 0
        for a, b, c in triangulos:
            pa, pb, pc = puntos[a], puntos[b], puntos[c]
            cruz = np.cross(pb - pa, pc - pa)
            area = 0.5 * float(np.linalg.norm(cruz))
            if area < area_minima:
                degeneradas += 1
        return degeneradas

    @staticmethod
    def _CrucesHeuristica(puntos: np.ndarray, triangulos: np.ndarray, limite: int) -> int:
        """Heurística ligera: solo en mallas pequeñas; no sustituye BVH de Blender."""
        if len(triangulos) > limite:
            return 0
        cruces = 0
        for indice, (a, b, c) in enumerate(triangulos):
            verts_a = {a, b, c}
            pa, pb, pc = puntos[a], puntos[b], puntos[c]
            normal = np.cross(pb - pa, pc - pa)
            longitud = float(np.linalg.norm(normal))
            if longitud < 1e-15:
                continue
            normal = normal / longitud
            for otro, (x, y, z) in enumerate(triangulos[indice + 1 :], start=indice + 1):
                if verts_a & {x, y, z}:
                    continue
                px, py, pz = puntos[x], puntos[y], puntos[z]
                centro = (px + py + pz) / 3.0
                if abs(float(np.dot(centro - pa, normal))) > 1e-3:
                    continue
                # Triángulos coplanares cercanos: contar como posible cruce.
                if ValidadorSolido._TrianguloContiene(puntos, (a, b, c), centro):
                    cruces += 1
                    break
        return cruces

    @staticmethod
    def _TrianguloContiene(puntos: np.ndarray, tri: tuple[int, int, int], punto: np.ndarray) -> bool:
        a, b, c = tri
        total = 0.0
        for i, j, k in ((a, b, c), (b, c, a), (c, a, b)):
            u = puntos[j] - puntos[i]
            v = puntos[k] - puntos[i]
            w = punto - puntos[i]
            denom = float(np.dot(u, u) * np.dot(v, v) - np.dot(u, v) ** 2)
            if denom < 1e-18:
                return False
            s = (np.dot(u, u) * np.dot(w, v) - np.dot(u, v) * np.dot(w, u)) / denom
            t = (np.dot(v, v) * np.dot(w, u) - np.dot(u, v) * np.dot(w, v)) / denom
            if s >= -1e-6 and t >= -1e-6 and s + t <= 1.0 + 1e-6:
                total += 1
        return total == 3

    @staticmethod
    def Comprobar(vertices, caras, *, intersections: bool = True) -> dict:
        """Salida: informe compatible con ``ValidadorMalla``."""
        puntos = np.asarray(vertices, dtype=np.float64)
        if puntos.ndim != 2 or puntos.shape[1] != 3:
            raise ValueError("Los vértices deben ser una matriz N×3.")
        triangulos = ValidadorSolido._Triangulos(caras)
        area_minima = float(Configuracion.ValorLimite("degenerate_area"))
        abiertas, no_manifold = ValidadorSolido._ContarAristas(triangulos)
        from .Malla import AnalizadorMalla

        no_manifold_verts = int(
            AnalizadorMalla._VerticesNoManifold(triangulos, len(puntos))
        )
        informe = {
            "open_edges": abiertas,
            "nonmanifold_edges": no_manifold,
            "nonmanifold_verts": no_manifold_verts,
            "degenerate_faces": ValidadorSolido._CarasDegeneradas(puntos, triangulos, area_minima),
            "triangles": int(len(triangulos)),
            "components": ValidadorSolido._ContarComponentes(triangulos),
            "triangle_crossings": 0,
        }
        if intersections:
            informe["triangle_crossings"] = ValidadorSolido._CrucesHeuristica(
                puntos, triangulos, _TOPE_CRUCES_HEURISTICA
            )
        informe["ok"] = (
            not any(
                informe[clave]
                for clave in (
                    "open_edges",
                    "nonmanifold_edges",
                    "nonmanifold_verts",
                    "degenerate_faces",
                    "triangle_crossings",
                )
            )
            and informe["components"] == 1
            and informe["triangles"] > 0
            and np.all(np.isfinite(puntos))
        )
        return informe
