# RES-2026-11-12-007 — Quitar la revisión de Alembic no generada por Alembic

Fecha: 2026-11-12 (America/Bogota)
Auditoría: AUD-2026-10-29-002 donde cita la revisión como evidencia de B-02
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción explícita del usuario, 2026-11-12:

> «Necesito que elimines el archivo de version que esta en alembic si ha sido generado por IA y no por comandos del mismo alembic.»

Alcance: borrar `apps/db/alembic/versions/20261112_1200_esquema_inicial.py` porque no lo emitió Alembic, y el humo `tests/persistencia/test_alembic_revision.py`, que solo importaba ese archivo. Ajustar las frases de la documentación canónica que lo presentan como la revisión vigente. No se reescribe el informe histórico de B-02. No se genera otra revisión a mano. Los hallazgos siguen abiertos.

## Por qué no es una revisión de Alembic

`apps/db/alembic/script.py.mako` siempre escribe `Revision ID`, `Revises`, `Create Date` e `import sqlalchemy as sa`. El archivo borrado no tiene esa cabecera. `upgrade` llama a `Base.metadata.create_all` en lugar de los `op.create_table` de `alembic revision --autogenerate`. El cierre de B-02 lo verificó importando el módulo, no ejecutando Alembic.

## Archivos

| Archivo | Hallazgos | Decisión |
|---|---|---|
| `apps/db/alembic/versions/20261112_1200_esquema_inicial.py` | Evidencia posterior de B-02; no está en el inventario congelado | Borrar |
| `tests/persistencia/test_alembic_revision.py` | Igual | Borrar: su única aserción es que ese archivo existe |
| `docs/AppBackend/DATABASE.md` | B-02 | Dejar de enlazar el archivo |
| `docs/AppBackend/OPERACION_Y_PRUEBAS.md` | B-02, B-17 | Igual |
| `docs/AppBackend/MODULOS.md` | B-17 | Igual |
| `README.md` | B-17 | Aclarar que `make migrar` no crea tablas mientras `versions/` esté vacío |
| `docs/Agents/INVENTARIO.md`, `REGISTRO_CAMBIOS.md` y los `SIMBOLOS.md` | B-17, B-01 | Inventario regenerado y esta entrega |
