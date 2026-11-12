# RES-2026-11-12-ISSUE-1 — Blindar carga y presupuestos (A-01, A-03, A-11)

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001
Estado: RESUELTO
Responsable: agente de implementación (autorización del plan 2026-11-12)
Issues: #1

## Archivos y hallazgos

| Archivo | Hallazgos | Decisión |
|---|---|---|
| `GenerateModelsApp/InspeccionNpz.py` (nuevo) | A-01, A-03 | Inspección de cabeceras NPY y presupuesto de conteos |
| `web/LectorSuperficie.py` | A-01, A-03, A-16 | Usa inspección antes de `np.load` |
| `GenerateModelsApp/Superficie.py` | A-01, A-03 | Idem al cargar NPZ local |
| `GenerateModelsApp/util/Utilidades.py` | A-11 | Esquema de límites (enteros, positivos, ratios, min≤max) |
| `GenerateModelsApp/config/limites.json` | A-03, A-11 | Nuevos topes de caras, salida, semillas y bytes de caché |
| `GenerateModelsApp/constants/Paterns.py` | A-03, A-11 | Tope de área de siembra; `pattern_batch` > 0 |
| `GenerateModelsApp/RefinadorMalla.py` | A-03, A-06 | Presupuesto al refinar |
| `GenerateModelsApp/Excepciones.py` | A-01… | `PresupuestoExcedido`, `CalidadInsuficiente`, `GeneracionCancelada` |
| `config/trabajador.yaml` | A-03 | `max_concurrent_geometry` |
| `web/jobs/TrabajadorGeneracion.py` | A-03 | Semáforo + cancelación intra-variante |
| `web/services/GeneradorGeometrico.py` | A-03 | Presupuestos y `cancelar` |
| `tests/geometria/test_carga_presupuesto.py` | A-01, A-11 | Regresiones |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.geometria.test_carga_presupuesto -v
→ 5 OK
```

## Riesgo residual

Ninguno para estos hallazgos. La cancelación intra-variante se consulta en puntos
de control del trabajador; un cálculo NumPy ya lanzado no se interrumpe a mitad
de un kernel C.
