# RES-2026-11-18-UI — Roadmap de mejora UI

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002 (cerradas en hallazgos A/B;
este resolve autoriza edición de archivos de inventario para la mejora UI).
Estado: RESUELTO (alcance UI del roadmap; no cierra hallazgos A/B históricos)
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18:

> «Implementa el roadmap de mejora de la UI»

Alcance (según `design-plans/00-ROADMAP_MEJORA_UI.md`):

- `apps/web/web/services/Autenticacion.py`
- `apps/web/assets/visor.html`
- `apps/web/assets/ortesislab.css`
- `apps/web/web/PaginaComparacion.py` (incl. `_GrupoTeclado`, `EstadoApp.TeclaPatron`)
- `apps/web/web/PaginaLote.py`
- `apps/web/web/PaginaHistorial.py`
- `apps/web/web/EstadoApp.py` (`TeclaPatron`)
- documentación `docs/AppFrontend/*`, `docs/Agents/REGISTRO_CAMBIOS.md`, `DESIGN.md`

No cambia persistencia, trabajador, núcleo Blender ni contratos de generación.

## Verificación

2026-11-18:

- `reflex compile --dry` (en `apps/web`): OK.
- `python -m unittest discover -s tests/aplicacion_web -t .`: 18 pruebas, 1 omitida, OK.
- HTML de auth: Manrope, card `--ol-*`, `new-password` en registro.
- Navegador: no ejercido en esta sesión.
