# RES-2026-11-12-003 — Cargar el .env de la raíz con python-dotenv

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-29-002 (el archivo estaba en `web/Ajustes.py`; [RES-2026-11-12-001](2026-11-12-resolve-monorepo.md) lo dejó en `apps/web/web/Ajustes.py`)
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario, 2026-11-12, sobre el lector de `.env`, y la opción
elegida a continuación:

> «Estas funciones son innecesarias si ya sabemos donde se va a ubicar el env»

Opción autorizada: quitar `_LeerArchivo` y usar `load_dotenv` sobre el `.env`
de la raíz. El entorno del proceso sigue ganando. Los valores del archivo
pasan a `os.environ` y dotenv sustituye referencias `$`. La misma autorización
cubre la prosa de `docs/AppBackend/MODULOS.md`,
`docs/AppBackend/OPERACION_Y_PRUEBAS.md` y `docs/AppBackend/ARQUITECTURA.md`.
El registro y `SIMBOLOS.md` se actualizan porque este cambio borra un método:
no cierran hallazgos.

No cierra la revisión de `AUD-2026-10-29-002`. B-01, B-02 y B-17 siguen
abiertos. El archivo sigue bloqueado para cualquier otro cambio.

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | SHA-256 anterior | SHA-256 verificada |
|---|---|---|---|
| `apps/web/web/Ajustes.py` | Revisión pendiente, sin hallazgo individual | no medida: el archivo cambió en la misma sesión antes de esta edición | `1bc9475b50d89ba5d4344a1c955ec49c6ccbc945c799c154bfb87cbc92f17198` |
| `docs/AppBackend/MODULOS.md` | B-17 | no medida | `4353132cb870245f36fa664839442deb869c30d4ef73503f2b2dab2475155e26` |
| `docs/AppBackend/OPERACION_Y_PRUEBAS.md` | B-02, B-17 | no medida | `3d73b2071fb912588e314449f8717ae7c0d0baa53c9f762b2f4f55d1f8cad611` |
| `docs/AppBackend/ARQUITECTURA.md` | Revisión pendiente, sin hallazgo individual | no medida | `221fc8c1c487986114bbded501a3aa061ca2c80534fb7153f0c6407d9dc42c2d` |
| `docs/Agents/REGISTRO_CAMBIOS.md` | B-01 | no medida | `66f428f41983ac2de4df835b4a805d58100e2a4b875232f66ce4894925ae6b9d` |
| `docs/AppBackend/SIMBOLOS.md` | B-17 | no medida | `2b570db2826beb695741fa868caecb6fd01993fbcf645c2fd79862dab4d89d43` |
| `docs/Agents/INVENTARIO.md` | B-17 | no medida | `14d0445997b3c2fcacbe4d5c91e1b2b9bfe9487865cd6d5ba6fb037b2a83937c` |
| `docs/BlenderPlugin/SIMBOLOS.md` | Revisión pendiente, sin hallazgo individual | no medida | `0eaa5edb1c84e48790e5ed0e00e2ce94d587b6dcc14e0821d801bcd071fa7f0e` |

## Decisión

`Cargar()` conoce la ruta (`RAIZ / ".env"`, cuatro niveles sobre este archivo).
Se elimina el parser propio. `load_dotenv` con `override=False` y
`encoding="utf-8-sig"` vuelca ese archivo al entorno del proceso y `Cargar`
guarda una copia. Una variable ya definida no se pisa. La primera llamada
sigue cacheada.

## Verificación

python-dotenv 1.2.4, instalado en un directorio temporal porque esta sesión
no tiene `.venv` ni `uv`. No se imprimieron valores de configuración.

- Con BOM, una variable ya definida en el proceso se conserva, una clave nueva
  entra, `${NUEVA}` se sustituye y el nombre no incluye el BOM.
- No había `.env` en la raíz. Se creó uno de prueba: `Cargar()` leyó la clave
  del archivo, conservó la del proceso y el archivo se borró. Al terminar,
  `.env` no estaba.
- `py -3 docs/Agents/Scripts/GenerarIndices.py` reescribió los catálogos. Una
  comprobación seguida marcó otra vez `docs/AppBackend/SIMBOLOS.md`: las
  líneas de `CacheRedis`, `Contratos` y `TrabajadorGeneracion` cambiaron
  mientras se medía. La ficha de `Ajustes` ya no incluye `_LeerArchivo`.

No se arrancó Reflex, el trabajador ni PostgreSQL.

## Riesgo residual y cierre

Los hallazgos citados siguen abiertos. Estos archivos siguen bloqueados para
cualquier cambio distinto del descrito aquí. `python-dotenv` no está declarado
en `apps/web`: entra en el entorno porque Reflex ya lo trae.
