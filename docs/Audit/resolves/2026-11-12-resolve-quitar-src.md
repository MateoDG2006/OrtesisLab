# RES-2026-11-12-009 — Quitar la carpeta `src`

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002. `src/generatemodelsapp/__init__.py` figura en ambos inventarios (hallazgo B-18 en la segunda). `pyproject.toml` también está en esos inventarios.
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12:

> «Elimina esa carpeta de src»

Alcance autorizado: borrar `src/` y el punto de entrada `generatemodelsapp` que solo llamaba a ese paquete. El saludo sigue en `OrtesisLabPlugin/consola.py`, lanzado por `scripts/IniciarConsola.py`. El proyecto deja de empaquetarse a sí mismo para que `uv run` siga instalando dependencias. No se cierran hallazgos.

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | Decisión |
|---|---|---|
| `src/generatemodelsapp/__init__.py` | B-18 y revisión del inventario inicial | Eliminar el archivo y la carpeta |
| `pyproject.toml` | Inventario de ambas auditorías | Quitar el script `generatemodelsapp` y declarar `package = false` |
| Documentación que enlazaba `src/` | B-17 donde aplique | Quitar la ficha y la fila de carpeta |

## Decisión

Esa carpeta no contenía geometría ni la aplicación Reflex: solo añadía el complemento a `sys.path` y llamaba `OrtesisLabPlugin.consola.main`. B-18 sigue abierto.

## Verificación

- La carpeta `src` ya no está en disco.
- `uv run python -c "print('uv-ok')"` terminó en 0.
- `python docs/Agents/Scripts/GenerarIndices.py --comprobar`: catálogos al día y enlaces correctos.

No se ejecutó unittest ni Reflex.

## Riesgo residual y cierre

Los archivos que permanecen siguen bloqueados para cualquier otro cambio. El comando instalado `generatemodelsapp` deja de existir.
