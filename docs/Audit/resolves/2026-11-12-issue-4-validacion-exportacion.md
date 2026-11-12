# Issue #4 — Validación y exportación (A-07, A-08, A-15)

Estado: RESUELTO  
Fecha: 2026-11-12  
Auditoría: AUD-2026-10-13-001

## Hallazgos

| ID | Decisión |
|---|---|
| A-07 | RESUELTO — `ValidadorSolido`, `GeneradorGeometrico.Construir` y `GeneradorWeb.Stl` validan antes de publicar. |
| A-08 | RESUELTO — `MallaEvaluada.Extraer` + exportación STL desde la misma instantánea evaluada. |
| A-15 | RESUELTO — Comprobación de finitud y límites float32 en `GeneradorWeb.Stl`. |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.geometria.test_exportacion_validada -v
```
