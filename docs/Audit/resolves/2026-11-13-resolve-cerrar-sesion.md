# RES-2026-11-13-004 — Cerrar sesión

Fecha: 2026-11-13 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario el 2026-11-13: «El boton de cerrar sesion no funciona».
Alcance: el botón de la barra. No cierra hallazgos.

## Decisión

`rx.el.form` llama a `preventDefault` en el submit, así que el POST no sale.
Cerrar sesión usa un `<form>` HTML con `method="post"`.
