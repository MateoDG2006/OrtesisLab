# RES-2026-11-12-014 — Fase 0: defectos que rompen límites, conciliación y purga

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario el 2026-11-12: «Necesito que resuelvas los conflictos e
implementes las librerías que están redactadas aquí», referida a
`docs/Simplificacion/`. Alcance de este registro: la fase 0 de
`docs/Simplificacion/PLAN_SIMPLIFICACION.md` (defectos D-1 a D-6). No cierra
hallazgos de auditoría. Las fases 1 a 7 siguen sin esta edición.

## Decisión

- **D-1.** Quitar `min_plausible_surface_extent_mm` y
  `max_plausible_surface_extent_mm` de la validación. El JSON ya no las tiene
  desde que se quitó el autoescalado.
- **D-2.** Ya está resuelto en el merge `6d98034`: `PoolPostgres` no llama a
  `ValidarEnArranque`. No se reintroduce el método.
- **D-3.** `ColgadosVencidos` devuelve imports en `received` o `validating`
  más viejos que el plazo del conciliador.
- **D-4.** `CLAVES_SOLO_VOXEL` es `repair` y `resolution_mm`: son los parámetros
  que solo cambian la reconstrucción voxel de Blender.
- **D-5.** La purga corre en el proceso del trabajador
  (`scripts/EjecutarTrabajador.py` abre `worker_database_url`). Se concede
  `DELETE` sobre `history_events` y `auth_sessions` solo a `ortesislab_worker`.
  La aplicación sigue sin `DELETE` en el historial. No se usa el rol migrador:
  ese rol puede cambiar el esquema.
- **D-6.** La revisión `0ea8eb9c0ca2` (login local) ya crea las tablas, los
  `GRANT` y el trigger. Esta fase solo añade la revisión de los `DELETE`.

## Archivos

| Archivo | Tratamiento |
|---|---|
| `apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py` | D-1 |
| `apps/web/web/persistence/repositorios/RepositorioImports.py` | D-3 |
| `apps/web/web/persistence/Contratos.py` | `user_id` en `ImportDTO`, que el conciliador ya lee |
| `apps/web/web/services/ServicioVersiones.py` | D-4 |
| `apps/db/alembic/versions/20261112_1135_purga_trabajador.py` | D-5 |
| `tests/geometria/test_carga_presupuesto.py` | El caso de las claves retiradas |
| `docs/AppBackend/DATABASE.md` | Permisos vigentes |
| `docs/Agents/REGISTRO_CAMBIOS.md` | Evidencia de esta corrección |

## Verificación

- `uv run python -m unittest tests.geometria.test_carga_presupuesto -v`: 5 pruebas, OK.
- Importación de `CLAVES_SOLO_VOXEL` y `ColgadosVencidos`: `simbolos-ok`.
- No se ejecutó `alembic upgrade head` ni la purga contra PostgreSQL.

## Riesgo residual

La revisión `b7c1d4e9a2f0` no está aplicada en la base de desarrollo hasta `make migrar`. Hasta entonces la purga del trabajador sigue fallando por permisos. Los hallazgos de auditoría siguen abiertos. Las fases 1 a 7 del plan de librerías no forman parte de este registro.
