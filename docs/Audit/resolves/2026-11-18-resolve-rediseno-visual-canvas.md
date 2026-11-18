# RES-2026-11-18-001 — Rediseño visual según el canvas «OrtesisLab Rediseño»

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002, ambas **CERRADAS** según
[issue-9](2026-11-12-issue-9-seguimiento.md) e [issue-b-indice](2026-11-12-issue-b-indice.md).
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18:

> «Implement this design in this codebase: https://claude.ai/code/artifact/a551995b-86d4-4f59-a9be-8cd5c19dbdec
> Read the design's files from that link. Match how it looks, using this codebase's own
> components and conventions.»

Alcance: `apps/web/rxconfig.py`, `apps/web/web/OrtesisLabApp.py`, `apps/web/web/Sesion.py`,
`apps/web/web/PaginaComparacion.py`, `apps/web/web/PaginaLote.py`, `apps/web/web/PaginaHistorial.py`,
`apps/web/web/EstadoApp.py` (descarga de la vista y un texto), `apps/web/web/EstadoHistorial.py`
(código de estado en la fila), archivo nuevo `apps/web/assets/ortesislab.css` y la documentación
afectada. No cambia persistencia, trabajador, núcleo, visor ni el complemento Blender.
No cierra hallazgos.

## Verificación

2026-11-18, `.venv`:

- `reflex compile --dry` (en `apps/web`): compiló sin errores.
- `python -m unittest discover -s tests/aplicacion_web -t .`: 18 pruebas, 1 omitida, OK.
- `python docs/Agents/Scripts/GenerarIndices.py --comprobar`: catálogos al día y enlaces correctos.

No se probó en navegador: el servidor de desarrollo del frontend no abrió puerto en este
entorno. Tampoco con PostgreSQL, trabajador y bucket.
