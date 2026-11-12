# RES-2026-11-12-010 — El módulo Reflex se llama `OrtesisLabApp`

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002. `web/GenerateModelsApp.py` figura en ambos inventarios.
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

`rxconfig.py` ya declara `app_module_import="web.OrtesisLabApp"`. Al arrancar, Reflex respondió:

> Module web.OrtesisLabApp not found. Ensure app_module_import='web.OrtesisLabApp' in rxconfig.py matches your folder structure.

Alcance autorizado: renombrar `apps/web/web/GenerateModelsApp.py` a `OrtesisLabApp.py` y las citas vigentes de ese módulo. No se cierra ningún hallazgo. No se toca el ZIP ni `OrtesisLabPlugin`.

## Decisión

El archivo sigue siendo la aplicación Reflex. Solo cambia el nombre del módulo para coincidir con `rxconfig.py`.

## Verificación

- `uv run --directory apps/web python -c "import rxconfig; import web.OrtesisLabApp"` terminó en 0.
- `python docs/Agents/Scripts/GenerarIndices.py --comprobar`: catálogos al día y enlaces correctos.

No se arrancó Reflex en el navegador.
