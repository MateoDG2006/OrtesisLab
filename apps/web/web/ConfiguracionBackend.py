"""Valores ajustables del backend, leídos de ``core/config/<area>.yaml``.

Los secretos y las URL van en el entorno (``Ajustes``); aquí solo hay límites,
tiempos y tamaños. Un archivo o una clave ausente es un error de despliegue.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

CARPETA = Path(__file__).resolve().parents[3] / "core" / "config"


class ConfiguracionBackend:
    @staticmethod
    @lru_cache(maxsize=None)
    def Cargar(area: str) -> dict:
        return yaml.safe_load((CARPETA / f"{area}.yaml").read_text(encoding="utf-8"))
