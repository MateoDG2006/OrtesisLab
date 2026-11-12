"""Contratos compartidos entre núcleo, Blender y la web."""

from __future__ import annotations

import numpy as np

from .util.Utilidades import Configuracion

VERSION = "OrtesisLab-contratos-1"


def ValidarTuplaSuperficie(tupla: tuple) -> None:
    """Entrada: (vértices, caras, normales, borde)."""
    if not isinstance(tupla, tuple) or len(tupla) != 4:
        raise ValueError("La superficie debe ser una tupla de cuatro arreglos.")
    vertices, caras, normales, borde = tupla
    puntos = np.asarray(vertices)
    if puntos.ndim != 2 or puntos.shape[1] != 3:
        raise ValueError("Los vértices deben ser N×3.")
    if len(caras) == 0:
        raise ValueError("La superficie no tiene caras.")
    if np.asarray(normales).shape[0] != len(puntos):
        raise ValueError("Las normales no coinciden con los vértices.")
    if len(borde) != len(puntos):
        raise ValueError("El borde no coincide con los vértices.")


def ValidarOpciones(options: dict | None) -> dict:
    """Opciones de generación: claves reconocidas y tipos básicos."""
    plantilla = Configuracion.ParametrosDefecto()
    opciones = {} if options is None else dict(options)
    desconocidos = set(opciones) - set(plantilla)
    if desconocidos:
        raise ValueError(f"Opciones no reconocidas: {sorted(desconocidos)}")
    return plantilla | opciones


def ValidarFicha(ficha: dict) -> None:
    """Ficha visible en la página de comparación."""
    for clave in ("archivo", "patron", "volumen", "peso"):
        if clave not in ficha:
            raise ValueError(f"Falta la clave '{clave}' en la ficha.")


def ValidarInformeValidacion(informe: dict) -> None:
    """Informe geométrico homogéneo entre web y Blender."""
    for clave in (
        "open_edges",
        "nonmanifold_edges",
        "degenerate_faces",
        "triangles",
        "components",
        "triangle_crossings",
        "ok",
    ):
        if clave not in informe:
            raise ValueError(f"Falta '{clave}' en el informe de validación.")


def ValidarSidecarStl(documento: dict) -> None:
    """JSON hermano de un STL exportado desde Blender."""
    if not isinstance(documento, dict):
        raise ValueError("El sidecar debe ser un objeto JSON.")
    for clave in ("parameters", "validation", "stl_units"):
        if clave not in documento:
            raise ValueError(f"Falta '{clave}' en el sidecar STL.")
    ValidarInformeValidacion(documento["validation"])
    if not isinstance(documento["parameters"], dict):
        raise ValueError("parameters debe ser un objeto.")
