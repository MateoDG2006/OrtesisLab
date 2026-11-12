# RES-2026-11-12-012 — Login y registro locales

| Campo | Valor |
|---|---|
| Resolución | RES-2026-11-12-012 |
| Auditoría | AUD-2026-10-13-001 y auditorías que incluyen estos archivos |
| Estado | EN_CURSO |
| Fecha | 2026-11-12 |
| Responsable | implementación pedida en el chat |

## Autorización

El usuario pidió: «Refactoricemos el mecanismo para incorporar un login simple y un register simple», y después: «Elimina toda la logica vieja de registro y login y remplazalo por un sistema mas simple de usuario contraseña almacenado en la base de datos».

Esas frases autorizan quitar el proveedor OIDC y el alta por `iss`/`sub`, y dejar usuario y contraseña en PostgreSQL. No cierran hallazgos.

## Alcance

- `apps/web/web/services/AutenticacionOidc.py` se sustituye por `Autenticacion.py`
- `apps/web/web/services/ContextoUsuario.py`
- `apps/web/web/persistence/Modelos.py` (`password_hash`)
- `apps/web/web/persistence/repositorios/RepositorioUsuarios.py`
- `apps/web/web/Sesion.py`
- `apps/web/web/Ajustes.py`
- `apps/web/web/OrtesisLabApp.py`
- `core/config/sesion.yaml`
- `.env.example`
- `pyproject.toml` (dependencia `authlib`)
- `apps/db/compose.yaml` y `scripts/BaseLocal.py` (proveedor OIDC de pruebas)
- `scripts/MigrarSubidas.py` y las pruebas que creaban cuentas por emisor y sujeto
- Documentación de arquitectura, módulos y operación que describe el login vigente
- Revisión Alembic del esquema, si la base del migrador responde

## Fuera de alcance

No se cierran hallazgos. No se reescriben informes históricos.
