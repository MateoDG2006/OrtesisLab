"""Pantalla principal (Diseño): visor de una ortesis, parámetros y superficie de entrada.

El lote se crea y se sigue en /lote (PaginaLote).
"""

from __future__ import annotations

import reflex as rx
from reflex_base.vars.base import Var

from .ConfiguracionBackend import ConfiguracionBackend
from .EstadoApp import ID_SUBIDA_SUPERFICIE, EstadoApp
from .GeneradorWeb import EJES, PATRONES
from .LectorSuperficie import LectorSuperficie
from .Sesion import Sesion

AYUDAS = ConfiguracionBackend.Cargar("web")["ayudas"]

# Trazos de los iconos de patrón del canvas «OrtesisLab Rediseño».
ICONOS_PATRON = {
    "VORONOI": "M3 8l6-5 6 3 1 6-5 4-6-2z M15 6l6-1v8l-5-1 M16 12l5 1v8l-6-1-4-4 M5 14l-2 7h12",
    "HEX": "M7 2.5l4 2.3v4.6L7 11.7 3 9.4V4.8z M17 2.5l4 2.3v4.6l-4 2.3-4-2.3V4.8z "
    "M12 12.3l4 2.3v4.6l-4 2.3-4-2.3v-4.6z",
    "DIAMOND": "M7 2l5 5-5 5-5-5z M17 2l5 5-5 5-5-5z M7 12l5 5-5 5-5-5z M17 12l5 5-5 5-5-5z",
    "SQUARE": "M3 3h7.5v7.5H3z M13.5 3H21v7.5h-7.5z M3 13.5h7.5V21H3z M13.5 13.5H21V21h-7.5z",
    "SOLID": "M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4z",
}


