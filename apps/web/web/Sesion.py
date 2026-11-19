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
    def Salir() -> rx.Component:
        return _FormularioHtml.create(
            rx.icon_button(
                rx.icon("log-out", size=18),
                type="submit",
                size="3",
                variant="outline",
                color_scheme="gray",
                aria_label="Cerrar sesión",
                title="Cerrar sesión",
            ),
            method="post",
            action=Sesion.Ruta("/auth/logout"),
        )

    @staticmethod
    def Barra(activa: str, autenticado=None, nombre=None) -> rx.Component:
        from .EstadoApp import EstadoApp

        autenticado = EstadoApp.autenticado if autenticado is None else autenticado
        nombre = EstadoApp.usuario_nombre if nombre is None else nombre
        secciones = (("/", "Diseño"), ("/lote", "Lotes"), ("/historial", "Historial"))
        return rx.el.header(
            rx.el.div(
                rx.link("OrtesisLab", href="/", class_name="ol-brand", aria_label="OrtesisLab · inicio"),
                rx.el.nav(
                    *[
                        rx.link(
                            texto,
                            href=ruta,
                            custom_attrs={"aria-current": "page"} if ruta == activa else {},
                        )
                        for ruta, texto in secciones
                    ],
                    class_name="ol-nav",
                    aria_label="Secciones",
                ),
                rx.hstack(
                    rx.icon_button(
                        rx.color_mode_cond(rx.icon("moon", size=18), rx.icon("sun", size=18)),
                        on_click=rx.toggle_color_mode,
                        size="3",
                        variant="outline",
                        color_scheme="gray",
                        aria_label="Cambiar entre modo claro y oscuro",
                    ),
                    rx.cond(
                        autenticado,
                        rx.hstack(
                            rx.box(
                                rx.avatar(
                                    fallback=nombre.to(str)[:2].upper(),
                                    size="2",
                                    radius="full",
                                    variant="solid",
                                ),
                                rx.text(nombre, size="2", weight="medium"),
                                class_name="ol-chip",
                            ),
                            Sesion.Salir(),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            Sesion.Boton("Crear cuenta", "/auth/registro", "soft"),
                            Sesion.Boton("Iniciar sesión", "/auth/login", "solid"),
                            spacing="2",
                        ),
                    ),
                    spacing="2",
                    align="center",
                ),
                class_name="ol-navbar-inner",
            ),
            class_name="ol-navbar",
            role="banner",
        )
