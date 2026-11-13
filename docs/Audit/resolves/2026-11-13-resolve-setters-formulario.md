# RES-2026-11-13-003 — Setters del formulario

Fecha: 2026-11-13 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por el fallo de compilación que pegó el usuario

## Autorización para corregir

El usuario pegó el traceback de `make web`: `AttributeError: type object
'EstadoApp' has no attribute 'set_pattern'`. Alcance: volver a registrar los
`set_*` que usan las páginas. No cierra hallazgos. No cambia qué campos se
pueden editar.

## Decisión

Esta versión de Reflex no genera `set_*` (`state_auto_setters` vale False y el
ajuste se retira). `EstadoApp` y `EstadoHistorial` registran un setter solo
para los campos que el formulario ya enlazaba.
