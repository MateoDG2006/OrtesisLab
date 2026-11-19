# RES-2026-11-18-SHELL — Refactor de shell UI (navbar, panel, tipografía, iconos)

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18:

> «Hay que refactorizar la interfaz, quitar los controles de acercamiento…
> navbar… panel lateral… tipografía… iconos de una librería…»

Alcance autorizado (no cierra hallazgos A/B históricos):

- `apps/web/web/Sesion.py` — navbar
- `apps/web/web/PaginaComparacion.py` — shell Diseño, panel, mosaicos
- `apps/web/assets/ortesislab.css` — márgenes, tipografía, layout
- `apps/web/assets/visor/controles.js` (+ `visor.css`) — quitar Acercar/Alejar
- Docs AppFrontend / DESIGN / REGISTRO / índices

## Decisión

`RESUELTO` — shell Operate con navbar, workspace full-height y aside 440px,
escala tipográfica Manrope, iconos Lucide en patrones, zoom del visor solo por
rueda/teclado.

## Evidencia

- `reflex compile --dry`: OK
- `unittest` aplicacion_web: 18 OK (1 omitida)
- Imagen `ortesislab-web` reconstruida; `GET /` → 200
