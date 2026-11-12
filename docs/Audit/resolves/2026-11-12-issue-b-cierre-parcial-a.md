# RES-2026-11-12-B-A — Cierre parcial hallazgos B (tramo A)

Fecha: 2026-11-12 (America/Bogota)  
Auditoría: AUD-2026-10-29-002  
Autorización: `docs/Audit/resolves/2026-11-12-resolve-aud-2026-10-29.md` (EN_CURSO)  
Estado: **RESUELTO** (tramo A: B-05…B-15, B-19…B-22 implementados aquí)

## Hallazgos cerrados en este tramo

| ID | Decisión | Verificación |
|---|---|---|
| B-05 | Cuotas en `persistencia.yaml`; comprobación en `ServicioImports._Registrar` | `test_cuota_almacen` |
| B-06 | `try/except BaseException` + conciliador de imports colgados | `test_import_fallo_publicar` |
| B-07 | Advisory lock en admisión (`RepositorioLotes.BloquearUsuario`) | Revisión de código + dedup en transacción |
| B-08 | CHECK `total_items` desde `maximo_items`; `ValidarEnArranque` | Smoke `ValidarEnArranque` |
| B-09 | Esquema por área en `ConfiguracionBackend.Cargar` | Smoke `ValidarEnArranque` |
| B-10 | Retroceso en `_Seguir` y `ServicioLotes.Esperar` | Revisión de código |
| B-11 | `capacidad_variante_s` en UI | Revisión de código |
| B-12 | `conciliador.explorar_bucket: false` por defecto | Revisión de código |
| B-13 | Purga `auth_sessions` / `history_events` vía conciliador | Revisión + `DATABASE.md` |
| B-15 | Logout POST; GET → 405; CORS local en `rxconfig.py` | Revisión de código |
| B-19 | Hash y comparación sin `repair`/`resolution_mm` | `CONTRATOS.md` |
| B-20 | `Confirmar` aborta si `CancelacionPedida` | Revisión de código |
| B-21 | Búsqueda de issue por URL Notion antes de crear | Revisión de `notion_sync_issues.py` |
| B-22 | Botón «Cancelar lote» en comparación | Revisión de `PaginaComparacion.py` |

## Comandos ejecutados (2026-11-12, `.venv`)

```
.venv\Scripts\python.exe -c "from web.ConfiguracionBackend import ConfiguracionBackend; ConfiguracionBackend.ValidarEnArranque(); print('ok')"
→ ok

.venv\Scripts\python.exe -m unittest tests.persistencia.test_cuota_almacen tests.persistencia.test_import_fallo_publicar -v
→ 2 OK

.venv\Scripts\python.exe -m unittest discover -s tests/persistencia -p test_*.py -q
→ Ran 25 tests, OK (skipped=23)
```

## Archivos tocados (tramo A)

- `config/persistencia.yaml`, `config/trabajador.yaml`
- `web/ConfiguracionBackend.py`, `web/persistence/Modelos.py`
- `web/services/ServicioImports.py`, `ServicioLotes.py`, `ServicioVersiones.py`
- `web/persistence/repositorios/RepositorioAssets.py`, `RepositorioImports.py`, `RepositorioUsuarios.py`, `RepositorioHistorial.py`
- `web/jobs/ConciliadorArchivos.py`, `web/jobs/TrabajadorGeneracion.py`
- `web/EstadoApp.py`, `web/EstadoHistorial.py`, `web/PaginaComparacion.py`, `web/Sesion.py`, `web/GenerateModelsApp.py`
- `web/services/AutenticacionOidc.py`
- `rxconfig.py`, `.github/scripts/notion_sync_issues.py`
- `tests/persistencia/test_cuota_almacen.py`, `tests/persistencia/test_import_fallo_publicar.py`
- `docs/AppBackend/CONTRATOS.md`, `docs/AppBackend/DATABASE.md`, `docs/Agents/REGISTRO_CAMBIOS.md`
