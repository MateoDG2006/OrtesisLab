# Empty states con una acción

Written against: `0965184`

## Evidence chain

- Surface: escenario vacío `/`; lote sin resultados; historial sin filas
- Problem: texto pasivo o silencio; usuario sin siguiente paso
- Design evidence: copy actual «La malla aparece aquí…»; «Sin lote abierto»
- Owner: `Escenario`, `PaginaLote.Index`/`Cabecera`, `PaginaHistorial.Tabla`
- Scope: UI vacía solamente

## Design decision

Cada empty state muestra: qué falta + **una** acción primaria (cargar superficie / previsualizar / crear lote / ir a diseño / limpiar filtros).

## Reuse

- Tipografía `ol-muted`, botones radius full existentes
- Exemplar tono: `Cabecera` «Sin lote abierto»

## Changes

1. `Escenario` sin archivo: CTA secundaria «Elegir superficie» (abre diálogo) además del texto
2. `/lote` sin `resultados` y sin lote: bloque en la cuadrícula, no solo heading
3. Historial vacío: ver plan 04

## Validation

- Usuario nuevo ve un camino claro en cada ruta

## Stop conditions

- Stop if producto prefiere empty states ilustrados (requiere assets).

## Design documentation

- Ninguna hasta implementar; luego una línea en flujos UX.
