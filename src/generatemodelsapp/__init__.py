def main() -> None:
    from pathlib import Path
    import sys

    plugin = Path(__file__).resolve().parents[2] / "apps" / "ortesis-plugin"
    if str(plugin) not in sys.path:
        sys.path.insert(0, str(plugin))
    from OrtesisLabPlugin.consola import main as consola

    consola()
