# Issue #7 — Contratos y consola (A-17, A-18)

Estado: RESUELTO  
Fecha: 2026-11-12  
Auditoría: AUD-2026-10-13-001

## Hallazgos

| ID | Decisión |
|---|---|
| A-17 | RESUELTO — `GenerateModelsApp/contratos.py` con validadores compartidos. |
| A-18 | RESUELTO — `EstadoApp` toma defaults de `ParametrosDefecto`; script `ortesislab`; `consola.py`. |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.nucleo.test_compatibilidad_npz_json tests.nucleo.test_wheel -v
```
