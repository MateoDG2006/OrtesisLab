# Issue #5 — Rollback y par STL/JSON (A-09, A-10)

Estado: RESUELTO  
Fecha: 2026-11-12  
Auditoría: AUD-2026-10-13-001

## Hallazgos

| ID | Decisión |
|---|---|
| A-09 | RESUELTO — `GeneradorObjeto.Crear` construye en objeto temporal y promueve a `OL_Ortesis` solo al terminar. |
| A-10 | RESUELTO — `PublicacionArchivos` escribe `.part` y confirma con `os.replace`; fallo de JSON descarta el STL temporal. |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.blender.test_rollback_publicacion -v
```
