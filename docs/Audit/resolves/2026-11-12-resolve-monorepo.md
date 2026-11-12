# RES-2026-11-12-001 — Reubicar el repositorio como monorepo

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12:

> «Necesito que movamos la infra a un monorepo, en donde tengamos una carpeta llamada apps y ahi dentro tengamos web que incluye backend y frontend con reflex, db que va a incluir la PostgreSQL y la redis y otro llamado ortesis-plugin que es donde va a estar todo el plugin de blender. Y todo lo que sea configs o cosas que se compartan entre las 3 vayan en otra carpeta aparte llamada core»

Alcance autorizado: reubicar carpetas y ajustar las rutas que dejan de resolver. No cambia la geometría, el esquema ni las firmas. Los hallazgos de ambas auditorías siguen abiertos.

## Destino

| Origen | Destino |
|---|---|
| `web/`, `rxconfig.py`, `assets/`, `reflex.lock/` | `apps/web/` (el paquete Python sigue llamándose `web`) |
| `infra/database/` y `db/` | `apps/db/` (PostgreSQL, Redis, y el Compose que ya trae MinIO y el OIDC de pruebas) |
| `GenerateModelsApp/` y su ZIP | `apps/ortesis-plugin/` |
| `config/*.yaml` y los JSON de `GenerateModelsApp/config/` | `core/config/` |

## Decisión

El paquete `GenerateModelsApp` no se parte: Blender lo instala como una carpeta y la web importa ese núcleo. Los JSON compartidos viven en `core/config`; el empaquetado los copia dentro del ZIP para que el complemento siga leyéndolos a su lado.

## Verificación

Se completa en el registro de cambios de esta entrega.
