# Auditoría de interfaz OrtesisLab

Written against: `0965184`  
Skills: `impeccable` (audit), `improve-ui`, `better-interface`, `better-accessibility`, `better-layout`, `better-writing`, `better-typography`, `better-colors`, `better-ui`, `web-design-guidelines`, `baseline-ui`  
Método: revisión de código y contratos de diseño en repo. **Rendered / teclado / lector de pantalla: Not verified** (no hay captura ni app viva en esta sesión).

## Design language

- Audited surface: App web Reflex — rutas `/`, `/lote`, `/historial`, barra `Sesion`, gate `/auth/*`, iframe `visor.html`
- Design sources: `apps/web/assets/ortesislab.css` (tokens `--ol-*`, modo claro/oscuro), canvas «OrtesisLab Rediseño» citado en CSS/código, `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md`
- Documented decisions: paleta `--ol-*` + Radix Themes; tipografía Manrope; cards `ol-card` / nav píldora; badges de estado; ficha flotante `ol-resumen`
- Governing owners and consumers: `PaginaComparacion.Pagina` + `Sesion.Barra` (shell); páginas de dominio; CSS global; auth HTML aparte; visor HTML aparte
- Explicit exceptions: None documented

## Audit Health Score (`impeccable audit`)

| # | Dimension | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Accessibility | 2/4 | Controles etiquetados en formularios; falta landmark `main`, patrón teclado del radiogroup de patrones incompleto, auth/visor fuera del sistema, ayuda `size=1` pequeña |
| 2 | Performance | 3/4 | iframes `loading=lazy`; miniaturas liberan WebGL; riesgo de varios WebGL en comparación 3D (hasta 3) |
| 3 | Theming | 2/4 | Tokens claros/oscuros coherentes en app; **auth** y **visor.html** usan colores fijos ajenos a `--ol-*` |
| 4 | Responsive Design | 2/4 | Wrap en Diseño/Lotes; Historial fuerza `min_width=960px` + scroll; ficha resumen solo se destapa `<768px` |
| 5 | Implementation Integrity | 3/4 | Sistema visual propio (teal/coral/Manrope) reconocible; rotura en gate de autenticación y en el iframe 3D |
| **Total** | | **12/20** | **Acceptable** — trabajo significativo, identidad de producto recuperable |

## Verdict por pantalla

### Shell (`Sesion.Barra`) — Operate

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| MEDIUM | Sin landmark de contenido: el shell envuelve todo en `rx.box`/`vstack` sin `<main>` | `PaginaComparacion.Pagina` |
| LOW | Marca es `rx.text`, no encabezado de documento; no hay skip-link | `Sesion.py:57` |
| — | Nav con `aria-current`, theme toggle y logout con `aria_label`: bien | `Sesion.py:60-73` |

### `/` Diseño — Operate

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| HIGH | Visor 3D: instrucción y control orientados a arrastre; iframe sin alternativa de cámara por teclado (docs lo confirman) | `PaginaLote` copy «arrastre…»; `COMPONENTES_Y_FLUJOS.md` UX; `Visor` |
| MEDIUM | `role=radiogroup` + botones `role=radio` sin roving tabindex / flechas APG | `PaginaComparacion.Formulario` + `Mosaico` |
| MEDIUM | CTA «Cambiar archivo…» como enlace subrayado `min_height: 24px` (cumple 2.5.8 AA mínimo; frágil en touch) | `Cargador` trigger |
| MEDIUM | Ayuda `icon_button size="1"` + icono 14px: hit area marginal | `Etiqueta` |
| LOW | Placeholder del escenario solo texto; sin CTA inline hacia Previsualizar/superficie | `Escenario` |
| LOW | Colores hardcodeados residuales (`#F3EDE6` en upload, outline focus fijo) | `Cargador`, `ortesislab.css` |
| — | Contraste `--ol-muted` / `--ol-text` sobre fondos claros/oscuros: **pasa AA** (medido en tokens) | cálculo WCAG sobre CSS |

### `/lote` Lotes — Operate

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| MEDIUM | Misma dependencia de interacción por arrastre en comparación 3D | `Comparacion` |
| MEDIUM | Cuadrícula vacía sin empty state cuando no hay `resultados` y «Sin lote abierto» | `Index` + `Cabecera` |
| LOW | Duplicación de copy/estructura vs Diseño (patrones, capa) sin título de página `<h1>` único | `NuevoLote` heading size 5 |
| — | Progress con `aria_label`; tarjetas con estados textuales + badge: buena redundancia | `Cabecera`, `Tarjeta` |

