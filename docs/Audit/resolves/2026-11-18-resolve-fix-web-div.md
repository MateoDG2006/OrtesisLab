# RES-2026-11-18-WEB — Fallo del contenedor web (`div is not defined`)

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18:

> «El contenedor de web esta fallaod»

Alcance: corregir `_GrupoTeclado` / export prerender en `PaginaComparacion.py`
(y docs/registro si aplica). No cierra hallazgos A/B históricos.

## Hallazgo

`_GrupoTeclado(rx.Component)` con `tag = "div"` emitía `jsx(div, …)` (identificador
sin comillas). En el prerender/export de producción eso provocaba
`ReferenceError: div is not defined`, el script `export` salía con código 1 y el
contenedor `ortesislab-web-1` entraba en bucle de reinicio.

## Decisión

`RESUELTO` — `_GrupoTeclado` pasa a subclase de
`reflex_components_core.el.elements.typography.Div` y solo añade el trigger
`on_key_down`. Así el JSX generado usa `jsx("div", …)`.

## Archivos

| Archivo | Acción |
|---|---|
| `apps/web/web/PaginaComparacion.py` | `_GrupoTeclado(Div)` |
| `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md` | Nota del contrato correcto |
| `docs/Agents/REGISTRO_CAMBIOS.md` | Entrada de esta corrección |

## Evidencia

- `reflex compile --dry` en `apps/web`: OK.
- Contenedor `ortesislab-web-1`: código con `class _GrupoTeclado(Div)`; logs
  «App running at: http://0.0.0.0:3000/»; `GET http://127.0.0.1:3000/` → 200
  sin `div is not defined` / `Unexpected Server Error`.
