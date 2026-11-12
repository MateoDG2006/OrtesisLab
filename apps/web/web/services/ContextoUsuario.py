"""Principal autenticado de cada operación.

La identidad sale de una sesión de servidor creada al registrarse o al entrar
con usuario y contraseña. El navegador solo guarda un token aleatorio en una
cookie HttpOnly; la base guarda su SHA-256. El token de sesión de Reflex no es
identidad.
"""

from __future__ import annotations

import hashlib
import secrets
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timedelta, timezone
from http.cookies import CookieError, SimpleCookie

from sqlalchemy.exc import IntegrityError

from web.ConfiguracionBackend import ConfiguracionBackend
from web.enums import EstadoUsuario
from web.persistence.ConexionPostgres import ConexionPostgres
from web.persistence.Contratos import SesionInvalida, UsuarioAutenticado
from web.persistence.repositorios import RepositorioPreferencias, RepositorioProyectos, RepositorioUsuarios

NOMBRE_COOKIE = "ortesislab_sesion"
DURACION_SESION = timedelta(hours=ConfiguracionBackend.Cargar("sesion")["duracion_horas"])

_actual: ContextVar[UsuarioAutenticado | None] = ContextVar("ortesislab_usuario", default=None)
_SCRYPT_N = 2**14
_SCRYPT_R = 8
_SCRYPT_P = 1


class CuentaYaExiste(Exception):
    """Ese usuario ya tiene una cuenta."""


class CredencialesInvalidas(Exception):
    """El usuario o la contraseña no coinciden."""


def NormalizarUsuario(valor: str) -> str:
    usuario = valor.strip().lower()
    if not usuario or len(usuario) > 120 or any(caracter.isspace() for caracter in usuario):
        raise ValueError("Escriba un usuario de 1 a 120 caracteres, sin espacios.")
    return usuario


def HashContrasena(plana: str) -> str:
    if len(plana) < 8 or len(plana) > 128:
        raise ValueError("La contraseña debe tener entre 8 y 128 caracteres.")
    sal = secrets.token_bytes(16)
    huella = hashlib.scrypt(plana.encode(), salt=sal, n=_SCRYPT_N, r=_SCRYPT_R, p=_SCRYPT_P, dklen=32)
    return f"scrypt${_SCRYPT_N}${_SCRYPT_R}${_SCRYPT_P}${sal.hex()}${huella.hex()}"


def VerificarContrasena(plana: str, guardada: str | None) -> bool:
    if not guardada:
        return False
    try:
        _algoritmo, n, r, p, sal, huella = guardada.split("$")
        calculada = hashlib.scrypt(
            plana.encode(), salt=bytes.fromhex(sal), n=int(n), r=int(r), p=int(p), dklen=32
        )
    except (TypeError, ValueError):
        return False
    return secrets.compare_digest(calculada.hex(), huella)


class ContextoUsuario:
    @staticmethod
    def Hash(token: str) -> str:
        return hashlib.sha256(token.encode("ascii")).hexdigest()

    @staticmethod
    def TokenDeCookie(cabecera: str) -> str:
        if not cabecera:
            return ""
        try:
            galleta = SimpleCookie()
            galleta.load(cabecera)
        except CookieError:
            return ""
        morsel = galleta.get(NOMBRE_COOKIE)
        return morsel.value if morsel is not None else ""

    @staticmethod
    def Requerir(cabecera_cookie: str) -> UsuarioAutenticado:
        """Entrada: cabecera Cookie. Proceso: resuelve la sesión vigente y el
        proyecto predeterminado. Salida: principal. Errores: SesionInvalida si
        falta, expiró, se revocó o la cuenta no está activa."""
        token = ContextoUsuario.TokenDeCookie(cabecera_cookie)
        if not token:
            raise SesionInvalida()
        huella = ContextoUsuario.Hash(token)

        def resolver(conexion) -> UsuarioAutenticado:
            fila = RepositorioUsuarios.ResolverSesion(conexion, huella)
            if fila is None:
                raise SesionInvalida("La sesión expiró. Vuelva a iniciar sesión.")
            proyecto = RepositorioProyectos.Predeterminado(conexion, fila["id"])
            return UsuarioAutenticado(fila["id"], fila["display_name"], None, proyecto)

        return ConexionPostgres.Ejecutar(resolver)

    @staticmethod
    def _AbrirSesion(conexion, user_id, token: str, expira: datetime) -> None:
        if RepositorioUsuarios.Estado(conexion, user_id) != EstadoUsuario.ACTIVE:
            raise SesionInvalida("La cuenta no está activa.")
        RepositorioPreferencias.Obtener(conexion, user_id)
        RepositorioProyectos.Predeterminado(conexion, user_id)
        RepositorioUsuarios.CrearSesion(conexion, user_id, ContextoUsuario.Hash(token), expira)

    @staticmethod
    def Registrar(usuario: str, password: str) -> tuple[str, datetime]:
        cuenta = NormalizarUsuario(usuario)
        huella = HashContrasena(password)
        token = secrets.token_urlsafe(32)
        expira = datetime.now(timezone.utc) + DURACION_SESION

        def crear(conexion) -> None:
            if RepositorioUsuarios.Buscar(conexion, cuenta) is not None:
                raise CuentaYaExiste()
            user_id = RepositorioUsuarios.Crear(conexion, cuenta, cuenta, huella)
            ContextoUsuario._AbrirSesion(conexion, user_id, token, expira)

        try:
            ConexionPostgres.Ejecutar(crear)
        except IntegrityError as exc:
            raise CuentaYaExiste() from exc
        return token, expira

    @staticmethod
    def Entrar(usuario: str, password: str) -> tuple[str, datetime]:
        cuenta = NormalizarUsuario(usuario)
        token = secrets.token_urlsafe(32)
        expira = datetime.now(timezone.utc) + DURACION_SESION

        def crear(conexion) -> None:
            fila = RepositorioUsuarios.Buscar(conexion, cuenta)
            if fila is None or not VerificarContrasena(password, fila["password_hash"]):
                raise CredencialesInvalidas()
            ContextoUsuario._AbrirSesion(conexion, fila["id"], token, expira)

        ConexionPostgres.Ejecutar(crear)
        return token, expira

    @staticmethod
    def CerrarSesion(cabecera_cookie: str) -> None:
        token = ContextoUsuario.TokenDeCookie(cabecera_cookie)
        if token:
            huella = ContextoUsuario.Hash(token)
            ConexionPostgres.Ejecutar(lambda conexion: RepositorioUsuarios.RevocarSesion(conexion, huella))

    @staticmethod
    @contextmanager
    def Activar(usuario: UsuarioAutenticado) -> Iterator[UsuarioAutenticado]:
        # Fija el principal para el código síncrono que corre en este contexto.
        marca = _actual.set(usuario)
        try:
            yield usuario
        finally:
            _actual.reset(marca)

    @staticmethod
    def Actual() -> UsuarioAutenticado:
        usuario = _actual.get()
        if usuario is None:
            raise SesionInvalida()
        return usuario
