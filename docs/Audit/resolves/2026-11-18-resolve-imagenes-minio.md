# RES-2026-11-18-002 — Imágenes MinIO públicas

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por el fallo de `make prod`

## Autorización para corregir

El usuario pegó el error de Docker: pull denegado de `minio/mc` y
`minio/minio`. MinIO dejó de publicar esas imágenes. Alcance: defaults de
Compose a forks públicos (`pgsty/silo`, `pgsty/mc`). No cierra hallazgos.

## Decisión

`MINIO_IMAGE` por defecto es `pgsty/silo:RELEASE.2026-11-12T00-00-00Z`.
`MC_IMAGE` por defecto es `pgsty/mc:RELEASE.2026-11-12T00-00-00Z`.
`inicializar.sh` deja de usar `sed` (no está en `pgsty/mc`) y sustituye
`__BUCKET__` con bash.
