# RES-2026-11-18-LOTES-N — Lotes con N características variables

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario (plan aprobado), 2026-11-18:

> «Los lotes no me dejan colocar n cantidad de caracteristicas para variar»
> + confirmación del plan «Lotes con N características variables»

Alcance: `GeneradorWeb.Combinaciones`, `EstadoApp` (barridos), `PaginaLote`,
tests `test_generador_web`, docs AppFrontend/AppBackend/REGISTRO/índices.
No cierra hallazgos A/B históricos.

## Decisión

`RESUELTO` — producto cartesiano de N barridos `{clave, desde, hasta, paso}` ×
patrones × liner; UI multi-fila en «Nuevo lote».

## Evidencia

- `reflex compile --dry`: OK
- `unittest tests.aplicacion_web.test_generador_web`: 14 OK (1 omitida)
