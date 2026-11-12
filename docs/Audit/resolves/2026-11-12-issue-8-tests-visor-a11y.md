# Issue #8 — Tests, visor y accesibilidad (A-19, A-20, A-21, B-14)

Estado: RESUELTO  
Fecha: 2026-11-12  
Auditoría: AUD-2026-10-13-001

## Hallazgos

| ID | Decisión |
|---|---|
| A-19 | RESUELTO — Workflow `.github/workflows/pruebas.yml`, ruff en `pyproject.toml`, ZIP test con `TemporaryDirectory`. |
| A-20 | RESUELTO — Etiquetas `html_for`/`id` en `PaginaComparacion`. |
| A-21 | RESUELTO — `assets/visor.html` con Three local, validación de URL, límites y teclado. |
| B-14 (Three.js) | RESUELTO — `assets/vendor/three-0.169.0.module.js` servido en origen. |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.e2e.test_carga_generacion_descarga -v
```
