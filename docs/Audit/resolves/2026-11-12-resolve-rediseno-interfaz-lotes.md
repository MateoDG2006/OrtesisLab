# RES-2026-11-12-011 — Rediseño de la interfaz web: parámetros, lotes y progreso

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002, ambas **CERRADAS** según
[issue-9](2026-11-12-issue-9-seguimiento.md) e [issue-b-indice](2026-11-12-issue-b-indice.md).
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-12:

> «Necesito que hagamos un rediseño de la interfaz actual de la web para incorporar
> mejores mecanismos para crear las bachas de modelos masivos y mejores formas para
> configurar los parametros, como puede ser colocando parametros genericos y colocando
> un checkbox para los avanzados, colocar un hint que explique para que sirve cada
> parametro y una interfaz exclusiva para ver el progreso de las bachas con imagenes
> de preview de cada ortesis»

Alcance: `apps/web/web/EstadoApp.py`, `apps/web/web/PaginaComparacion.py`,
`apps/web/web/OrtesisLabApp.py`, `apps/web/web/Sesion.py`, `apps/web/web/EstadoHistorial.py`
(solo el destino de la redirección tras Restaurar/Reintentar), `apps/web/assets/visor.html`,
`core/config/web.yaml`, archivos nuevos `apps/web/web/PaginaLote.py` y
`tests/aplicacion_web/test_estado_lote.py`, y la documentación afectada. No se cambian
persistencia, trabajador, núcleo ni el complemento Blender. No cierra hallazgos.

## Verificación

2026-11-12, `.venv`:

- `python -m unittest tests.aplicacion_web.test_estado_lote -v`: 2 OK.
- `python -m unittest tests.aplicacion_web.test_generador_web tests.aplicacion_web.test_humo_import`:
  3 errores en `LectorSuperficie.Preparar`, idénticos sin estos cambios (`git stash`).
- `reflex compile --dry` (en `apps/web`): compiló sin errores.
- `python docs/Agents/Scripts/GenerarIndices.py --comprobar`: catálogos al día y enlaces correctos.

No se probó en navegador ni con PostgreSQL, trabajador y bucket.
