"""Arranque de un contenedor OrtesisLab: migrate, web o worker.

Uso: ``python scripts/EntradaContenedor.py migrate|web|worker``
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def _Migrar() -> int:
    return subprocess.call(
        [sys.executable, "-m", "alembic", "upgrade", "head"],
        cwd=RAIZ,
        env=os.environ.copy(),
    )


def _Web() -> int:
    entorno = os.environ.copy()
    entorno["PYTHONPATH"] = os.pathsep.join(
        [
            str(RAIZ / "apps" / "web"),
            str(RAIZ / "apps" / "ortesis-plugin"),
            entorno.get("PYTHONPATH", ""),
        ]
    )
    return subprocess.call(
        [
            sys.executable,
            "-m",
            "reflex",
            "run",
            "--env",
            "prod",
            "--single-port",
            "--backend-host",
            "0.0.0.0",
            "--frontend-port",
            "3000",
        ],
        cwd=RAIZ / "apps" / "web",
        env=entorno,
    )


def _Worker() -> int:
    return subprocess.call(
        [sys.executable, str(RAIZ / "scripts" / "EjecutarTrabajador.py")],
        cwd=RAIZ,
        env=os.environ.copy(),
    )


def main(argv: list[str] | None = None) -> int:
    argumentos = argv if argv is not None else sys.argv[1:]
    if len(argumentos) != 1 or argumentos[0] not in {"migrate", "web", "worker"}:
        print("Uso: EntradaContenedor.py migrate|web|worker", file=sys.stderr)
        return 2
    modo = argumentos[0]
    if modo == "migrate":
        return _Migrar()
    if modo == "web":
        return _Web()
    return _Worker()


if __name__ == "__main__":
    raise SystemExit(main())
