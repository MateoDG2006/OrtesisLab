# RES-2026-11-12-005 — Quitar seeds y la base de pruebas

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12:

> «Necesito que elimines la parte de seeds y test de la db ya que lo vamos a generar con contenido que utilicemos.»

Alcance autorizado: borrar el fixture `apps/db/seeds/` y la base desechable `ortesislab_test` (`apps/db/test/`, `make db-seed`, `make db-test-reset` y las URL `ORTESISLAB_TEST_*` de la plantilla). El SQL de permisos de una base vacía pasa a `apps/db/preparar_base.sql` y solo lo usa `make db-reset` sobre `ortesislab_dev`. No cambia el esquema, los roles ni la geometría. Los hallazgos siguen abiertos.

## Archivos

| Archivo desde la raíz | Hallazgos | Decisión |
|---|---|---|
| `db/seeds/development.sql` (ahora `apps/db/seeds/development.sql`) | Inventario AUD-2026-10-29-002 | Borrar |
| `db/test/preparar_base.sql` (ahora `apps/db/test/preparar_base.sql`) | Inventario AUD-2026-10-29-002 | Mover fuera de `test/` para el reset de desarrollo |
| `Makefile` | Inventario AUD-2026-10-29-002 | Quitar `db-seed` y `db-test-reset` |
| `infra/database/compose.yaml` (ahora `apps/db/compose.yaml`) | Inventario AUD-2026-10-29-002 | Dejar de montar `./seeds` |
| `.env.example`, `README.md` | Ambas auditorías donde constan | Quitar la base de pruebas de la plantilla y de la guía |
| `docs/AppBackend/DATABASE.md`, `MODULOS.md`, `OPERACION_Y_PRUEBAS.md`, `tests/README.md` | AUD-2026-10-29-002 | Describir solo el comportamiento que queda |
| `tests/persistencia/apoyo_persistencia.py` | Inventario AUD-2026-10-29-002 | El texto deja de nombrar una base que el repositorio ya no trae |
| `.github/workflows/pruebas.yml` | No está en los inventarios | Quitar el job que creaba `ortesislab_test` |

## Verificación

Se completa en el registro de cambios de esta entrega. No cierra hallazgos.
