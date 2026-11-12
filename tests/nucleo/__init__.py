"""Pruebas del núcleo geométrico: validación, catálogo, volumen y material."""
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(_RAIZ / "apps" / "web"), str(_RAIZ / "apps" / "ortesis-plugin")]
