"""Pantalla /lote: progreso de un lote con una miniatura por variante.

``/lote?id=<uuid>`` abre ese lote; sin id, el último del usuario. Comparte
``EstadoApp`` con la página principal, que es quien lo encola.
"""

from __future__ import annotations

import reflex as rx

from .EstadoApp import ESTADOS_VISIBLES, EstadoApp
from .PaginaComparacion import PaginaComparacion
from .Sesion import Sesion

COLORES_ESTADO = {
    "queued": "gray",
    "running": "blue",
    "succeeded": "grass",
    "failed": "red",
    "cancelled": "orange",
}


class PaginaLote:
    """Cabecera con el avance, comparación 3D y cuadrícula de miniaturas."""

    @staticmethod
    def Index() -> rx.Component:
        return rx.box(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                Sesion.Barra(),
                rx.heading("Progreso del lote", size="8"),
                PaginaLote.Cabecera(),
                PaginaLote.Comparacion(),
                rx.grid(
                    rx.foreach(EstadoApp.resultados, PaginaLote.Tarjeta),
                    columns={"initial": "1", "sm": "2", "md": "3", "lg": "4"},
                    spacing="4",
                    width="100%",
                ),
                spacing="5",
                width="100%",
            ),
            padding="6",
            max_width="1400px",
            margin="0 auto",
        )

    @staticmethod
    def Cabecera() -> rx.Component:
        return rx.card(
            rx.vstack(
                rx.hstack(
                    rx.text(EstadoApp.mensaje, size="3", weight="medium"),
                    rx.spacer(),
                    rx.cond(
                        EstadoApp.ocupado,
                        rx.button(
                            "Cancelar lote",
                            on_click=EstadoApp.CancelarLote,
                            color_scheme="red",
                            variant="soft",
                            size="2",
                        ),
                        rx.box(),
                    ),
                    rx.button(rx.link("Nuevo lote", href="/"), as_child=True, size="2", variant="outline"),
                    width="100%",
                    align="center",
                    wrap="wrap",
                    spacing="3",
                ),
                rx.cond(
                    EstadoApp.total > 0,
                    rx.vstack(
                        rx.progress(value=EstadoApp.porcentaje, width="100%"),
                        rx.hstack(
                            rx.text(EstadoApp.hechos, " de ", EstadoApp.total, " terminadas", size="2"),
                            rx.text(EstadoApp.resumen_estados, size="2", color_scheme="gray"),
                            spacing="4",
                            wrap="wrap",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.box(),
                ),
                spacing="3",
                width="100%",
            ),
            width="100%",
        )

    @staticmethod
    def Comparacion() -> rx.Component:
        return rx.cond(
            EstadoApp.vistas.length() > 0,
            rx.card(
                rx.vstack(
                    rx.heading("Comparación 3D", size="4"),
                    rx.text(
                        "Arrastre para girar y use la rueda para acercar. Hasta tres a la vez.",
                        size="1",
                        color_scheme="gray",
                    ),
                    rx.hstack(
                        rx.foreach(EstadoApp.vistas, PaginaComparacion.Marco),
                        align="start",
                        width="100%",
                        spacing="4",
                        wrap="wrap",
                    ),
                    spacing="3",
                    width="100%",
                ),
                width="100%",
            ),
            rx.box(),
        )

    @staticmethod
    def Tarjeta(ficha) -> rx.Component:
        elegida = EstadoApp.vistas.contains(ficha["archivo"])
        return rx.card(
            rx.vstack(
                rx.box(
                    rx.cond(
                        ficha["archivo"] != "",
                        PaginaComparacion.Visor(ficha["archivo"], "200px", miniatura=True),
                        rx.center(
                            rx.cond(
                                ficha["error"] != "",
                                rx.vstack(
                                    rx.icon("triangle-alert", color="var(--red-9)"),
                                    rx.text(ficha["error"], size="1", color_scheme="red", align="center"),
                                    align="center",
                                    spacing="2",
                                ),
                                rx.cond(
                                    ficha["estado"] == "running",
                                    rx.vstack(rx.spinner(size="3"), rx.text("Construyendo…", size="1"), align="center"),
                                    rx.vstack(
                                        rx.icon("clock", color="var(--gray-9)"),
                                        rx.text("En cola", size="1", color_scheme="gray"),
                                        align="center",
                                    ),
                                ),
                            ),
                            height="200px",
                            padding="3",
                        ),
                    ),
                    background="var(--gray-3)",
                    border_radius="12px",
                    width="100%",
                    overflow="hidden",
                ),
                rx.hstack(
                    rx.text(ficha["patron"], size="3", weight="bold"),
                    rx.spacer(),
                    rx.match(
                        ficha["estado"],
                        *[
                            (codigo, rx.badge(texto, color_scheme=COLORES_ESTADO.get(codigo, "gray")))
                            for codigo, texto in ESTADOS_VISIBLES.items()
                        ],
                        rx.box(),
                    ),
                    width="100%",
                    align="center",
                ),
                rx.text(ficha["detalle"], size="1", color_scheme="gray"),
                rx.cond(
                    ficha["volumen"] != "",
                    rx.hstack(
                        PaginaComparacion.Medida("Volumen", ficha["volumen"]),
                        PaginaComparacion.Medida("Peso", ficha["peso"]),
                        PaginaComparacion.Medida("Precio", ficha["precio"]),
                        spacing="3",
                        wrap="wrap",
                    ),
                    rx.box(),
                ),
                rx.hstack(
                    rx.button(
                        rx.cond(elegida, "Quitar de 3D", "Ver en 3D"),
                        size="1",
                        variant=rx.cond(elegida, "solid", "soft"),
                        on_click=EstadoApp.Comparar(ficha["id"]),
                        disabled=ficha["archivo"] == "",
                    ),
                    rx.button(
                        rx.icon("download", size=14),
                        "STL",
                        size="1",
                        variant="outline",
                        on_click=EstadoApp.Descargar(ficha["id"]),
                        disabled=ficha["archivo"] == "",
                    ),
                    spacing="2",
                ),
                spacing="2",
                width="100%",
            ),
            width="100%",
        )
