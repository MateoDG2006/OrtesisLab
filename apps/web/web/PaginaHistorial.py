"""Pantalla /historial: generaciones del usuario, comparación y restauración."""

from __future__ import annotations

import reflex as rx

from .EstadoHistorial import ESTADOS_VISIBLES, TODOS, EstadoHistorial
from .GeneradorWeb import PATRONES
from .PaginaComparacion import PaginaComparacion


class PaginaHistorial:
    """Filtros, tabla paginada por cursor y visores de las versiones elegidas."""

    @staticmethod
    def Index() -> rx.Component:
        return PaginaComparacion.Pagina(
            "/historial",
            PaginaHistorial.Filtros(),
            rx.cond(EstadoHistorial.mensaje != "", rx.callout(EstadoHistorial.mensaje, size="1"), rx.fragment()),
            PaginaHistorial.Tabla(),
            PaginaHistorial.Comparacion(),
            autenticado=EstadoHistorial.autenticado,
            nombre=EstadoHistorial.usuario_nombre,
        )

    @staticmethod
    def Filtros() -> rx.Component:
        return rx.box(
            rx.hstack(
                rx.box(
                    PaginaComparacion.Selector(
                        "Patrón",
                        EstadoHistorial.filtro_patron,
                        EstadoHistorial.set_filtro_patron,
                        [(TODOS, "Todos"), *PATRONES.items()],
                    ),
                    flex="1 1 180px",
                ),
                rx.box(
                    PaginaComparacion.Selector(
                        "Estado",
                        EstadoHistorial.filtro_estado,
                        EstadoHistorial.set_filtro_estado,
                        [(TODOS, "Todos"), *ESTADOS_VISIBLES.items()],
                    ),
                    flex="1 1 160px",
                ),
                PaginaHistorial.Fecha("Desde", EstadoHistorial.filtro_desde, EstadoHistorial.set_filtro_desde),
                PaginaHistorial.Fecha("Hasta", EstadoHistorial.filtro_hasta, EstadoHistorial.set_filtro_hasta),
                rx.button(
                    rx.icon("filter", size=16),
                    "Filtrar",
                    on_click=EstadoHistorial.Cargar,
                    loading=EstadoHistorial.cargando,
                    radius="full",
                    size="3",
                ),
                align="end",
                spacing="4",
                wrap="wrap",
                width="100%",
            ),
            class_name="ol-card",
            width="100%",
        )

    @staticmethod
    def Fecha(etiqueta: str, valor, cambio) -> rx.Component:
        return rx.vstack(
            rx.text(etiqueta, class_name="ol-lbl"),
            rx.input(value=valor, on_change=cambio, type="date", size="3", aria_label=etiqueta, width="100%"),
            spacing="1",
            flex="1 1 160px",
        )

    @staticmethod
    def Tabla() -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.box(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Versión"),
                                rx.table.column_header_cell("Fecha"),
                                rx.table.column_header_cell("Patrón"),
                                rx.table.column_header_cell("Parámetros"),
                                rx.table.column_header_cell("Estado"),
                                rx.table.column_header_cell("Volumen"),
                                rx.table.column_header_cell("Peso"),
                                rx.table.column_header_cell("Precio"),
                                rx.table.column_header_cell(""),
                            ),
                        ),
                        rx.table.body(rx.foreach(EstadoHistorial.filas, PaginaHistorial.Fila)),
                        width="100%",
                        min_width="960px",
                        class_name="ol-tabla",
                    ),
                    overflow_x="auto",
                    width="100%",
                ),
                rx.flex(
                    rx.text("Restaurar crea una versión nueva; la original no cambia.", size="2", class_name="ol-muted"),
                    rx.hstack(
                        rx.button(
                            "Anterior",
                            size="2",
                            radius="full",
                            variant="outline",
                            color_scheme="gray",
                            on_click=EstadoHistorial.Anterior,
                            disabled=EstadoHistorial.pagina <= 1,
                        ),
                        rx.text("Página ", EstadoHistorial.pagina, size="2", weight="medium"),
                        rx.button(
                            "Siguiente",
                            size="2",
                            radius="full",
                            variant="outline",
                            color_scheme="gray",
                            on_click=EstadoHistorial.Siguiente,
                            disabled=~EstadoHistorial.hay_siguiente,
                        ),
                        align="center",
                        spacing="3",
                    ),
                    justify="between",
                    align="center",
                    wrap="wrap",
                    gap="12px",
                    padding="14px 18px",
                    width="100%",
                ),
                spacing="0",
                width="100%",
            ),
            class_name="ol-card",
            padding="0",
            overflow="hidden",
            width="100%",
        )

    @staticmethod
    def Fila(fila) -> rx.Component:
        elegida = EstadoHistorial.seleccion.contains(fila["version_id"])
        return rx.table.row(
            rx.table.cell(rx.text(fila["version"], weight="bold")),
            rx.table.cell(rx.text(fila["fecha"], class_name="ol-muted", white_space="nowrap")),
            rx.table.cell(rx.text(fila["patron"], weight="medium")),
            rx.table.cell(
                rx.vstack(
                    rx.text(fila["detalle"], size="1", class_name="ol-muted"),
                    rx.text(fila["aviso"], size="1", color="var(--ol-coral)"),
                )
            ),
            rx.table.cell(rx.el.span(fila["estado"], class_name="ol-badge ol-b-" + fila["estado_codigo"])),
            rx.table.cell(fila["volumen"]),
            rx.table.cell(fila["peso"]),
            rx.table.cell(fila["precio"]),
            rx.table.cell(
                rx.hstack(
                    rx.button(
                        rx.cond(elegida, "Quitar", "Comparar"),
                        size="2",
                        radius="full",
                        variant=rx.cond(elegida, "solid", "outline"),
                        color_scheme=rx.cond(elegida, "teal", "gray"),
                        aria_pressed=elegida,
                        on_click=EstadoHistorial.Seleccionar(fila["version_id"]),
                    ),
                    PaginaHistorial.Accion(
                        "rotate-ccw", "Restaurar como versión nueva", EstadoHistorial.Restaurar(fila["version_id"])
                    ),
                    PaginaHistorial.Accion("rotate-cw", "Reintentar", EstadoHistorial.Reintentar(fila["version_id"])),
                    PaginaHistorial.Accion(
                        "download", "Descargar STL", EstadoHistorial.Descargar(fila["item_id"]), fila["url"] == ""
                    ),
                    spacing="2",
                    justify="end",
                )
            ),
        )

    @staticmethod
    def Comparacion() -> rx.Component:
        return rx.cond(
            EstadoHistorial.comparacion.length() > 0,
            rx.el.section(
                rx.heading("Comparación de versiones", size="5", weight="medium", margin_bottom="14px"),
                rx.grid(
                    rx.foreach(EstadoHistorial.comparacion, PaginaHistorial.Tarjeta),
                    columns="repeat(auto-fit, minmax(280px, 1fr))",
                    spacing="4",
                    width="100%",
                ),
                aria_label="Comparación de versiones",
                style={"width": "100%"},
            ),
            rx.fragment(),
        )

    @staticmethod
    def Tarjeta(tarjeta) -> rx.Component:
        return rx.el.article(
            rx.vstack(
                rx.heading(tarjeta["titulo"], size="4", weight="bold"),
                rx.cond(
                    tarjeta["url"] != "",
                    PaginaComparacion.Visor(tarjeta["url"], "220px"),
                    rx.center(
                        rx.text("Sin STL disponible.", size="2", class_name="ol-muted"),
                        min_height="120px",
                        width="100%",
                        background="var(--ol-stage)",
                        border_radius="16px",
                    ),
                ),
                rx.text(tarjeta["detalle"], size="2", weight="medium"),
                rx.text(tarjeta["cambios"], size="1", class_name="ol-muted"),
                rx.grid(
                    PaginaComparacion.Medida("Volumen", tarjeta["volumen"]),
                    PaginaComparacion.Medida("Peso", tarjeta["peso"]),
                    PaginaComparacion.Medida("Precio", tarjeta["precio"]),
                    columns="3",
                    spacing="2",
                    width="100%",
                    border_top="1px solid var(--ol-line)",
                    padding_top="10px",
                ),
                rx.text(tarjeta["intentos"], " · ", tarjeta["nota"], size="1", class_name="ol-muted"),
                spacing="3",
                width="100%",
            ),
            class_name="ol-card",
        )

    @staticmethod
    def Accion(icono: str, etiqueta: str, al_pulsar, deshabilitado=False) -> rx.Component:
        return rx.tooltip(
            rx.icon_button(
                rx.icon(icono, size=16),
                size="2",
                variant="outline",
                color_scheme="gray",
                aria_label=etiqueta,
                on_click=al_pulsar,
                disabled=deshabilitado,
            ),
            content=etiqueta,
        )
