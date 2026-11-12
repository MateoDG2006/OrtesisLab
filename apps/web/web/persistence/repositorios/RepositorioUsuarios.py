"""Cuentas locales y sus sesiones de servidor."""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta
from uuid import UUID

from sqlalchemy import and_, delete, insert, or_, select, update

from web.enums import EstadoUsuario

from .Consultas import AHORA, SESIONES, USUARIOS
from .RepositorioBase import RepositorioBase


class RepositorioUsuarios(RepositorioBase):
    TABLA = USUARIOS

    @classmethod
    def Buscar(cls, conexion, usuario: str) -> dict | None:
        return cls._Uno(
            conexion,
            select(
                USUARIOS.c.id,
                USUARIOS.c.password_hash,
                USUARIOS.c.status,
                USUARIOS.c.display_name,
            ).where(USUARIOS.c.username == usuario),
        )

    @staticmethod
    def Crear(conexion, usuario: str, nombre: str, password_hash: str) -> UUID:
        user_id = uuid.uuid4()
        conexion.execute(
            insert(USUARIOS).values(
                id=user_id,
                username=usuario,
                password_hash=password_hash,
                display_name=nombre[:120] or usuario[:120],
            )
        )
        return user_id

    @classmethod
    def Asegurar(cls, conexion, usuario: str, nombre: str, password_hash: str) -> UUID:
        fila = cls.Buscar(conexion, usuario)
        if fila is not None:
            return fila["id"]
        return cls.Crear(conexion, usuario, nombre, password_hash)

    @staticmethod
    def Estado(conexion, user_id: UUID) -> str | None:
        return conexion.execute(select(USUARIOS.c.status).where(USUARIOS.c.id == user_id)).scalar_one_or_none()

    @staticmethod
    def CrearSesion(conexion, user_id: UUID, token_sha256: str, expira: datetime) -> None:
        conexion.execute(
            insert(SESIONES).values(id=uuid.uuid4(), user_id=user_id, token_sha256=token_sha256, expires_at=expira)
        )

    @classmethod
    def ResolverSesion(cls, conexion, token_sha256: str) -> dict | None:
        return cls._Uno(
            conexion,
            select(USUARIOS.c.id, USUARIOS.c.display_name, USUARIOS.c.username)
            .select_from(SESIONES.join(USUARIOS, USUARIOS.c.id == SESIONES.c.user_id))
            .where(
                SESIONES.c.token_sha256 == token_sha256,
                SESIONES.c.revoked_at.is_(None),
                SESIONES.c.expires_at > AHORA,
                USUARIOS.c.status == EstadoUsuario.ACTIVE,
            ),
        )

    @staticmethod
    def PurgarSesionesVencidas(conexion, dias: int) -> int:
        limite = AHORA - timedelta(days=max(1, dias))
        resultado = conexion.execute(
            delete(SESIONES).where(
                or_(
                    SESIONES.c.expires_at < limite,
                    and_(SESIONES.c.revoked_at.is_not(None), SESIONES.c.revoked_at < limite),
                )
            )
        )
        return int(resultado.rowcount)

    @staticmethod
    def RevocarSesion(conexion, token_sha256: str) -> None:
        conexion.execute(
            update(SESIONES)
            .where(SESIONES.c.token_sha256 == token_sha256, SESIONES.c.revoked_at.is_(None))
            .values(revoked_at=AHORA)
        )
