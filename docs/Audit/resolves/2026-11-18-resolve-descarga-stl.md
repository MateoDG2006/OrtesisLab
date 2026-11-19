# RES-2026-11-18-004 — Descarga de STL

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por el fallo de descarga

## Autorización para corregir

Instrucción del usuario: «Cuando vas a descargar la descarga falla». El log
muestra `ValueError: The URL argument should start with a /` en `rx.download`.
Alcance: `EstadoApp.Descargar` y `EstadoHistorial.Descargar`. No cierra hallazgos.

## Decisión

Reflex 0.9 no acepta URL absolutas en `rx.download(url=…)`. Tras registrar la
descarga se leen los bytes del bucket y se envían con `rx.download(data=…)`.
