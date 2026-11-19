"""Backend de arrays: NumPy por defecto, CuPy si ``ORTESISLAB_ARRAY=cupy``.

El núcleo sigue entregando ``numpy.ndarray`` al resto del pipeline; CuPy solo
acelera kernels puntuales (p. ej. distancias de patrón) cuando hay CUDA.
"""

from __future__ import annotations

import os

import numpy as np
from OrtesisLabPlugin.util.Utilidades import Registro

_BACKEND = (os.environ.get("ORTESISLAB_ARRAY") or "numpy").strip().lower()
_xp = np
_nombre = "numpy"


def _Inicializar() -> None:
    global _xp, _nombre
    if _BACKEND not in ("cupy", "cuda", "gpu"):
        _xp = np
        _nombre = "numpy"
        return
    try:
        import cupy as cp

        # Fuerza detección temprana de GPU.
        _ = cp.cuda.runtime.getDeviceCount()
        _xp = cp
        _nombre = "cupy"
        Registro.Obtener("nucleo").info("Arrays: backend CuPy (GPU).")
    except Exception as exc:  # noqa: BLE001 — cualquier fallo vuelve a CPU
        _xp = np
        _nombre = "numpy"
        Registro.Obtener("nucleo").warning("Arrays: CuPy no disponible (%s); se usa NumPy.", exc)


_Inicializar()


class Arrays:
    """Fachada mínima compartida por patrones y muestreo."""

    @staticmethod
    def nombre() -> str:
        return _nombre

    @staticmethod
    def xp():
        return _xp

    @staticmethod
    def asarray(valor, dtype=None):
        if dtype is None:
            return _xp.asarray(valor)
        return _xp.asarray(valor, dtype=dtype)

    @staticmethod
    def to_numpy(valor) -> np.ndarray:
        if _nombre == "cupy":
            return _xp.asnumpy(valor)
        return np.asarray(valor)
