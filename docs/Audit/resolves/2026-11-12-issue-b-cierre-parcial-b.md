# RES-2026-11-12-B-B — Cierre parcial hallazgos B (tramo B)

Fecha: 2026-11-12 (America/Bogota)  
Auditoría: AUD-2026-10-29-002  
Autorización: `docs/Audit/resolves/2026-11-12-resolve-aud-2026-10-29.md`  
Estado: **RESUELTO**

## Hallazgos cerrados en este tramo

| ID | Decisión | Evidencia |
|---|---|---|
| B-01 | Constantes de contrato restauradas (tramo previo issue-1) | `web/persistence/Contratos.py`, resolve issue-1 |
| B-02 | Revisión Alembic inicial con tablas, trigger y GRANT | `db/alembic/versions/20261112_1200_esquema_inicial.py`, `tests/persistencia/test_alembic_revision.py`, `DATABASE.md` |
| B-03 | CI: `uv sync`, humo, unittest, `GenerarIndices --comprobar`, job `persistencia` | `.github/workflows/pruebas.yml` |
| B-04 | Caché plantilla + semáforo `NORMALIZACION` | `web/GeneradorWeb.py`, `web/LectorSuperficie.py`, `config/web.yaml`, `ARQUITECTURA.md` |
| B-14 | RIESGO_ACEPTADO STL anónimo + visor local cubiertos por issue-2 e issue-8 | [issue-2](2026-11-12-issue-2-riesgo-stl-anonimo.md), [issue-8](2026-11-12-issue-8-tests-visor-a11y.md) |
| B-16 | ZIP Blender regenerado y prueba de paquete | `scripts/EmpaquetarBlender.py`, `tests/blender/blender_paquete_zip.py` |
| B-17 | Enlaces Audit, `sweep` en contratos, MODULOS/Alembic, índices | `docs/README.md`, `CONTRATOS.md`, `MODULOS.md`, `GenerarIndices.py` |
| B-18 | `pyproject.toml`, Ruff N802, `.vscode/settings.json`, consola | `pyproject.toml`, `.vscode/settings.json`, `src/generatemodelsapp/__init__.py` |

## B-14 — nota de cobertura

El hallazgo B-14 (STL servido sin sesión y superficie en visor) queda **totalmente cubierto** por:

- **A-02 / STL anónimo:** [RES-2026-11-12-ISSUE-2](2026-11-12-issue-2-riesgo-stl-anonimo.md) (`RIESGO_ACEPTADO`, controles MinIO y política documentada).
- **Visor / pruebas / a11y:** [RES-2026-11-12-ISSUE-8](2026-11-12-issue-8-tests-visor-a11y.md) (Three.js local, sin CDN, humo CI).

No se requieren cambios de código adicionales en este tramo para B-14.

## Verificación (2026-11-12, `.venv`)

```
.venv\Scripts\python.exe -m unittest tests.persistencia.test_alembic_revision tests.aplicacion_web.test_humo_import -v
→ 3 OK

.venv\Scripts\python.exe -c "from web.ConfiguracionBackend import ConfiguracionBackend; ConfiguracionBackend.ValidarEnArranque(); print('ok')"
→ ok

.venv\Scripts\python.exe scripts\EmpaquetarBlender.py
→ GenerateModelsApp.zip actualizado

.venv\Scripts\python.exe docs\Agents\Scripts\GenerarIndices.py
.venv\Scripts\python.exe docs\Agents\Scripts\GenerarIndices.py --comprobar
→ catálogos al día

.venv\Scripts\python.exe -m unittest discover -s tests -p test_*.py -q
→ ver salida de la sesión (omitidas sin bpy/base según caso)

uv run ruff check .
→ 124 avisos previos en el repo (I001/E501 en complemento y web); configuración N802 añadida; la deuda no bloquea el cierre B-18
```

`tests/blender/blender_paquete_zip.py` requiere Blender (`bpy`); no ejecutado en este entorno.

## Archivos tocados (tramo B)

- `db/alembic/versions/20261112_1200_esquema_inicial.py`
- `tests/persistencia/test_alembic_revision.py`
- `.github/workflows/pruebas.yml`
- `config/web.yaml`, `web/ConfiguracionBackend.py`, `web/GeneradorWeb.py`, `web/LectorSuperficie.py`
- `pyproject.toml`, `.vscode/settings.json`
- `docs/README.md`, `docs/AppBackend/DATABASE.md`, `OPERACION_Y_PRUEBAS.md`, `ARQUITECTURA.md`, `CONTRATOS.md`, `MODULOS.md`
- `docs/Agents/REGISTRO_CAMBIOS.md`, índices en `docs/Audit/resolves/`
