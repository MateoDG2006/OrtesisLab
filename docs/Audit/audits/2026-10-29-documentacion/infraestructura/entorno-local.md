# Infraestructura · Entorno local, base de datos y operación

**Estado:** propuesta. **Archivos:** `infra/database/**`, `Makefile`, `alembic.ini`,
`db/**`, `.env.example`, `infra/database/.env.example`, `scripts/*.py`,
`.github/**`.

## Servicios de Compose (`infra/database/compose.yaml`, proyecto `ortesislab-db`)

| Servicio | Imagen | Puerto (solo 127.0.0.1) | Volumen | Perfil | Salud |
|---|---|---|---|---|---|
| `postgres` | `postgres:17-bookworm` | 5433 → 5432 | `postgres-data`; `./init`, `db/seeds` y `./backups` montados | — | `pg_isready` cada 5 s |
| `minio` | `minio/minio:RELEASE.2025-09-07T16-13-09Z` (`MINIO_IMAGE`) | 9000 (API), 9001 (consola) | `minio-data` | — | `mc ready local` |
| `minio-init` | `minio/mc:RELEASE.2025-08-13T08-35-41Z` | — | `./minio:/config` | `init` | — |
| `redis` | `redis:7.4-alpine`, sin persistencia, `maxmemory 256mb` (`ORTESISLAB_REDIS_MAXMEMORY`), `allkeys-lru` | 6379 | — | — | `redis-cli ping` |
| `mc` | `minio/mc` | — | `./backups` | `tools` | — |
| `oidc` | `ghcr.io/navikt/mock-oauth2-server:2.2.1` | `ORTESISLAB_OIDC_PORT` (8080) | — | `auth-dev` | — |

Variables obligatorias de `infra/database/.env`:

- PostgreSQL: `POSTGRES_USER`, `POSTGRES_PASSWORD` y
  `ORTESISLAB_{MIGRATOR,APP,WORKER,BACKUP}_PASSWORD`.
- MinIO: `MINIO_ROOT_USER` y `MINIO_ROOT_PASSWORD`.
- Cuenta de servicio S3 (solo `init`): `ORTESISLAB_S3_ACCESS_KEY` y
  `ORTESISLAB_S3_SECRET_KEY`.

## Roles PostgreSQL (`infra/database/init/01_roles.sh`, solo con volumen nuevo)

| Rol | Permisos creados por el script | `search_path` | `statement_timeout` |
|---|---|---|---|
| `ortesislab_migrator` | `CONNECT`, `TEMPORARY`; dueño del esquema `ortesislab` | `ortesislab` | — |
| `ortesislab_app` | `CONNECT`, `TEMPORARY`; `USAGE` del esquema. **Sin `GRANT` de tablas** hasta que exista la migración (B-02) | ídem | 15 s |
| `ortesislab_worker` | ídem | ídem | 15 s |
| `ortesislab_backup` | `pg_read_all_data` | ídem | — |

`REVOKE ALL ON DATABASE … FROM PUBLIC` y `REVOKE CREATE ON SCHEMA public`.
`db/test/preparar_base.sql` repite permisos y esquema en otra base (sin roles).

`statement_timeout` de 15 s afecta a la web y al trabajador. Una consulta de
historial o de progreso que lo supere falla con `OperationalError` y llega
como `PersistenciaNoDisponible`.

## Migraciones (Alembic 1.20)

- `alembic.ini` → `db/alembic/env.py`.
- **`db/alembic/versions/` está vacío** (B-02).
- `env.py`:
  - URL del migrador, o la de pruebas con `-x base=test`;
  - `SET search_path TO ortesislab`;
  - `version_table_schema=ortesislab` e ignora `alembic_version`;
  - `compare_type` y `compare_server_default`;
  - solo funciona en línea: no admite `--sql`.

Lo que la primera revisión debe escribir a mano (SQL en
`docs/AppBackend/DATABASE.md` §12):

- la función y el trigger `model_versions_comprobar`;
- los `GRANT` de los roles app y worker;
- la FK `batch_items_winning_attempt_fk` después de `generation_attempts`.

