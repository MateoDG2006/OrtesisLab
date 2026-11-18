# RES-2026-11-18-001 — Docker de producción

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucciones del usuario el 2026-11-18: «Necesito que crees un dockerfile
para levantar esta infraestructura automaticamente» y «Para la A y para el
entorno de produccion». Alcance: empaquetar la pila (Postgres, MinIO, Redis,
migraciones, web, trabajador y Caddy HTTPS) y documentar el arranque. No
cierra hallazgos. No sustituye `make up` local.

## Decisión

Se añade `Dockerfile`, `compose.prod.yaml`, `deploy/` y
`scripts/EntradaContenedor.py`. Se actualizan `README.md`, `Makefile` y
`docs/AppBackend/OPERACION_Y_PRUEBAS.md` para el comando de producción.
