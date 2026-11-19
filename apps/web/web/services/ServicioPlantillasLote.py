"""CRUD de plantillas de lote por usuario."""

from __future__ import annotations

from uuid import UUID

from web.persistence.ConexionPostgres import ConexionPostgres
from web.persistence.Contratos import PlantillaLoteDTO, UsuarioAutenticado
from web.persistence.repositorios import RepositorioPlantillasLote


class ServicioPlantillasLote:
    @staticmethod
    def Listar(usuario: UsuarioAutenticado) -> list[PlantillaLoteDTO]:
        return ConexionPostgres.Ejecutar(
            lambda conexion: RepositorioPlantillasLote.Listar(conexion, usuario.user_id)
        )

    @staticmethod
    def Obtener(usuario: UsuarioAutenticado, plantilla_id: UUID) -> PlantillaLoteDTO:
        return ConexionPostgres.Ejecutar(
            lambda conexion: RepositorioPlantillasLote.Obtener(conexion, usuario.user_id, plantilla_id)
        )

    @staticmethod
    def Guardar(
        usuario: UsuarioAutenticado,
        nombre: str,
        payload: dict,
        plantilla_id: UUID | None = None,
    ) -> PlantillaLoteDTO:
        return ConexionPostgres.Ejecutar(
            lambda conexion: RepositorioPlantillasLote.Guardar(
                conexion, usuario.user_id, nombre, payload, plantilla_id
            )
        )

    @staticmethod
    def Borrar(usuario: UsuarioAutenticado, plantilla_id: UUID) -> None:
        ConexionPostgres.Ejecutar(
            lambda conexion: RepositorioPlantillasLote.Borrar(conexion, usuario.user_id, plantilla_id)
        )