### `/historial` — Operate / Read

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| HIGH (responsive) | Tabla `min_width="960px"` → scroll horizontal obligatorio en viewports estrechos; sin vista alternativa (cards) | `PaginaHistorial.Tabla` |
| MEDIUM | Sin empty state cuando `filas` está vacío | `Tabla` body `foreach` |
| MEDIUM | Columna de acciones sin encabezado accesible (`column_header_cell("")`) | `Tabla` header |
| LOW | Acciones icon-only bien etiquetadas (`aria_label` + tooltip) | `Accion` |
| — | Comparación `auto-fit minmax(280px)` razonable | `Comparacion` |

### `/auth/login` · `/auth/registro` — Persuade/Operate (gate)

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| HIGH (integrity) | HTML mínimo `system-ui`, sin Manrope, sin `--ol-*`, sin dark mode, sin marca visual OrtesisLab | `Autenticacion._Pagina` |
| MEDIUM | Registro usa `autocomplete="current-password"` en lugar de `new-password` | misma plantilla para login y registro |
| LOW | Errores en `<p>` sin `role=alert` / asociación al campo | `_Pagina` |

### `visor.html` — Operate (embedded)

| Severidad | Hallazgo | Evidencia |
|-----------|----------|-----------|
| HIGH (theming) | Fondo/texto fijos `#eef1f4` / `#1c2024`; ignora claro/oscuro del host | `visor.html` styles |
| MEDIUM | Sin controles de cámara ni texto de estado de interacción accesible más allá de errores | script + docs VISOR_3D |

## Findings consolidados (`better-interface`)

Triggers / P0–P1 primero:

| # | Domain | Severity | Problem | Locations | Why | Fix |
|---|--------|----------|---------|-----------|-----|-----|
| 1 | systems / craft | HIGH | Gate de auth rompe el sistema visual del producto | `Autenticacion.py` | Primera impresión y sesión viven fuera de `ortesislab.css` | Reutilizar tokens/layout OrtesisLab en `/auth/*` |
| 2 | theming | HIGH | Visor 3D no hereda tema | `visor.html` | Escenario `--ol-stage` vs iframe gris genérico | Tokens CSS alineados a `--ol-*` / `prefers-color-scheme` o query del host |
| 3 | layout | HIGH | Historial inutilizable en móvil sin estrategia aparte del scroll | `PaginaHistorial.Tabla` | `min_width=960px` demostrado en fuente | Vista cards `<768px` o columnas prioritarias |
| 4 | accessibility | HIGH | Visor sin camino de teclado equivalente al arrastre | `Visor` + `visor.html` + copy | Trigger: pointer-only path | Controles botón (orbit/zoom) o documentación + skip foco iframe |
| 5 | accessibility | MEDIUM | Radiogroup de patrones sin teclado APG | `Mosaico` / `Formulario` | `role=radio` sin flechas | Roving tabindex o `rx.radio` nativo |
| 6 | accessibility | MEDIUM | Hit targets frágiles (ayuda, link «Cambiar archivo») | `Etiqueta`, `Cargador` | 2.5.8 borderline / touch | `min 40×40` con padding / size≥2 |
| 7 | layout | MEDIUM | Sin `<main>` / jerarquía h1 por ruta | `Pagina`, headings size 5/7 | Orientación AT y SR | `main` + un `h1` por página |
| 8 | writing / craft | MEDIUM | Empty states débiles (Historial, Lote sin resultados, escenario vacío) | tres páginas | Tarea sin siguiente paso visible | Empty state con una acción |
| 9 | writing | LOW | Disclaimer de precio/moneda denso y confuso | `Escenario` | Carga cognitiva en CTA | Aclarar moneda o acortar |
| 10 | accessibility | LOW | Registro: autocomplete incorrecto | `Autenticacion._Pagina` | Autofill erróneo | `new-password` en registro |

## Improve first

**Unificar auth + visor con el sistema `--ol-*` (hallazgos 1–2).**  
Es el mayor corte de identidad y theming con el menor riesgo de lógica de negocio: no toca generación ni lotes, y alinea la primera y la última milla visual con Diseño/Lotes/Historial.

## Not verified

- Contraste real en Radix (estilos generados sobre tokens)
- Orden de tab completo y focus trap del diálogo de superficie
- Comportamiento táctil del iframe Three.js
- Zoom 200% / viewport 320px en dispositivo
- Lector de pantalla (NVDA/VoiceOver)

## Referencias de código

- Shell: `apps/web/web/Sesion.py`, `PaginaComparacion.Pagina`
- Diseño: `apps/web/web/PaginaComparacion.py`
- Lotes: `apps/web/web/PaginaLote.py`
- Historial: `apps/web/web/PaginaHistorial.py`
- Auth: `apps/web/web/services/Autenticacion.py`
- Tema: `apps/web/assets/ortesislab.css`
- Visor: `apps/web/assets/visor.html`
- Contrato UX: `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md` (§ UX y accesibilidad observadas)
