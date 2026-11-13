"""Barra de sesión común a la comparación y al historial."""

from __future__ import annotations

import reflex as rx
from reflex_base.components.component import field
from reflex_base.vars.base import Var
from reflex_components_core.el.elements.base import BaseHTML


class _FormularioHtml(BaseHTML):
    """<form> que el navegador envía. rx.el.form cancela el submit."""

    tag = "form"
    action: Var[str] = field(default=None)
    method: Var[str] = field(default=None)


class Sesion:
    """Enlaces al registro y al login del backend, y navegación entre páginas."""

    @staticmethod
    def Ruta(ruta: str) -> str:
        # La cookie HttpOnly la fija el backend; el navegador va allí y vuelve a la página.
        return f"{rx.config.get_config().api_url.rstrip('/')}{ruta}"

    @staticmethod
    def Boton(texto: str, ruta: str, variante: str) -> rx.Component:
        # Reflex compila el ancla como Link del enrutador; sin reloadDocument mostraría su 404 para /auth.
        enlace = rx.el.a(texto, href=Sesion.Ruta(ruta), custom_attrs={"reloadDocument": True})
        return rx.button(enlace, as_child=True, size="1", variant=variante)

    @staticmethod
    def FormularioPost(texto: str, ruta: str, variante: str) -> rx.Component:
        return _FormularioHtml.create(
            rx.button(texto, type="submit", size="1", variant=variante),
            method="post",
            action=Sesion.Ruta(ruta),
        )

    @staticmethod
    def Barra(autenticado=None, nombre=None) -> rx.Component:
        from .EstadoApp import EstadoApp

        autenticado = EstadoApp.autenticado if autenticado is None else autenticado
        nombre = EstadoApp.usuario_nombre if nombre is None else nombre
        return rx.hstack(
            rx.link("Comparar", href="/", size="2"),
            rx.link("Lote", href="/lote", size="2"),
            rx.link("Historial", href="/historial", size="2"),
            rx.spacer(),
            rx.cond(
                autenticado,
                rx.hstack(
                    rx.text(nombre, size="2", color_scheme="gray"),
                    Sesion.FormularioPost("Cerrar sesión", "/auth/logout", "soft"),
                    spacing="3",
                    align="center",
                ),
                rx.hstack(
                    Sesion.Boton("Crear cuenta", "/auth/registro", "soft"),
                    Sesion.Boton("Iniciar sesión", "/auth/login", "solid"),
                    spacing="2",
                ),
            ),
            width="100%",
            align="center",
            padding_right="48px",
        )
