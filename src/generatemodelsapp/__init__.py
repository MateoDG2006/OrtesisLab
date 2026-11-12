def main() -> None:
    from pathlib import Path
    import sys

    raiz = Path(__file__).resolve().parents[2]
    if str(raiz) not in sys.path:
        sys.path.insert(0, str(raiz))
    from GenerateModelsApp.consola import main as consola

    consola()
