"""Pantalla principal: parámetros, previsualización de una ortesis y creación de lotes.

El progreso de los lotes se sigue en /lote (PaginaLote).
"""

from __future__ import annotations

import reflex as rx
from reflex_base.vars.base import Var

from .ConfiguracionBackend import ConfiguracionBackend
from .EstadoApp import (
    ETIQUETAS_EJE,
    ID_SUBIDA_SUPERFICIE,
    LIMITE_LOTE,
    EstadoApp,
)
from .GeneradorWeb import EJES, PATRONES
from .LectorSuperficie import LectorSuperficie
from .Sesion import Sesion

AYUDAS = ConfiguracionBackend.Cargar("web")["ayudas"]


class PaginaComparacion:
    """Formulario de parámetros (genéricos y avanzados), vista previa y lote."""

    @staticmethod
    def Index() -> rx.Component:
        return rx.box(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                Sesion.Barra(),
                rx.heading("OrtesisLab", size="8"),
                rx.text(
                    "Configure los parámetros y previsualice una ortesis, o genere un lote de variantes "
                    "y siga su avance con miniaturas. El cascarón, el volumen, el peso y el precio salen "
                    "del mismo cálculo; la reconstrucción voxel queda en Blender.",
                    size="3",
                    color_scheme="gray",
                ),
                rx.hstack(
                    rx.vstack(
                        PaginaComparacion.Superficie(),
                        PaginaComparacion.Formulario(),
                        spacing="4",
                        width="100%",
                        max_width="420px",
                    ),
                    PaginaComparacion.Acciones(),
                    align="start",
                    width="100%",
                    spacing="6",
                    wrap="wrap",
                ),
                spacing="5",
                width="100%",
            ),
            padding="6",
            max_width="1200px",
            margin="0 auto",
        )

    @staticmethod
    def Formulario() -> rx.Component:
        return rx.card(
            rx.vstack(
                rx.hstack(
                    rx.heading("Parámetros", size="5"),
                    rx.spacer(),
                    rx.button(
                        rx.icon("rotate-ccw", size=14),
                        "Restaurar",
                        size="1",
                        variant="ghost",
                        on_click=EstadoApp.RestaurarPredeterminados,
                        disabled=EstadoApp.ocupado,
                    ),
                    width="100%",
                    align="center",
                ),
                PaginaComparacion.Selector(
                    "Patrón", EstadoApp.pattern, EstadoApp.set_pattern, list(PATRONES.items()), AYUDAS["pattern"]
                ),
                rx.cond(
                    EstadoApp.pattern == "SOLID",
                    PaginaComparacion.Numero("solid_mm", EstadoApp.solid_mm, EstadoApp.set_solid_mm),
                    rx.vstack(
                        PaginaComparacion.Numero("cell_mm", EstadoApp.cell_mm, EstadoApp.set_cell_mm),
                        PaginaComparacion.Numero("rib_width_mm", EstadoApp.rib_width_mm, EstadoApp.set_rib_width_mm),
                        PaginaComparacion.Numero("rib_height_mm", EstadoApp.rib_height_mm, EstadoApp.set_rib_height_mm),
                        PaginaComparacion.Interruptor(
                            "Capa interior continua", EstadoApp.liner, EstadoApp.set_liner, AYUDAS["liner"]
                        ),
                        rx.cond(
                            EstadoApp.liner,
                            rx.vstack(
                                PaginaComparacion.Numero("skin_mm", EstadoApp.skin_mm, EstadoApp.set_skin_mm),
                                rx.text("Espesor total en nervadura: ", EstadoApp.espesor_total, " mm", size="2"),
                                spacing="3",
                                width="100%",
                            ),
                            rx.text("Rejilla abierta: la altura es el espesor total.", size="2"),
                        ),
                        spacing="3",
                        width="100%",
                    ),
                ),
                rx.separator(size="4"),
                rx.text(
                    rx.hstack(
                        rx.checkbox(checked=EstadoApp.avanzados, on_change=EstadoApp.set_avanzados),
                        "Mostrar parámetros avanzados",
                        spacing="2",
                        align="center",
                    ),
                    as_="label",
                    size="2",
                    weight="medium",
                ),
                rx.cond(EstadoApp.avanzados, PaginaComparacion.Avanzados(), rx.box()),
                rx.text(
                    "La reconstrucción voxel solo está disponible en Blender y está ",
                    rx.cond(EstadoApp.repair, "activada", "desactivada"),
                    ", resolución ",
                    EstadoApp.resolution_mm,
                    " mm.",
                    size="1",
                    color_scheme="gray",
                ),
                spacing="3",
                width="100%",
            ),
            width="100%",
        )

    @staticmethod
    def Avanzados() -> rx.Component:
        return rx.vstack(
            rx.cond(
                EstadoApp.pattern != "SOLID",
                rx.vstack(
                    rx.cond(
                        EstadoApp.liner,
                        PaginaComparacion.Numero("rounding_mm", EstadoApp.rounding_mm, EstadoApp.set_rounding_mm),
                        rx.box(),
                    ),
                    PaginaComparacion.Numero("angle_deg", EstadoApp.angle_deg, EstadoApp.set_angle_deg),
                    rx.cond(
                        EstadoApp.pattern == "VORONOI",
                        PaginaComparacion.Numero("seed", EstadoApp.seed, EstadoApp.set_seed),
                        rx.box(),
                    ),
                    PaginaComparacion.Numero("border_mm", EstadoApp.border_mm, EstadoApp.set_border_mm),
                    PaginaComparacion.Numero(
                        "reinforce_width_mm", EstadoApp.reinforce_width_mm, EstadoApp.set_reinforce_width_mm
                    ),
                    PaginaComparacion.Numero("reinforce_y_mm", EstadoApp.reinforce_y_mm, EstadoApp.set_reinforce_y_mm),
                    PaginaComparacion.Campo(
                        "Paso de superficie para el patrón (mm)",
                        EstadoApp.surface_step_mm,
                        EstadoApp.set_surface_step_mm,
                        AYUDAS["surface_step_mm"],
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.box(),
            ),
            PaginaComparacion.Interruptor(
                "Invertir lado del espesor", EstadoApp.flip_normals, EstadoApp.set_flip_normals, AYUDAS["flip_normals"]
            ),
            spacing="3",
            width="100%",
            padding_left="3",
            border_left="2px solid var(--accent-6)",
        )

    @staticmethod
    def Acciones() -> rx.Component:
        return rx.card(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Una ortesis", value="una"),
                    rx.tabs.trigger("Lote de variantes", value="lote"),
                ),
                rx.tabs.content(PaginaComparacion.Vista(), value="una", padding_top="4"),
                rx.tabs.content(PaginaComparacion.Lote(), value="lote", padding_top="4"),
                default_value="una",
                width="100%",
            ),
            flex="1",
            min_width="320px",
        )

    @staticmethod
    def Superficie() -> rx.Component:
        return rx.card(
            rx.vstack(
                rx.heading("Superficie de entrada", size="5"),
                rx.upload(
                    rx.vstack(
                        rx.icon("upload", size=24),
                        rx.text("Arrastre un STL o NPZ, o haga clic para elegirlo.", size="2"),
                        rx.foreach(
                            rx.selected_files(ID_SUBIDA_SUPERFICIE),
                            lambda nombre: rx.badge(nombre, variant="soft"),
                        ),
                        spacing="2",
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
                    border="1px dashed var(--gray-7)",
                    border_radius="10px",
                    padding="4",
                    width="100%",
                    cursor="pointer",
                ),
                rx.hstack(
                    rx.button(
                        "Cargar archivo",
                        on_click=EstadoApp.CargarSuperficie(rx.upload_files(upload_id=ID_SUBIDA_SUPERFICIE)),
                        loading=EstadoApp.subiendo_superficie,
                        disabled=EstadoApp.ocupado | EstadoApp.subiendo_superficie,
                        size="2",
                    ),
                    rx.button(
                        "Usar incluida",
                        on_click=EstadoApp.UsarSuperficieIncluida,
                        disabled=EstadoApp.ocupado | EstadoApp.subiendo_superficie,
                        size="2",
                        variant="soft",
                    ),
                    spacing="2",
                ),
                rx.vstack(
                    rx.text(EstadoApp.superficie_nombre, size="2", weight="bold"),
                    rx.text(EstadoApp.superficie_detalle, size="1", color_scheme="gray"),
                    rx.cond(
                        EstadoApp.superficie_error != "",
                        rx.text(EstadoApp.superficie_error, size="1", color_scheme="red"),
                        rx.box(),
                    ),
                    spacing="1",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            width="100%",
        )

    @staticmethod
    def Vista() -> rx.Component:
        return rx.vstack(
            rx.hstack(
                rx.button(
                    "Previsualizar",
                    on_click=EstadoApp.Previsualizar,
                    loading=EstadoApp.ocupado,
                    disabled=EstadoApp.ocupado,
                    size="3",
                ),
                rx.text(EstadoApp.mensaje, size="2", color_scheme="gray"),
                align="center",
                spacing="3",
                wrap="wrap",
            ),
            rx.cond(
                EstadoApp.archivo != "",
                rx.vstack(
                    PaginaComparacion.Visor(EstadoApp.archivo, "520px"),
                    rx.text(EstadoApp.ficha_detalle, size="2", weight="medium"),
                    rx.hstack(
                        PaginaComparacion.Medida("Volumen", EstadoApp.ficha_volumen),
                        PaginaComparacion.Medida("Peso PETG", EstadoApp.ficha_peso),
                        PaginaComparacion.Medida("Precio", EstadoApp.ficha_precio),
                        spacing="4",
                        wrap="wrap",
                    ),
                    rx.text(
                        "PETG a 0,15 por gramo. La moneda no está declarada en el material. "
                        "El volumen es el del cascarón, antes del voxel, y no predice el filamento ni la resistencia.",
                        size="1",
                        color_scheme="gray",
                    ),
                    rx.cond(
                        EstadoApp.ficha_error != "",
                        rx.text(EstadoApp.ficha_error, size="2", color_scheme="red"),
                        rx.box(),
                    ),
                    spacing="3",
                    width="100%",
                ),
                rx.center(
                    rx.text("La malla aparece aquí al pulsar Previsualizar.", size="2", color_scheme="gray"),
                    min_height="520px",
                    width="100%",
                ),
            ),
            spacing="3",
            width="100%",
        )

    @staticmethod
    def Lote() -> rx.Component:
        return rx.vstack(
            rx.text(
                f"El lote parte de los parámetros de la izquierda. Elija los patrones y, si quiere, "
                f"un parámetro que recorra un rango. Admite hasta {LIMITE_LOTE} variantes.",
                size="2",
                color_scheme="gray",
            ),
            rx.text("1. Patrones", size="3", weight="bold"),
            rx.grid(
                PaginaComparacion.Casilla(PATRONES["VORONOI"], EstadoApp.usar_voronoi, EstadoApp.set_usar_voronoi),
                PaginaComparacion.Casilla(PATRONES["HEX"], EstadoApp.usar_hex, EstadoApp.set_usar_hex),
                PaginaComparacion.Casilla(PATRONES["DIAMOND"], EstadoApp.usar_diamond, EstadoApp.set_usar_diamond),
                PaginaComparacion.Casilla(PATRONES["SQUARE"], EstadoApp.usar_square, EstadoApp.set_usar_square),
                PaginaComparacion.Casilla(PATRONES["SOLID"], EstadoApp.usar_solid, EstadoApp.set_usar_solid),
                columns={"initial": "1", "sm": "2", "md": "3"},
                spacing="2",
                width="100%",
            ),
            rx.text("2. Parámetro que varía", size="3", weight="bold"),
            PaginaComparacion.Selector("Parámetro", EstadoApp.eje, EstadoApp.set_eje, ETIQUETAS_EJE),
            rx.cond(
                EstadoApp.eje != "ninguno",
                rx.vstack(
                    rx.match(
                        EstadoApp.eje,
                        *[(clave, rx.text(AYUDAS[clave], size="1", color_scheme="gray")) for clave in EJES],
                        rx.box(),
                    ),
                    rx.hstack(
                        PaginaComparacion.Campo("Desde", EstadoApp.desde, EstadoApp.set_desde),
                        PaginaComparacion.Campo("Hasta", EstadoApp.hasta, EstadoApp.set_hasta),
                        PaginaComparacion.Campo("Cada", EstadoApp.paso, EstadoApp.set_paso),
                        spacing="3",
                        width="100%",
                        align="start",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.box(),
            ),
            rx.text("3. Capa interior", size="3", weight="bold"),
            PaginaComparacion.Interruptor(
                "Probar con capa continua y sin ella",
                EstadoApp.ambos_revestimientos,
                EstadoApp.set_ambos_revestimientos,
                "Duplica cada variante con patrón: una con piel continua y otra de rejilla abierta.",
            ),
            rx.callout(
                EstadoApp.resumen_lote,
                icon=rx.cond(EstadoApp.lote_valido, "layers", "triangle-alert"),
                color_scheme=rx.cond(EstadoApp.lote_valido, "grass", "red"),
                size="1",
                width="100%",
            ),
            rx.hstack(
                rx.button(
                    "Generar lote y ver progreso",
                    on_click=EstadoApp.PedirLote,
                    loading=EstadoApp.ocupado,
                    disabled=EstadoApp.ocupado | ~EstadoApp.lote_valido,
                    size="3",
                ),
                rx.cond(
                    EstadoApp.lote_id != "",
                    rx.link("Ver progreso del último lote", href="/lote", size="2"),
                    rx.box(),
                ),
                align="center",
                spacing="4",
                wrap="wrap",
            ),
            rx.text(EstadoApp.mensaje, size="2", color_scheme="gray"),
            spacing="3",
            width="100%",
        )

    @staticmethod
    def Casilla(etiqueta: str, valor, cambio) -> rx.Component:
        return rx.card(
            rx.text(
                rx.hstack(rx.checkbox(checked=valor, on_change=cambio), etiqueta, spacing="2", align="center"),
                as_="label",
                size="2",
            ),
            size="1",
            variant=rx.cond(valor, "surface", "ghost"),
        )

    @staticmethod
    def Marco(archivo) -> rx.Component:
        return rx.box(PaginaComparacion.Visor(archivo, "320px"), flex="1", min_width="260px")

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
            return rx.text(texto, size="2", weight="medium")
        return rx.hstack(
            rx.text(texto, size="2", weight="medium"),
            rx.tooltip(
                rx.icon_button(
                    rx.icon("info", size=14),
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
            rx.input(value=valor, on_change=cambio, type="number", width="100%", aria_label=etiqueta),
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
                size="2",
            ),
            spacing="1",
            width="100%",
        )

    @staticmethod
    def Medida(etiqueta: str, valor) -> rx.Component:
        return rx.vstack(
            rx.text(etiqueta, size="1", color_scheme="gray"),
            rx.text(valor, size="4", weight="bold"),
            spacing="1",
        )
