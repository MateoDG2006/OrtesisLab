# Historial usable en viewports estrechos

Written against: `0965184`

## Evidence chain

- Surface: `/historial` tabla
- Problem: `min_width="960px"` obliga scroll horizontal; sin empty state
- Design evidence: docs ya advierten desbordes; Lotes ya usa cards `minmax(240px)`
- Owner: `PaginaHistorial.Tabla` / `Fila`
- Scope: presentación Historial
- Uncertainty: prioridad de columnas para ortesis (Versión, Fecha, Patrón, Estado, acciones)

## Design decision

Mantener tabla en ≥768px. Bajo 768px, renderizar lista de cards (patrón Lotes/Comparación) con los campos clave y las mismas acciones. Añadir empty state cuando no hay filas.

## Reuse

- `ol-card`, badges `ol-b-*`, `PaginaHistorial.Accion`, métricas `Medida`
- Exemplar: `PaginaLote.Tarjeta`

## Changes

1. `PaginaHistorial.Tabla`
   - Change: rama responsive (CSS class o `rx.desktop_only` / media via class); tabla conserva `overflow_x` en desktop
   - Preserve: filtros, paginación, selección Comparar
2. Empty state
   - Change: si `filas.length()==0`, mensaje + CTA «Ir a Diseño» o «Quitar filtros»
3. Header acciones
   - Change: `column_header_cell("Acciones")` en vez de `""`

## Scope

- Inherit: solo Historial
- Exclude: virtualización de miles de filas

## Validation

- Interface: 360, 768, 1280; filtrar a cero resultados; Comparar 2–3 en mobile cards
- Product: Restaurar/Reintentar/Descargar siguen igual

## Stop conditions

- Stop if se exige paridad pixel-perfect con tabla en móvil (entonces solo columnas prioritarias + scroll).

## Design documentation

- Actualizar § `/historial` en `COMPONENTES_Y_FLUJOS.md`.
