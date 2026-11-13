# RES-2026-11-13-002 — Sin tope de variantes por lote

Fecha: 2026-11-13 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario el 2026-11-13: «Elimina el limite de items que se pueden
hacer en una sola bacha». Alcance: quitar el máximo de variantes de un lote.
No cierra hallazgos. Sigue el tope de lotes pendientes y el de vistas comparadas.

## Decisión

`lotes.maximo_items` deja de existir. `Combinaciones` y `ServicioLotes.Solicitar`
ya no rechazan un lote por cantidad. El `CHECK` de `generation_batches.total_items`
pasa a `total_items >= 1`. Un lote vacío sigue siendo un error.