class PaginaComparacion:
    """Escenario con el visor y la ficha, y columna con parámetros y superficie."""

    @staticmethod
    def Pagina(activa: str, *contenido, autenticado=None, nombre=None) -> rx.Component:
        return rx.box(
            rx.vstack(Sesion.Barra(activa, autenticado, nombre), *contenido, spacing="5", width="100%"),
            background="var(--ol-bg)",
            color="var(--ol-text)",
            min_height="100vh",
            padding="20px",
        )

    @staticmethod
    def Index() -> rx.Component:
        return PaginaComparacion.Pagina(
            "/",
            rx.flex(
                PaginaComparacion.Escenario(),
                rx.vstack(
                    PaginaComparacion.Formulario(),
                    PaginaComparacion.Superficie(),
                    spacing="4",
                    flex="1 1 380px",
                    min_width="0",
                ),
                wrap="wrap",
                gap="20px",
                width="100%",
                align="stretch",
            ),
        )

    @staticmethod
    def Escenario() -> rx.Component:
        return rx.el.section(
            rx.text("Una ortesis · previsualización", size="2", weight="medium", class_name="ol-muted"),
            rx.cond(EstadoApp.archivo != "", PaginaComparacion.Resumen(), rx.fragment()),
            rx.cond(
                EstadoApp.archivo != "",
                PaginaComparacion.Visor(EstadoApp.archivo, "640px"),
                rx.center(
                    rx.text("La malla aparece aquí al pulsar Previsualizar.", size="2", class_name="ol-muted"),
                    min_height="480px",
                    width="100%",
                ),
            ),
            rx.cond(
                EstadoApp.ficha_error != "",
                rx.text(EstadoApp.ficha_error, size="2", color_scheme="red"),
                rx.fragment(),
            ),
            rx.flex(
                rx.vstack(
                    rx.text(EstadoApp.mensaje, size="2"),
                    rx.text(
                        "PETG a 0,15 por gramo; la moneda no está declarada en el material. El volumen es el "
                        "del cascarón, antes del voxel, y no predice el filamento ni la resistencia.",
                        size="1",
                        class_name="ol-muted",
                    ),
                    spacing="1",
                    flex="1 1 280px",
                ),
                rx.hstack(
                    rx.button(
                        rx.icon("download", size=16),
                        "Descargar STL",
                        on_click=EstadoApp.DescargarVista,
                        disabled=EstadoApp.archivo == "",
                        variant="outline",
                        color_scheme="gray",
                        radius="full",
                        size="3",
                    ),
                    rx.button(
                        rx.icon("play", size=16),
                        "Previsualizar",
                        on_click=EstadoApp.Previsualizar,
                        loading=EstadoApp.ocupado,
                        disabled=EstadoApp.ocupado,
                        radius="full",
                        size="3",
                    ),
                    spacing="3",
                    wrap="wrap",
                ),
                gap="16px",
                align="end",
                justify="between",
                wrap="wrap",
                width="100%",
            ),
            aria_label="Visor 3D",
            style={
                "flex": "999 1 640px",
                "min_width": "0",
                "position": "relative",
                "display": "flex",
                "flex_direction": "column",
                "gap": "16px",
                "background": "var(--ol-stage)",
            },
        )

    @staticmethod
    def Resumen() -> rx.Component:
        # <details> pliega la ficha sin estado en el servidor.
        def fila(etiqueta: str, valor) -> rx.Component:
            return rx.el.div(rx.el.dt(etiqueta), rx.el.dd(valor))

        return rx.el.details(
            rx.el.summary("Resumen"),
            rx.el.dl(
                fila("Volumen", EstadoApp.ficha_volumen),
                fila("Peso PETG", EstadoApp.ficha_peso),
                fila("Precio", EstadoApp.ficha_precio),
            ),
            rx.text(EstadoApp.ficha_detalle, size="1", margin_top="8px"),
            open=True,
            class_name="ol-resumen",
            aria_label="Ficha de la pieza",
        )

    @staticmethod
    def Formulario() -> rx.Component:
        return rx.el.section(
            rx.vstack(
                rx.hstack(
                    rx.heading("Parámetros", size="5", weight="medium"),
                    rx.spacer(),
                    rx.button(
                        rx.icon("rotate-ccw", size=14),
                        "Restaurar",
                        size="2",
                        variant="outline",
                        color_scheme="gray",
                        radius="full",
                        on_click=EstadoApp.RestaurarPredeterminados,
                        disabled=EstadoApp.ocupado,
                    ),
                    width="100%",
                    align="center",
                ),
                rx.box(
                    PaginaComparacion.Etiqueta("Patrón", AYUDAS["pattern"]),
                    rx.grid(
                        *[
                            PaginaComparacion.Mosaico(
                                codigo,
                                EstadoApp.pattern == codigo,
                                EstadoApp.set_pattern(codigo),
                                "radio",
                            )
                            for codigo in PATRONES
                        ],
                        role="radiogroup",
                        aria_label="Patrón",
                        columns="3",
                        spacing="2",
                        margin_top="6px",
                    ),
                    width="100%",
                ),
                rx.cond(
                    EstadoApp.es_macizo,
                    PaginaComparacion.Numero("solid_mm", EstadoApp.solid_mm, EstadoApp.set_solid_mm),
                    rx.vstack(
                        rx.grid(
                            PaginaComparacion.Numero("cell_mm", EstadoApp.cell_mm, EstadoApp.set_cell_mm),
                            PaginaComparacion.Numero(
                                "rib_width_mm", EstadoApp.rib_width_mm, EstadoApp.set_rib_width_mm
                            ),
                            PaginaComparacion.Numero(
                                "rib_height_mm", EstadoApp.rib_height_mm, EstadoApp.set_rib_height_mm
                            ),
                            columns={"initial": "1", "sm": "3"},
                            spacing="3",
                            width="100%",
                        ),
                        rx.flex(
                            rx.vstack(
                                PaginaComparacion.Etiqueta("Capa interior continua", AYUDAS["liner"]),
                                rx.text(
                                    rx.cond(
                                        EstadoApp.liner,
                                        "Piel continua bajo la nervadura",
                                        "Rejilla abierta: la altura es el espesor",
                                    ),
                                    size="1",
                                    class_name="ol-muted",
                                ),
                                spacing="1",
                            ),
                            rx.switch(
                                checked=EstadoApp.liner,
                                on_change=EstadoApp.set_liner,
                                aria_label="Capa interior continua",
                                size="3",
                            ),
                            justify="between",
                            align="center",
                            gap="12px",
                            width="100%",
                            class_name="ol-sub",
                        ),
                        rx.cond(
                            EstadoApp.liner,
                            rx.grid(
                                PaginaComparacion.Numero("skin_mm", EstadoApp.skin_mm, EstadoApp.set_skin_mm),
                                rx.text(
                                    "Total en nervadura: ",
                                    rx.el.strong(EstadoApp.espesor_total, " mm"),
                                    size="2",
                                    class_name="ol-muted",
                                    align_self="end",
                                    padding_bottom="10px",
                                ),
                                columns="2",
                                spacing="3",
                                width="100%",
                            ),
                            rx.fragment(),
                        ),
                        spacing="3",
                        width="100%",
                    ),
                ),
                rx.box(
                    rx.button(
                        "Parámetros avanzados",
                        rx.icon(rx.cond(EstadoApp.avanzados, "chevron-up", "chevron-down"), size=18),
                        on_click=EstadoApp.set_avanzados(~EstadoApp.avanzados),
                        aria_expanded=EstadoApp.avanzados,
                        variant="ghost",
                        color_scheme="gray",
                        size="3",
                        width="100%",
                        justify_content="space-between",
                        style={"font_weight": "700"},
                    ),
                    rx.cond(EstadoApp.avanzados, PaginaComparacion.Avanzados(), rx.fragment()),
                    border_top="1px solid var(--ol-line)",
                    padding_top="14px",
                    width="100%",
                ),
                rx.text(
                    "La reconstrucción voxel solo está disponible en Blender y está ",
                    rx.cond(EstadoApp.repair, "activada", "desactivada"),
                    ", resolución ",
                    EstadoApp.resolution_mm,
                    " mm.",
                    size="1",
                    class_name="ol-muted",
                ),
                spacing="4",
                width="100%",
            ),
            aria_label="Configuración",
            class_name="ol-card",
        )

    @staticmethod
    def Avanzados() -> rx.Component:
        return rx.vstack(
            rx.cond(
                ~EstadoApp.es_macizo,
                rx.grid(
                    PaginaComparacion.Numero("angle_deg", EstadoApp.angle_deg, EstadoApp.set_angle_deg),
                    PaginaComparacion.Numero("border_mm", EstadoApp.border_mm, EstadoApp.set_border_mm),
                    PaginaComparacion.Numero(
                        "reinforce_width_mm", EstadoApp.reinforce_width_mm, EstadoApp.set_reinforce_width_mm
                    ),
                    PaginaComparacion.Numero("reinforce_y_mm", EstadoApp.reinforce_y_mm, EstadoApp.set_reinforce_y_mm),
                    PaginaComparacion.Campo(
                        "Paso de superficie (mm)",
                        EstadoApp.surface_step_mm,
                        EstadoApp.set_surface_step_mm,
                        AYUDAS["surface_step_mm"],
                    ),
                    rx.cond(
                        EstadoApp.liner,
                        PaginaComparacion.Numero("rounding_mm", EstadoApp.rounding_mm, EstadoApp.set_rounding_mm),
                        rx.fragment(),
                    ),
                    rx.cond(
                        EstadoApp.pide_semilla,
                        PaginaComparacion.Numero("seed", EstadoApp.seed, EstadoApp.set_seed),
                        rx.fragment(),
                    ),
                    columns="2",
                    spacing="3",
                    width="100%",
                ),
                rx.fragment(),
            ),
            PaginaComparacion.Interruptor(
                "Invertir lado del espesor", EstadoApp.flip_normals, EstadoApp.set_flip_normals, AYUDAS["flip_normals"]
            ),
            spacing="3",
            width="100%",
            padding_top="8px",
        )

    @staticmethod
    def Superficie() -> rx.Component:
        return rx.el.section(
            rx.hstack(
                rx.el.svg(
                    rx.el.svg.path(
                        d="M8 40C8 28 22 22 34 20L52 18C58 18 58 34 52 36L32 42C20 46 8 48 8 40Z",
                        fill="var(--ol-meshfill)",
                        stroke="var(--ol-mesh)",
                        stroke_width="2",
                    ),
                    view_box="0 0 64 64",
                    width="64",
                    height="64",
                    aria_hidden="true",
                    style={"border_radius": "12px", "background": "var(--ol-panel2)", "flex": "none"},
                ),
                rx.vstack(
                    rx.text("Superficie de entrada", class_name="ol-lbl"),
                    rx.text(EstadoApp.superficie_nombre, size="2", weight="bold"),
                    PaginaComparacion.Cargador(),
                    spacing="1",
                    min_width="0",
                ),
                spacing="4",
                align="center",
            ),
            rx.grid(
                rx.text("Malla", class_name="ol-lbl"),
                rx.text("Espesor total", class_name="ol-lbl"),
                rx.text(EstadoApp.superficie_detalle, size="2", weight="medium"),
                rx.text(EstadoApp.espesor_total, " mm", size="2", weight="medium"),
                columns="2",
                spacing_x="4",
                spacing_y="1",
                border_top="1px solid var(--ol-line)",
                padding_top="12px",
                margin_top="14px",
            ),
            rx.cond(
                EstadoApp.superficie_error != "",
                rx.text(EstadoApp.superficie_error, size="1", color_scheme="red", margin_top="8px"),
                rx.fragment(),
            ),
            aria_label="Superficie de entrada",
            class_name="ol-card",
            padding="18px",
        )

    @staticmethod
    def Cargador() -> rx.Component:
        # Diálogo «Cambiar superficie» del canvas: zona de arrastre y carga.
        return rx.dialog.root(
            rx.dialog.trigger(
                rx.el.button(
                    "Cambiar archivo (STL o NPZ)",
                    type="button",
                    style={
                        "background": "none",
                        "border": "none",
                        "padding": "0",
                        "min_height": "24px",
                        "text_align": "left",
                        "color": "var(--ol-accent)",
                        "font": "inherit",
                        "font_size": "13px",
                        "font_weight": "600",
                        "text_decoration": "underline",
                        "cursor": "pointer",
                    },
                )
            ),
            rx.dialog.content(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.dialog.title("Cambiar superficie", size="5", weight="medium", margin="0"),
                            rx.dialog.description(
                                "Superficie interior escaneada del paciente, de una sola capa y abierta.",
                                size="2",
                                class_name="ol-muted",
                            ),
                            spacing="1",
                        ),
                        rx.dialog.close(
                            rx.icon_button(
                                rx.icon("x", size=18),
                                variant="outline",
                                color_scheme="gray",
                                size="3",
                                aria_label="Cerrar",
                            )
                        ),
                        justify="between",
                        align="start",
                        width="100%",
                    ),
                    rx.upload(
                        rx.vstack(
                            rx.center(
                                rx.icon("upload", size=24),
                                width="56px",
                                height="56px",
                                border_radius="50%",
                                background="var(--ol-strong)",
                                color="#F3EDE6",
                            ),
                            rx.text("Arrastre un archivo aquí", size="3", weight="bold"),
                            rx.text("o haga clic para elegirlo · STL o NPZ", size="2", class_name="ol-muted"),
                            rx.foreach(
                                rx.selected_files(ID_SUBIDA_SUPERFICIE),
                                lambda nombre: rx.badge(nombre, variant="soft"),
                            ),
                            spacing="3",
                            align="center",
                        ),
                        id=ID_SUBIDA_SUPERFICIE,
                        accept={
                            "model/stl": [".stl"],
                            "application/octet-stream": [".stl", ".npz"],
                        },
                        max_files=1,
                        max_size=LectorSuperficie.MAXIMO_BYTES,
                        multiple=False,
                        border="1.5px dashed var(--ol-mesh)",
                        border_radius="18px",
                        background="var(--ol-meshfill)",
                        padding="32px 20px",
                        width="100%",
                        cursor="pointer",
                    ),
                    rx.flex(
                        rx.button(
                            "Cargar archivo",
                            on_click=EstadoApp.CargarSuperficie(rx.upload_files(upload_id=ID_SUBIDA_SUPERFICIE)),
                            loading=EstadoApp.subiendo_superficie,
                            disabled=EstadoApp.ocupado | EstadoApp.subiendo_superficie,
                            radius="full",
                            size="3",
                            flex="1 1 160px",
                        ),
                        rx.button(
                            "Usar superficie incluida",
                            on_click=EstadoApp.UsarSuperficieIncluida,
                            disabled=EstadoApp.ocupado | EstadoApp.subiendo_superficie,
                            variant="outline",
                            color_scheme="gray",
                            radius="full",
                            size="3",
                            flex="1 1 160px",
                        ),
                        gap="10px",
                        wrap="wrap",
                        width="100%",
                    ),
                    rx.cond(
                        EstadoApp.superficie_error != "",
                        rx.text(EstadoApp.superficie_error, size="1", color_scheme="red"),
                        rx.text(EstadoApp.superficie_detalle, size="1", class_name="ol-muted"),
                    ),
                    spacing="4",
                    width="100%",
                ),
                max_width="480px",
                style={"border_radius": "24px", "background": "var(--ol-panel)"},
            ),
        )

    @staticmethod
    def Mosaico(codigo: str, elegido, al_pulsar, rol: str) -> rx.Component:
        # Botón de patrón con icono; ``rol`` es "radio" (Diseño) o "pressed" (Lotes, varios a la vez).
        estado = {"aria-checked": elegido, "role": "radio"} if rol == "radio" else {"aria-pressed": elegido}
        return rx.el.button(
            rx.el.svg(
                rx.el.svg.path(d=ICONOS_PATRON[codigo]),
                view_box="0 0 24 24",
                width="30",
                height="30",
                fill="currentColor" if codigo == "SOLID" else "none",
                fill_opacity="0.35" if codigo == "SOLID" else "1",
                stroke="currentColor",
                stroke_width="1.6",
                stroke_linecap="round",
                stroke_linejoin="round",
                aria_hidden="true",
            ),
            rx.el.span(PATRONES[codigo]),
            type="button",
            on_click=al_pulsar,
            class_name="ol-tile",
            custom_attrs=estado,
        )

    @staticmethod
    def Marco(archivo) -> rx.Component:
        return rx.box(PaginaComparacion.Visor(archivo, "320px"), flex="1", min_width="220px")

    @staticmethod
    def Visor(archivo, alto: str, miniatura: bool = False) -> rx.Component:
        # El iframe carga el STL desde el bucket. La miniatura dibuja un fotograma y libera WebGL.
        return rx.el.iframe(
            src=PaginaComparacion.Enlace(archivo, miniatura),
            title="Miniatura de la ortesis" if miniatura else "Vista previa de la ortesis",
            width="100%",
            height=alto,
            border_radius="12px",
            border="0",
            custom_attrs={"loading": "lazy"},
            tab_index=-1 if miniatura else 0,
        )

    @staticmethod
    def Enlace(archivo, miniatura: bool = False):
        # ``archivo`` es el object_url del STL en el bucket; el visor lo descarga sin pasar por el backend.
        url = archivo if isinstance(archivo, Var) else Var.create(archivo)
        extra = "&miniatura=1" if miniatura else ""
        expresion = f"`/visor.html?src=${{encodeURIComponent({url})}}{extra}`"
        return Var(_js_expr=expresion, _var_type=str, _var_data=url._get_all_var_data())

    @staticmethod
    def Etiqueta(texto: str, ayuda: str = "") -> rx.Component:
        # El icono es enfocable: la ayuda se abre con ratón, teclado o toque.
        if not ayuda:
            return rx.text(texto, class_name="ol-lbl")
        return rx.hstack(
            rx.text(texto, class_name="ol-lbl"),
            rx.tooltip(
                rx.icon_button(
                    rx.icon("circle-help", size=14),
                    size="1",
                    variant="ghost",
                    radius="full",
                    color_scheme="gray",
                    aria_label=f"Ayuda: {ayuda}",
                    type="button",
                ),
                content=ayuda,
            ),
            spacing="1",
            align="center",
        )

    @staticmethod
    def Numero(clave: str, valor, cambio) -> rx.Component:
        # Etiqueta y ayuda salen de web.yaml (ejes y ayudas) para no repetir textos.
        return PaginaComparacion.Campo(EJES[clave], valor, cambio, AYUDAS[clave])

    @staticmethod
    def Campo(etiqueta: str, valor, cambio, ayuda: str = "") -> rx.Component:
        return rx.vstack(
            PaginaComparacion.Etiqueta(etiqueta, ayuda),
            rx.input(
                value=valor,
                on_change=cambio,
                type="number",
                width="100%",
                size="3",
                aria_label=etiqueta,
                style={"font_weight": "600"},
            ),
            spacing="1",
            width="100%",
        )

    @staticmethod
    def Interruptor(etiqueta: str, valor, cambio, ayuda: str = "") -> rx.Component:
        return rx.hstack(
            rx.switch(checked=valor, on_change=cambio, aria_label=etiqueta),
            PaginaComparacion.Etiqueta(etiqueta, ayuda),
            spacing="2",
            align="center",
            min_height="44px",
        )

    @staticmethod
    def Selector(etiqueta: str, valor, cambio, opciones: list[tuple[str, str]], ayuda: str = "") -> rx.Component:
        return rx.vstack(
            PaginaComparacion.Etiqueta(etiqueta, ayuda),
            rx.select.root(
                rx.select.trigger(width="100%", aria_label=etiqueta),
                rx.select.content(
                    *[rx.select.item(texto, value=codigo) for codigo, texto in opciones],
                ),
                value=valor,
                on_change=cambio,
                size="3",
            ),
            spacing="1",
            width="100%",
        )

    @staticmethod
    def Medida(etiqueta: str, valor) -> rx.Component:
        return rx.vstack(
            rx.text(etiqueta, size="1", weight="medium", class_name="ol-muted"),
            rx.text(valor, size="2", weight="bold"),
            spacing="0",
        )
