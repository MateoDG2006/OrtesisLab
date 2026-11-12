"""Rutas de registro e inicio de sesión: /auth/registro, /auth/login y /auth/logout.

Se montan con ``api_transformer``. La cuenta es un usuario y una contraseña
guardados en PostgreSQL.
"""

from __future__ import annotations

import asyncio
from html import escape
from urllib.parse import parse_qs

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, PlainTextResponse, RedirectResponse, Response
from starlette.routing import Mount, Route

from web.Ajustes import Ajustes
from web.persistence.Contratos import ErrorPersistencia, SesionInvalida

from .ContextoUsuario import DURACION_SESION, NOMBRE_COOKIE, ContextoUsuario, CredencialesInvalidas, CuentaYaExiste


def _Campos(cuerpo: bytes) -> dict[str, str]:
    datos = parse_qs(cuerpo.decode("utf-8", errors="replace"), keep_blank_values=True)
    return {clave: valores[0] for clave, valores in datos.items()}


def _Pagina(titulo: str, accion: str, error: str, enlace: str) -> HTMLResponse:
    aviso = f"<p>{escape(error)}</p>" if error else ""
    cuerpo = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{escape(titulo)}</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 4rem auto; max-width: 24rem; }}
label {{ display: block; margin-top: 1rem; }}
input {{ width: 100%; padding: .5rem; box-sizing: border-box; }}
button {{ margin-top: 1rem; }}
</style></head><body>
<h1>{escape(titulo)}</h1>
{aviso}
<form method="post" action="{escape(accion)}">
<label>Usuario <input name="usuario" autocomplete="username" required></label>
<label>Contraseña <input name="password" type="password" autocomplete="current-password" required></label>
<button type="submit">{escape(titulo)}</button>
</form>
<p>{enlace}</p>
</body></html>"""
    return HTMLResponse(cuerpo)


def _ConCookie(respuesta: Response, valor: str, ajustes: Ajustes) -> Response:
    respuesta.set_cookie(
        NOMBRE_COOKIE,
        valor,
        max_age=int(DURACION_SESION.total_seconds()),
        httponly=True,
        secure=ajustes.cookie_secure,
        samesite="lax",
        path="/",
    )
    return respuesta


class Autenticacion:
    @staticmethod
    def Aplicacion() -> Starlette:
        """Aplicación raíz que Reflex usa como transformador; monta /auth."""
        ajustes = Ajustes.Cargar()

        def login_pagina(error: str = "") -> HTMLResponse:
            return _Pagina(
                "Iniciar sesión",
                "/auth/login",
                error,
                '<a href="/auth/registro">Crear cuenta</a>',
            )

        def registro_pagina(error: str = "") -> HTMLResponse:
            return _Pagina(
                "Crear cuenta",
                "/auth/registro",
                error,
                '<a href="/auth/login">Ya tengo cuenta</a>',
            )

        async def login(request: Request) -> Response:
            if request.method == "GET":
                return login_pagina()
            campos = _Campos(await request.body())
            try:
                valor, _expira = await asyncio.to_thread(
                    ContextoUsuario.Entrar, campos.get("usuario", ""), campos.get("password", "")
                )
            except (CredencialesInvalidas, ValueError):
                return login_pagina("Usuario o contraseña incorrectos.")
            except SesionInvalida as exc:
                return login_pagina(str(exc))
            except ErrorPersistencia as exc:
                return PlainTextResponse(str(exc), status_code=503)
            return _ConCookie(RedirectResponse(ajustes.app_url, status_code=303), valor, ajustes)

        async def registro(request: Request) -> Response:
            if request.method == "GET":
                return registro_pagina()
            campos = _Campos(await request.body())
            try:
                valor, _expira = await asyncio.to_thread(
                    ContextoUsuario.Registrar, campos.get("usuario", ""), campos.get("password", "")
                )
            except CuentaYaExiste:
                return registro_pagina("Ese usuario ya existe.")
            except ValueError as exc:
                return registro_pagina(str(exc))
            except SesionInvalida as exc:
                return registro_pagina(str(exc))
            except ErrorPersistencia as exc:
                return PlainTextResponse(str(exc), status_code=503)
            return _ConCookie(RedirectResponse(ajustes.app_url, status_code=303), valor, ajustes)

        async def logout(request: Request) -> Response:
            try:
                await asyncio.to_thread(ContextoUsuario.CerrarSesion, request.headers.get("cookie", ""))
            except ErrorPersistencia:
                pass
            respuesta = RedirectResponse(ajustes.app_url, status_code=303)
            respuesta.delete_cookie(
                NOMBRE_COOKIE, path="/", httponly=True, secure=ajustes.cookie_secure, samesite="lax"
            )
            return respuesta

        async def logout_get(_request: Request) -> Response:
            return PlainTextResponse("Cierre de sesión solo por POST.", status_code=405)

        rutas = Starlette(
            routes=[
                Route("/login", login, methods=["GET", "POST"]),
                Route("/registro", registro, methods=["GET", "POST"]),
                Route("/logout", logout, methods=["POST"]),
                Route("/logout", logout_get, methods=["GET"]),
            ]
        )
        return Starlette(routes=[Mount("/auth", app=rutas)])
