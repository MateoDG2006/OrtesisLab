# RES-2026-11-18-HTML — Extraer HTML a plantillas y módulos del visor

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002 (cerradas en hallazgos;
autoriza edición de archivos de inventario para este refactor).
Estado: RESUELTO (alcance refactor HTML; no cierra hallazgos A/B históricos)
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18:

> «Explota los HTML en componentes y compostables reutilizables del visor y veo
> que hay HTML hardcodeado en archivos de python»

Alcance:

- `apps/web/assets/auth/auth.html`, `auth.css`
- `apps/web/web/services/PlantillaAuth.py`
- `apps/web/web/services/Autenticacion.py` (sin HTML embebido)
- `apps/web/assets/visor.html` + `apps/web/assets/visor/*`
- docs AppFrontend / REGISTRO / inventario

No cambia contratos de generación, persistencia ni Blender.

## Verificación

- `PlantillaAuth` OK; `reflex compile --dry` OK; unittest aplicacion_web 18 OK (1 omitida).
