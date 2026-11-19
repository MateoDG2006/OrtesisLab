"""Pantalla /lote: creación de un lote y su progreso con una miniatura por variante.

``/lote?id=<uuid>`` abre ese lote; sin id, el último del usuario. Comparte
``EstadoApp`` con Diseño: el lote parte de sus parámetros.
"""

from __future__ import annotations

import reflex as rx

from .EstadoApp import CASILLAS_PATRON, ESTADOS_VISIBLES, EstadoApp
from .GeneradorWeb import EJES
from .PaginaComparacion import AYUDAS, PaginaComparacion
from .persistence.Contratos import MAXIMO_LOTES_PENDIENTES


class PaginaLote:
    """Formulario «Nuevo lote», avance, comparación 3D y cuadrícula de miniaturas."""

    @staticmethod
    def Index() -> rx.Component:
        return PaginaComparacion.Pagina(
            "/lote",
            "Lotes",
            rx.flex(
                PaginaLote.NuevoLote(),
                rx.vstack(
                    PaginaLote.Cabecera(),
                    PaginaLote.Comparacion(),
                    rx.cond(
                        EstadoApp.resultados.length() > 0,
                        rx.grid(
                            rx.foreach(EstadoApp.resultados, PaginaLote.Tarjeta),
                            columns="repeat(auto-fill, minmax(240px, 1fr))",
                            spacing="4",
                            width="100%",
                        ),
                        rx.box(
                            rx.text("No hay variantes en este lote.", size="3", weight="bold"),
                            rx.text(
                                "Elija patrones y características en Nuevo lote, o abra un lote desde Historial.",
                                size="2",
                                class_name="ol-muted",
                            ),
                            class_name="ol-empty",
                        ),
                    ),
                    spacing="5",
                    flex="999 1 640px",
                    min_width="0",
                ),
                wrap="wrap",
                gap="20px",
                width="100%",
                align="start",
            ),
        )

    @staticmethod
    def NuevoLote() -> rx.Component:
        return rx.el.aside(
            rx.vstack(
                rx.vstack(
                    rx.heading("Nuevo lote", size="5", weight="medium"),
                    rx.text(
                        "Parte de los parámetros de Diseño. Elija patrones y tantas características "
                        "numéricas como quiera; se combinan entre sí.",
                        size="2",
                        class_name="ol-muted",
                    ),
                    spacing="1",
                ),
                rx.box(
                    rx.text("1. Patrones", class_name="ol-lbl"),
                    rx.grid(
                        *[
                            PaginaComparacion.Mosaico(
                                codigo,
                                getattr(EstadoApp, campo),
                                getattr(EstadoApp, f"set_{campo}")(~getattr(EstadoApp, campo)),
                                "pressed",
                            )
                            for codigo, campo in CASILLAS_PATRON
                        ],
                        role="group",
                        aria_label="Patrones",
                        columns="3",
                        spacing="2",
                        margin_top="6px",
                    ),
                    width="100%",
                ),
                rx.vstack(
                    rx.text("2. Características que varían", class_name="ol-lbl"),
                    rx.text(
                        "Cada fila barre un parámetro. Varias filas se multiplican (producto cartesiano).",
                        size="1",
                        class_name="ol-muted",
                    ),
                    rx.foreach(EstadoApp.barridos, PaginaLote.FilaBarrido),
                    rx.button(
                        rx.icon("plus", size=16),
                        "Añadir característica",
                        on_click=EstadoApp.AnadirBarrido,
                        disabled=EstadoApp.barridos.length() >= len(EJES),
                        variant="outline",
                        color_scheme="gray",
                        radius="full",
                        size="2",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                    class_name="ol-sub",
                ),
                rx.flex(
                    rx.vstack(
                        rx.text("3. Con y sin capa interior", size="2", weight="medium"),
                        rx.text("Duplica cada variante con patrón", size="1", class_name="ol-muted"),
                        spacing="1",
                    ),
                    rx.switch(
                        checked=EstadoApp.ambos_revestimientos,
                        on_change=EstadoApp.set_ambos_revestimientos,
                        aria_label="Con y sin capa interior",
                        size="3",
                    ),
                    justify="between",
                    align="center",
                    gap="12px",
                    width="100%",
                    class_name="ol-sub",
                ),
                rx.callout(
                    EstadoApp.resumen_lote,
                    icon=rx.cond(EstadoApp.lote_valido, "layers", "triangle-alert"),
                    color_scheme=rx.cond(EstadoApp.lote_valido, "teal", "red"),
                    size="1",
                    width="100%",
                ),
                rx.button(
                    "Generar lote",
                    on_click=EstadoApp.PedirLote,
                    loading=EstadoApp.ocupado,
                    disabled=EstadoApp.ocupado | ~EstadoApp.lote_valido,
                    radius="full",
                    size="3",
                    width="100%",
                ),
                rx.text(
                    "El lote queda en cola: puede salir; el trabajador construye solo.",
                    size="1",
                    class_name="ol-muted",
                ),
                rx.vstack(
                    rx.text("Plantillas guardadas", class_name="ol-lbl"),
                    rx.hstack(
                        rx.input(
                            placeholder="Nombre de la plantilla",
                            value=EstadoApp.plantilla_nombre,
                            on_change=EstadoApp.set_plantilla_nombre,
                            width="100%",
                            size="2",
                            aria_label="Nombre de la plantilla",
                        ),
                        rx.button(
                            "Guardar",
                            on_click=EstadoApp.GuardarPlantilla,
                            disabled=EstadoApp.ocupado | ~EstadoApp.lote_valido,
                            radius="full",
                            size="2",
                            variant="outline",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.foreach(EstadoApp.plantillas, PaginaLote.FilaPlantilla),
                    rx.button(
                        "Generar plantillas marcadas",
                        on_click=EstadoApp.PedirPlantillasSeleccionadas,
                        loading=EstadoApp.ocupado,
                        disabled=EstadoApp.ocupado | (EstadoApp.plantillas_marcadas.length() == 0),
                        radius="full",
                        size="2",
                        width="100%",
                        variant="soft",
                    ),
                    rx.text(
                        f"Hasta {MAXIMO_LOTES_PENDIENTES} lotes en espera a la vez; el resto se omite hasta que haya hueco.",
                        size="1",
                        class_name="ol-muted",
                    ),
                    spacing="2",
                    width="100%",
                    class_name="ol-sub",
                ),
                spacing="4",
                width="100%",
            ),
            aria_label="Nuevo lote",
            class_name="ol-card",
            style={"flex": "1 1 340px", "max_width": "400px"},
        )

    @staticmethod
    def FilaPlantilla(fila) -> rx.Component:
        return rx.hstack(
            rx.checkbox(
                checked=EstadoApp.plantillas_marcadas.contains(fila["id"]),
                on_change=EstadoApp.MarcarPlantilla(fila["id"]),
                aria_label="Marcar plantilla",
            ),
            rx.text(fila["nombre"], size="2", weight="medium", flex="1"),
            rx.icon_button(
                rx.icon("folder-open", size=14),
                on_click=EstadoApp.CargarPlantilla(fila["id"]),
                variant="ghost",
                size="1",
                aria_label="Cargar plantilla",
            ),
            rx.icon_button(
                rx.icon("trash-2", size=14),
                on_click=EstadoApp.BorrarPlantilla(fila["id"]),
                variant="ghost",
                color_scheme="gray",
                size="1",
                aria_label="Borrar plantilla",
            ),
            spacing="2",
            width="100%",
            align="center",
        )

    @staticmethod
    def FilaBarrido(fila) -> rx.Component:
        return rx.vstack(
            rx.hstack(
                rx.select.root(
                    rx.select.trigger(width="100%", aria_label="Parámetro que varía"),
                    rx.select.content(
                        *[rx.select.item(texto, value=codigo) for codigo, texto in EJES.items()],
                    ),
                    value=fila["clave"],
                    on_change=EstadoApp.set_barrido_clave(fila["id"]),
                    size="3",
                ),
                rx.icon_button(
                    rx.icon("trash-2", size=16),
                    on_click=EstadoApp.QuitarBarrido(fila["id"]),
                    variant="outline",
                    color_scheme="gray",
                    size="2",
                    aria_label="Quitar característica",
                ),
                spacing="2",
                width="100%",
                align="center",
            ),
            rx.match(
                fila["clave"],
                *[(clave, rx.text(AYUDAS[clave], size="1", class_name="ol-muted")) for clave in EJES],
                rx.fragment(),
            ),
            rx.grid(
                PaginaComparacion.Campo("Desde", fila["desde"], EstadoApp.set_barrido_desde(fila["id"])),
                PaginaComparacion.Campo("Hasta", fila["hasta"], EstadoApp.set_barrido_hasta(fila["id"])),
                PaginaComparacion.Campo("Cada", fila["paso"], EstadoApp.set_barrido_paso(fila["id"])),
                columns="3",
                spacing="3",
                width="100%",
            ),
            spacing="2",
            width="100%",
            padding_bottom="8px",
            border_bottom="1px solid var(--ol-line)",
        )

    @staticmethod
    def Cabecera() -> rx.Component:
        return rx.box(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.text("Lote en curso", class_name="ol-lbl"),
                        rx.cond(
                            EstadoApp.total > 0,
                            rx.heading(
                                EstadoApp.hechos, " de ", EstadoApp.total, " variantes terminadas", size="7",
                                weight="medium",
                            ),
                            rx.heading("Sin lote abierto", size="7", weight="medium"),
                        ),
                        rx.text(EstadoApp.mensaje, size="2", class_name="ol-muted"),
                        spacing="1",
                    ),
                    rx.cond(
                        EstadoApp.ocupado,
                        rx.button(
                            "Cancelar lote",
                            on_click=EstadoApp.CancelarLote,
                            variant="outline",
                            radius="full",
                            size="2",
                            style={"color": "var(--ol-coral)", "box_shadow": "inset 0 0 0 1px var(--ol-coral)"},
                        ),
                        rx.fragment(),
                    ),
                    justify="between",
                    align="center",
                    wrap="wrap",
                    gap="12px",
                    width="100%",
                ),
                rx.cond(
                    EstadoApp.total > 0,
                    rx.vstack(
                        rx.progress(value=EstadoApp.porcentaje, width="100%", size="3", aria_label="Avance del lote"),
                        rx.text(EstadoApp.resumen_estados, size="2", class_name="ol-muted"),
                        spacing="2",
                        width="100%",
                    ),
                    rx.fragment(),
                ),
                spacing="4",
                width="100%",
            ),
            class_name="ol-card",
            width="100%",
        )

    @staticmethod
    def Comparacion() -> rx.Component:
        return rx.cond(
            EstadoApp.vistas.length() > 0,
            rx.box(
                rx.vstack(
                    rx.flex(
                        rx.heading("Comparación 3D", size="5", weight="medium"),
                        rx.text(
                            "Hasta tres a la vez · arrastre, flechas o botones del visor",
                            size="2",
                            class_name="ol-muted",
                        ),
                        justify="between",
                        align="baseline",
                        wrap="wrap",
                        gap="12px",
                        width="100%",
                    ),
                    rx.flex(
                        rx.foreach(EstadoApp.vistas, PaginaComparacion.Marco),
                        wrap="wrap",
                        gap="14px",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                class_name="ol-card",
                background="var(--ol-stage)",
                width="100%",
            ),
            rx.fragment(),
        )

    @staticmethod
    def Tarjeta(ficha) -> rx.Component:
        elegida = EstadoApp.vistas.contains(ficha["archivo"])
        return rx.el.article(
            rx.vstack(
                rx.box(
                    rx.cond(
                        ficha["archivo"] != "",
                        PaginaComparacion.Visor(ficha["archivo"], "150px", miniatura=True),
                        rx.center(
                            rx.cond(
                                ficha["error"] != "",
                                rx.vstack(
                                    rx.icon("triangle-alert", color="var(--ol-coral)"),
                                    rx.text(ficha["error"], size="1", align="center", color="var(--ol-coral)"),
                                    align="center",
                                    spacing="2",
                                ),
                                rx.cond(
                                    ficha["estado"] == "running",
                                    rx.vstack(
                                        rx.spinner(size="3"),
                                        rx.text("Construyendo…", size="1", weight="medium", class_name="ol-muted"),
                                        align="center",
                                    ),
                                    rx.vstack(
                                        rx.icon("clock", color="var(--ol-muted)"),
                                        rx.text("En cola", size="1", weight="medium", class_name="ol-muted"),
                                        align="center",
                                    ),
                                ),
                            ),
                            height="150px",
                            padding="3",
                        ),
                    ),
                    background="var(--ol-stage)",
                    border_radius="14px",
                    width="100%",
                    overflow="hidden",
                ),
                rx.hstack(
                    rx.text(ficha["patron"], size="3", weight="bold"),
                    rx.spacer(),
                    rx.match(
                        ficha["estado"],
                        *[
                            (codigo, rx.el.span(texto, class_name=f"ol-badge ol-b-{codigo}"))
                            for codigo, texto in ESTADOS_VISIBLES.items()
                        ],
                        rx.fragment(),
                    ),
                    width="100%",
                    align="center",
                ),
                rx.text(ficha["detalle"], size="1", class_name="ol-muted"),
                rx.cond(
                    ficha["volumen"] != "",
                    rx.grid(
                        PaginaComparacion.Medida("Volumen", ficha["volumen"]),
                        PaginaComparacion.Medida("Peso", ficha["peso"]),
                        PaginaComparacion.Medida("Precio", ficha["precio"]),
                        columns="3",
                        spacing="2",
                        width="100%",
                        border_top="1px solid var(--ol-line)",
                        padding_top="10px",
                    ),
                    rx.fragment(),
                ),
                rx.hstack(
                    rx.button(
                        rx.cond(elegida, "Quitar de 3D", "Ver en 3D"),
                        size="2",
                        radius="full",
                        variant=rx.cond(elegida, "solid", "outline"),
                        color_scheme=rx.cond(elegida, "teal", "gray"),
                        on_click=EstadoApp.Comparar(ficha["id"]),
                        disabled=ficha["archivo"] == "",
                        aria_pressed=elegida,
                        flex="1",
                    ),
                    rx.button(
                        rx.icon("download", size=14),
                        "STL",
                        size="2",
                        radius="full",
                        variant="outline",
                        color_scheme="gray",
                        on_click=EstadoApp.Descargar(ficha["id"]),
                        disabled=ficha["archivo"] == "",
                    ),
                    spacing="2",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            class_name="ol-card",
            style={"padding": "14px", "border_radius": "20px"},
        )
