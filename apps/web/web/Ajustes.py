"""Variables de entorno de OrtesisLab: el único lugar que las declara y las lee.

``Cargar`` lee el ``.env`` de la raíz con python-dotenv (UTF-8, con o sin BOM)
sin pisar variables que el proceso ya tenga. Una variable sin
valor por defecto es obligatoria: leerla sin definirla lanza ``RuntimeError``.
Una variable con prefijo exigido lanza ``RuntimeError`` si no empieza por él.
Ningún valor se envía al navegador.
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

# .env de la raíz del monorepo: apps/web/web/Ajustes.py sube cuatro niveles.
RAIZ = Path(__file__).resolve().parents[3]


class Variable:
    """Una clave del entorno; sin ``defecto`` es obligatoria y no admite vacío."""

    def __init__(self, clave: str, defecto: str | None = None, prefijo: str = ""):
        self.clave = clave
        self.defecto = defecto
        self.prefijo = prefijo

    def __get__(self, ajustes: Ajustes, _tipo: type) -> str:
        valor = ajustes.valores.get(self.clave) or self.defecto
        if valor is None:
            raise RuntimeError(f"Falta la variable de entorno {self.clave}.")
        if not valor.startswith(self.prefijo):
            raise RuntimeError(f"La variable de entorno {self.clave} debe empezar por {self.prefijo}")
        return valor


# SQLAlchemy necesita el driver en la URL.
POSTGRES = "postgresql+psycopg://"


class Ajustes:
    # PostgreSQL: la web, el trabajador y Alembic usan roles distintos.
    database_url = Variable("ORTESISLAB_DATABASE_URL", prefijo=POSTGRES)
    worker_database_url = Variable("ORTESISLAB_WORKER_DATABASE_URL", prefijo=POSTGRES)
    migrator_database_url = Variable("ORTESISLAB_MIGRATOR_DATABASE_URL", prefijo=POSTGRES)
    test_database_url = Variable("ORTESISLAB_TEST_DATABASE_URL", prefijo=POSTGRES)
    test_worker_database_url = Variable("ORTESISLAB_TEST_WORKER_DATABASE_URL", prefijo=POSTGRES)
    test_migrator_database_url = Variable("ORTESISLAB_TEST_MIGRATOR_DATABASE_URL", prefijo=POSTGRES)

    # Bucket S3; sin URL pública, el navegador usa el endpoint.
    s3_endpoint = Variable("ORTESISLAB_S3_ENDPOINT")
    s3_public_url = Variable("ORTESISLAB_S3_PUBLIC_URL", "")
    s3_access_key = Variable("ORTESISLAB_S3_ACCESS_KEY")
    s3_secret_key = Variable("ORTESISLAB_S3_SECRET_KEY")
    s3_bucket = Variable("ORTESISLAB_S3_BUCKET", "ortesislab")
    s3_region = Variable("ORTESISLAB_S3_REGION", "us-east-1")

    # Vacía: la generación funciona sin caché.
    redis_url = Variable("ORTESISLAB_REDIS_URL", "")

    app_url = Variable("ORTESISLAB_APP_URL", "http://localhost:3000")
    _cookie_secure = Variable("ORTESISLAB_COOKIE_SECURE", "false")

    def __init__(self, valores: dict[str, str]):
        self.valores = valores

    @property
    def cookie_secure(self) -> bool:
        return self._cookie_secure.lower() == "true"

    @staticmethod
    @lru_cache(maxsize=1)
    def Cargar() -> Ajustes:
        load_dotenv(RAIZ / ".env", override=False, encoding="utf-8-sig")
        return Ajustes(dict(os.environ))
