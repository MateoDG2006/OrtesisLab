"""Script del comando de consola del proyecto.

Delegación fina hacia ``OrtesisLabPlugin.consola``. No genera ortesis ni abre Blender.
Se puede lanzar con: python scripts/IniciarConsola.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "apps" / "ortesis-plugin"))

from OrtesisLabPlugin.consola import main as _main  # noqa: E402


class IniciarConsola:
    @staticmethod
    def Ejecutar() -> None:
        _main()


if __name__ == "__main__":
    IniciarConsola.Ejecutar()