`alembic check` no compara `GRANT` ni triggers.

## Objetivos del Makefile

| Objetivo | Efecto | Salvaguarda |
|---|---|---|
| `db-help` (por defecto) | Lista los objetivos | — |
| `db-config` | `compose config --quiet` | — |
| `db-up` | `up -d --wait postgres minio redis` | — |
| `db-init-s3` | `run --rm minio-init` | Idempotente; `attach` con `\|\| true` |
| `db-stop`, `db-down`, `db-logs` | Ciclo de vida | `down` conserva los volúmenes |
| `db-health`, `s3-health`, `redis-health` | Comprobaciones | — |
| `db-seed` | `development.sql` como migrador | Solo `ortesislab_dev`; el SQL exige que el esquema exista |
| `db-shell` | `psql` como migrador | — |
| `db-backup FILE=x.dump` | `pg_dump -Fc -n ortesislab` como `ortesislab_backup` | Nombre en lista blanca; no sobrescribe |
| `db-restore FILE=x.dump CONFIRM=RESTAURAR` | `pg_restore --clean --single-transaction` | Solo dev, con confirmación; **no restaura objetos** |
| `s3-backup` / `s3-restore CONFIRM=RESTAURAR` | `mc mirror` del bucket a `backups/objetos` y vuelta | El restore exige confirmación |
| `db-drop CONFIRM=ELIMINAR` / `db-destroy CONFIRM=ELIMINAR` | Borra la base o los volúmenes | Confirmación |
| `db-test-reset` | Recrea `ortesislab_test` vacía | Sin confirmación (base desechable) |
| `auth-dev-up` / `auth-dev-down` | Proveedor OIDC de pruebas | — |

Un respaldo consistente requiere `db-backup` y `s3-backup` juntos y sin
escrituras. No hay ningún mecanismo que lo garantice.

## Scripts

| Script | Uso | Estado en `e56df68` |
|---|---|---|
| `scripts/EjecutarTrabajador.py [--una-vez]` | Proceso trabajador | **Falla al importar** (B-01) |
| `scripts/MigrarSubidas.py [--simular]` | Traslada `uploaded_files/` al bucket con el usuario semilla `subidas-locales-previas` | **Falla al importar** (B-01) |
| `scripts/EmpaquetarBlender.py` | Regenera `GenerateModelsApp.zip` | Funcional; el ZIP versionado está desactualizado (B-16) |
| `scripts/EjecutarOrtesisLab.py` | `register()` dentro de Blender desde el repositorio | No ejecutado |
| `scripts/IniciarConsola.py`, `src/generatemodelsapp/__init__.py` | Saludo de plantilla | Sin función de producto (B-18) |

## Automatización en GitHub

| Archivo | Disparador | Qué hace |
|---|---|---|
| `.github/workflows/notion-to-issues.yml` | Manual y diario (13:17 UTC) | Python 3.12, `notion_sync_issues.py` con `NOTION_TOKEN` (secreto) y los ids de base y proyecto fijos. Permisos `issues: write` y `contents: read`; concurrencia `notion-sync` |
| `.github/scripts/notion_sync_issues.py` | — | Consulta las tareas sin «GitHub Issue» → crea la issue → escribe la URL en Notion. `DRY_RUN=1` no escribe. No es atómico (B-21) |

No hay CI de pruebas (B-03), ni despliegue, imágenes de aplicación, TLS,
monitorización, alertas o métricas. Los logs van a consola y a
`GenerateModelsApp/logs/ortesislab.log`, sin rotación configurada.

## Arranque desde cero (procedimiento actual y dónde se rompe)

1. `uv python install 3.14 && uv sync --locked`.
2. Copiar los `.env.example` y completarlos.
3. `make db-up && make db-init-s3`.
4. **Escribir la revisión inicial de Alembic** y aplicarla
   (`uv run alembic upgrade head`). Hoy no se puede hacer sin escribir código (B-02).
5. `make auth-dev-up`.
6. `uv run python scripts/EjecutarTrabajador.py`. **Falla** (B-01).
7. `uv run reflex run`. **Falla** (B-01).
