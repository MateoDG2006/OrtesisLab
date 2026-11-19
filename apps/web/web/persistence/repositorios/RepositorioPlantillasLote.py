"""Plantillas con nombre para armar lotes."""

from __future__ import annotations

import uuid
from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.dialects.postgresql import insert as insertar_pg
from sqlalchemy.exc import IntegrityError

from ..Contratos import AccesoDenegado, PlantillaLoteDTO
from .Consultas import AHORA, PLANTILLAS_LOTE
from .RepositorioBase import RepositorioBase


class RepositorioPlantillasLote(RepositorioBase):
    TABLA = PLANTILLAS_LOTE
    DTO = PlantillaLoteDTO

    @classmethod
    def Listar(cls, conexion, user_id: UUID) -> list[PlantillaLoteDTO]:
        return cls._Lista(
            conexion,
            select(PLANTILLAS_LOTE)
            .where(PLANTILLAS_LOTE.c.user_id == user_id)
            .order_by(PLANTILLAS_LOTE.c.updated_at.desc(), PLANTILLAS_LOTE.c.nombre),
        )

    @classmethod
    def Obtener(cls, conexion, user_id: UUID, plantilla_id: UUID) -> PlantillaLoteDTO:
        return cls._DelUsuario(conexion, user_id, PLANTILLAS_LOTE.c.id == plantilla_id)

    @classmethod
    def Guardar(cls, conexion, user_id: UUID, nombre: str, payload: dict, plantilla_id: UUID | None = None) -> PlantillaLoteDTO:
        nombre = nombre.strip()
        if not nombre or len(nombre) > 120:
            raise ValueError("El nombre debe tener entre 1 y 120 caracteres.")
        if not isinstance(payload, dict):
            raise ValueError("La plantilla no es válida.")
        try:
            if plantilla_id is None:
                plantilla_id = uuid.uuid4()
                conexion.execute(
                    insertar_pg(PLANTILLAS_LOTE).values(
                        id=plantilla_id,
                        user_id=user_id,
                        nombre=nombre,
                        payload=payload,
                    )
                )
                return cls.Obtener(conexion, user_id, plantilla_id)
            fila = cls._Opcional(
                conexion,
                update(PLANTILLAS_LOTE)
                .where(PLANTILLAS_LOTE.c.user_id == user_id, PLANTILLAS_LOTE.c.id == plantilla_id)
                .values(nombre=nombre, payload=payload, updated_at=AHORA)
                .returning(*PLANTILLAS_LOTE.c),
            )
            if fila is None:
                raise AccesoDenegado()
            return fila
        except IntegrityError as exc:
            raise ValueError("Ya existe una plantilla con ese nombre.") from exc

    @classmethod
    def Borrar(cls, conexion, user_id: UUID, plantilla_id: UUID) -> None:
        resultado = conexion.execute(
            delete(PLANTILLAS_LOTE).where(
                PLANTILLAS_LOTE.c.user_id == user_id,
                PLANTILLAS_LOTE.c.id == plantilla_id,
            )
        )
        if resultado.rowcount == 0:
            raise AccesoDenegado()
