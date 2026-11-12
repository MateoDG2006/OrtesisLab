"""Script del comando de consola del proyecto.

Delegación fina hacia ``GenerateModelsApp.consola``. No genera ortesis ni abre Blender.
Se puede lanzar con: python scripts/IniciarConsola.py
"""

from GenerateModelsApp.consola import main as _main


class IniciarConsola:
    @staticmethod
    def Ejecutar() -> None:
        _main()


if __name__ == "__main__":
    IniciarConsola.Ejecutar()
