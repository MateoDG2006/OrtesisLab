# RES-2026-11-12-015 — SELECT de sesiones para el trabajador

| Campo | Valor |
|---|---|
| Resolución | RES-2026-11-12-015 |
| Auditoría | Auditorías que incluyen `docs/AppBackend/DATABASE.md` |
| Estado | EN_CURSO |
| Fecha | 2026-11-12 |
| Responsable | implementación pedida en el chat |

## Autorización

El usuario arrancó el trabajador y PostgreSQL respondió `permission denied for table auth_sessions` en el `DELETE` de sesiones vencidas.

Esa traza autoriza conceder al rol `ortesislab_worker` el `SELECT` que esa sentencia necesita sobre `auth_sessions`, y documentarlo. No cierra hallazgos.

## Alcance

- Nueva revisión Alembic que concede `SELECT` sobre `ortesislab.auth_sessions` a `ortesislab_worker`
- La línea de permisos vigente en `docs/AppBackend/DATABASE.md`

## Fuera de alcance

La aplicación sigue sin `DELETE`. No se cierran hallazgos.
