"""Infraestructura local: arranque, parada, estado, respaldo y reinicio de la base.

PostgreSQL, MinIO y Redis salen de ``apps/db/compose.yaml``.
Las cinco operaciones conservan las salvaguardas de nombre, base de desarrollo
y confirmación. No aplica migraciones.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
COMPOSE = RAIZ / "apps" / "db" / "compose.yaml"
BACKUPS = RAIZ / "apps" / "db" / "backups"
PREPARAR = RAIZ / "apps" / "db" / "preparar_base.sql"
DUMP = re.compile(r"[A-Za-z0-9._-]{1,80}\.dump")
DESARROLLO = "ortesislab_dev"


def _variable(nombre: str, defecto: str) -> str:
    valor = os.environ.get(nombre, "").strip()
    return valor or defecto


def _compose(perfil: str | None = None) -> list[str]:
    env = Path(_variable("ENV_FILE", "apps/db/.env"))
    if not env.is_absolute():
        env = RAIZ / env
    if not env.is_file():
        raise SystemExit(f"Falta {env}. Ejecute make install y complete las claves.")
    comando = ["docker", "compose", "-f", str(COMPOSE), "--env-file", str(env)]
    if perfil:
        comando.extend(["--profile", perfil])
    return comando


def _correr(comando: list[str], entrada: bytes | None = None) -> None:
    resultado = subprocess.run(comando, cwd=RAIZ, input=entrada)
    if resultado.returncode != 0:
        raise SystemExit(resultado.returncode)


def _accion(permitidas: tuple[str, ...], defecto: str) -> str:
    valor = _variable("ACCION", defecto)
    if valor not in permitidas:
        raise SystemExit(f"ACCION no permitida: {valor}. Use {', '.join(permitidas)}.")
    return valor


def _archivo() -> str:
    nombre = os.environ.get("FILE", "").strip()
    if not nombre:
        raise SystemExit("Indique FILE=nombre.dump")
    if DUMP.fullmatch(nombre) is None:
        raise SystemExit(f"Valor no permitido: {nombre}")
    return nombre


def _exigir_desarrollo() -> str:
    base = _variable("DB_NAME", DESARROLLO)
    if base != DESARROLLO:
        raise SystemExit(f"Solo se permite sobre {DESARROLLO}")
    return base


def _confirmar(valor: str, mensaje: str) -> None:
    if os.environ.get("CONFIRM", "").strip() != valor:
        raise SystemExit(mensaje)


def _base() -> str:
    return _variable("DB_NAME", DESARROLLO)


def _bucket() -> str:
    return _variable("BUCKET", "ortesislab")


def _salud() -> None:
    comprobaciones = (
        _compose() + ["exec", "-T", "postgres", "pg_isready", "-d", _base()],
        _compose() + ["exec", "-T", "minio", "mc", "ready", "local"],
        _compose() + ["exec", "-T", "redis", "redis-cli", "ping"],
    )
    fallos = 0
    for comando in comprobaciones:
        if subprocess.run(comando, cwd=RAIZ).returncode != 0:
            fallos += 1
    if fallos:
        raise SystemExit(1)


def up() -> None:
    _correr(_compose() + ["config", "--quiet"])
    _correr(_compose() + ["up", "-d", "--wait", "postgres", "minio", "redis"])
    _correr(_compose("init") + ["run", "--rm", "minio-init"])
    _salud()


def down() -> None:
    accion = _accion(("parar", "retirar", "destruir"), "retirar")
    comando = _compose()
    if accion == "parar":
        _correr(comando + ["stop"])
        return
    if accion == "destruir":
        _confirmar("ELIMINAR", "Confirme con CONFIRM=ELIMINAR; borra los volumenes locales")
        _correr(comando + ["down", "--volumes", "--remove-orphans"])
        return
    _correr(comando + ["down", "--remove-orphans"])


def estado() -> None:
    accion = _accion(("salud", "logs", "consola"), "salud")
    if accion == "logs":
        _correr(_compose() + ["logs", "--tail", "200"])
        return
    if accion == "consola":
        _correr(_compose() + ["exec", "postgres", "psql", "-U", "ortesislab_migrator", "-d", _base()])
        return
    _salud()


def respaldo() -> None:
    accion = _accion(("crear", "restaurar"), "crear")
    nombre = _archivo()
    destino = BACKUPS / nombre
    if accion == "crear":
        if destino.exists():
            raise SystemExit(f"Ya existe apps/db/backups/{nombre}")
        _correr(_compose() + [
            "exec", "-T", "postgres", "pg_dump", "-Fc", "-U", "ortesislab_backup",
            "-d", _base(), "-n", "ortesislab", "-f", f"/backups/{nombre}",
        ])
        _correr(_compose() + [
            "run", "--rm", "mc", "mirror", "--overwrite", f"local/{_bucket()}", "/backups/objetos",
        ])
        return
    base = _exigir_desarrollo()
    _confirmar("RESTAURAR", f"Confirme con CONFIRM=RESTAURAR; reemplaza metadatos y objetos de {base}")
    if not destino.is_file():
        raise SystemExit(f"No existe apps/db/backups/{nombre}")
    if not (BACKUPS / "objetos").is_dir():
        raise SystemExit("No existe apps/db/backups/objetos; metadatos y objetos se restauran juntos")
    _correr(_compose() + ["exec", "-T", "postgres", "pg_restore", "--list", f"/backups/{nombre}"])
    _correr(_compose() + [
        "exec", "-T", "postgres", "pg_restore", "--clean", "--if-exists",
        "--single-transaction", "--exit-on-error", "-U", "ortesislab_migrator",
        "-d", base, f"/backups/{nombre}",
    ])
    _correr(_compose() + [
        "run", "--rm", "mc", "mirror", "--overwrite", "/backups/objetos", f"local/{_bucket()}",
    ])


def reset() -> None:
    base = _exigir_desarrollo()
    _confirmar("ELIMINAR", f"Confirme con CONFIRM=ELIMINAR; recrea {base} vacia")
    admin = _variable("DB_ADMIN", "ortesislab_admin")
    _correr(_compose() + ["exec", "-T", "postgres", "dropdb", "--if-exists", "--force", "-U", admin, base])
    _correr(_compose() + ["exec", "-T", "postgres", "createdb", "-U", admin, "-O", "ortesislab_migrator", base])
    _correr(
        _compose() + [
            "exec", "-T", "postgres", "psql", "-v", "ON_ERROR_STOP=1", "-q",
            "-v", f"base={base}", "-U", admin, "-d", base,
        ],
        entrada=PREPARAR.read_bytes(),
    )


def comprobar() -> None:
    assert DUMP.fullmatch("copia.dump")
    assert DUMP.fullmatch("../copia.dump") is None
    assert DUMP.fullmatch(".dump") is None
    os.environ.pop("CONFIRM", None)
    try:
        _confirmar("ELIMINAR", "falta confirmacion")
    except SystemExit:
        pass
    else:
        raise AssertionError("sin CONFIRM debe detenerse")
    os.environ["CONFIRM"] = "ELIMINAR"
    _confirmar("ELIMINAR", "falta confirmacion")
    os.environ["FILE"] = "../x.dump"
    try:
        _archivo()
    except SystemExit:
        pass
    else:
        raise AssertionError("un nombre de volcado invalido debe detenerse")
    os.environ.pop("FILE", None)
    os.environ.pop("CONFIRM", None)
    anterior = os.environ.get("ACCION")
    try:
        os.environ["ACCION"] = "destruir"
        assert _accion(("parar", "retirar", "destruir"), "retirar") == "destruir"
        os.environ["ACCION"] = ""
        assert _accion(("parar", "retirar", "destruir"), "retirar") == "retirar"
        os.environ["ACCION"] = "no"
        try:
            _accion(("parar",), "parar")
        except SystemExit:
            pass
        else:
            raise AssertionError("una ACCION desconocida debe detenerse")
    finally:
        if anterior is None:
            os.environ.pop("ACCION", None)
        else:
            os.environ["ACCION"] = anterior
    print("comprobacion ok")


COMANDOS = {"up": up, "down": down, "estado": estado, "respaldo": respaldo, "reset": reset, "--comprobar": comprobar}


def main(argv: list[str]) -> None:
    if len(argv) != 2 or argv[1] not in COMANDOS:
        raise SystemExit("Uso: BaseLocal.py up|down|estado|respaldo|reset|--comprobar")
    COMANDOS[argv[1]]()


if __name__ == "__main__":
    main(sys.argv)
