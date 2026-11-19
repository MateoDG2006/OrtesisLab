# Landmarks y jerarquía de títulos

Written against: `0965184`

## Evidence chain

- Surface: shell compartido + `/`, `/lote`, `/historial`
- Problem: no hay `<main>`; títulos de sección `heading size="5|7"` sin un `h1` de página; marca es texto
- Design evidence: títulos de documento ya existen (`OrtesisLabApp` `title=…`); nav ya es `<nav aria-label="Secciones">`
- Owner: `PaginaComparacion.Pagina`, headers de cada página
- Scope: estructura semántica, no layout visual mayor
- Uncertainty: nivel exacto que Reflex asigna a `rx.heading size="5"` — verificar HTML compilado

## Design decision

Envolver el contenido de página (bajo la barra) en `<main>` y añadir un `h1` visually consistent (puede ser `sr-only` o título visible corto) por ruta: «Diseño», «Lotes», «Historial».

## Reuse

- `PaginaComparacion.Pagina` como único shell
- Exemplar: `Sesion` nav landmark

## Changes

1. `PaginaComparacion.Pagina`
   - Change: aceptar título de página; render `rx.el.main` alrededor de `*contenido`
   - Preserve: padding, fondo, barra
2. `Index` de cada página
   - Change: pasar `h1` adecuado; bajar headings internos un nivel si el HTML compilado salta niveles
   - Verify: un `h1` y un `main` por vista

## Scope

- Inherit: las tres rutas
- Exclude: auth HTML (plan 01)

## Validation

- Accessibility tree: `main` + `h1`
- Visual: sin romper wrap existente

## Stop conditions

- Stop if Reflex no permite `main` sin romper layout — documentar y usar `role="main"`.

## Design documentation

- Mencionar landmarks en `COMPONENTES_Y_FLUJOS.md`.
