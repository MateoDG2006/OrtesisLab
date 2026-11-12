"""Lectura de preferencias por usuario."""

from __future__ import annotations

from web.persistence.ConexionPostgres import ConexionPostgres
from web.persistence.Contratos import Preferencias, UsuarioAutenticado
from web.persistence.repositorios import RepositorioPreferencias


class ServicioPreferencias:
    @staticmethod
    def Obtener(usuario: UsuarioAutenticado) -> Preferencias:
        return ConexionPostgres.Ejecutar(lambda conexion: RepositorioPreferencias.Obtener(conexion, usuario.user_id))
