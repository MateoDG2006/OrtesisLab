# RES-2026-11-12-013 — Resolver el merge entre `/lote` y el login local

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario el 2026-11-12: «Necesito que resuelvas los conflictos e
implementes las librerías que están redactadas aquí». Alcance de este registro:
los ocho archivos en conflicto del merge `4ec9585` (login local) sobre
`2cddb8f` (página `/lote`). No cierra hallazgos. La implementación de
librerías queda en un registro aparte y no empieza hasta dejar este merge
resuelto.

## Decisión

Conservar las dos historias. El código ya fusionado tiene página `/lote`,
ayudas en `web.yaml`, login con usuario y contraseña, y no llama a
`ValidarEnArranque` ni a OIDC. La prosa debe describir ese resultado.

## Archivos

| Archivo | Tratamiento |
|---|---|
| `docs/Agents/REGISTRO_CAMBIOS.md` | Las dos entradas del 2026-11-12 |
| `docs/Agents/INVENTARIO.md` | Filas del rediseño y del login |
| `docs/AppBackend/OPERACION_Y_PRUEBAS.md` | `sesion.yaml` sin OIDC; `web.yaml` con ayudas y `/lote` |
| `docs/AppBackend/SIMBOLOS.md` | `PoolPostgres` en la línea del archivo fusionado |
| `docs/AppFrontend/ARQUITECTURA.md` | Barra con Lote y botones de cuenta local |
| `docs/AppFrontend/OPERACION_Y_PRUEBAS.md` | Sin OIDC, con `PaginaLote.py` y el ajuste de React Router |
| `docs/AppFrontend/SIMBOLOS.md` | Igual que el índice de backend para `PoolPostgres` |
| `docs/Audit/resolves/README.md` | Las tres filas: rediseño, arranque y login |

## Verificación

Pendiente: `git diff --check` sin marcadores y el merge commit.
