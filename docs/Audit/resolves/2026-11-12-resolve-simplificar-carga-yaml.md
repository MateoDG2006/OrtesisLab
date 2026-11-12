# RES-2026-11-12-002 — Lectura directa del YAML en `Cargar`

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Archivos y hallazgos

El inventario de `AUD-2026-10-29-002` registra `web/ConfiguracionBackend.py`
(SHA-256 de línea base `27b5bcd69b094cd4f799360f97064a2fb158e61cbbbbc33d7d1c6852752f28e9`,
hallazgo B-09, revisión pendiente). Ese path ya no está en disco. El mismo
módulo está en `apps/web/web/ConfiguracionBackend.py`.

| Archivo desde la raíz | Hallazgos | SHA-256 anterior | SHA-256 verificada |
|---|---|---|---|
| `apps/web/web/ConfiguracionBackend.py` (continuación de `web/ConfiguracionBackend.py`) | B-09, abierto | `0d6f97729ccdd6c9d66403073da74e5117b7cede4d7d0963a70c4191a39cfa92` | `fca7bd5247449849cc0953a7bddc046c59cb48d8bcb3ba865c46bac772560e49` |

## Autorización para corregir (si había bloqueo)

Instrucción explícita del usuario, 2026-11-12, en el chat, después de
informarle del bloqueo:

> «Lo autorizo»

Alcance autorizado: dejar `ConfiguracionBackend.Cargar` en una sola llamada
a `Path.read_text` sobre `core/config/<area>.yaml`. No se añade validación de
esquema, no se cambian firmas ni llamadores, y no se cierra B-09.

## Decisión y trabajo realizado

`Cargar` ya construye la ruta `CARPETA / f"{area}.yaml"`. El `with`/`open`
solo entrega el texto a `yaml.safe_load`. `Path.read_text` hace esa lectura
y cierra el archivo. Hecho en `apps/web/web/ConfiguracionBackend.py`. B-09
(el `dict` sigue sin esquema) queda pendiente.

## Verificación

Python 3.15 del sistema, sin `.venv`, sin `uv` y sin PyYAML instalable
(no hay rueda para 3.15 y el build exige Cython). No se importó `Cargar`.

Con `pathlib`, `read_text(encoding="utf-8")` y `open(encoding="utf-8").read()`
devolvieron el mismo texto en `core/config/{almacen,cache,persistencia,sesion,trabajador,web}.yaml`.
`core/config/no-existe.yaml` lanzó `FileNotFoundError`.

## Riesgo residual y cierre

B-09 sigue confirmado. El archivo sigue bloqueado para cualquier otro cambio.
