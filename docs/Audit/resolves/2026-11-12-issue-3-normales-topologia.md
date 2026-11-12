# RES-2026-11-12-ISSUE-3 — Normales, topología, unidades y resolución (A-04, A-05, A-06, A-14, A-16, A-22)

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001
Estado: RESUELTO
Responsable: agente de implementación
Issues: #3

## Archivos y hallazgos

| Archivo | Hallazgos |
|---|---|
| `GenerateModelsApp/Malla.py` | A-04 (acuerdo con normales geométricas), A-05 (abanicos) |
| `GenerateModelsApp/Cascaron.py` | A-04 (espesor colapsado) |
| `GenerateModelsApp/ValidacionMalla.py` / `ValidacionSolido.py` | A-05 (`nonmanifold_verts`) |
| `GenerateModelsApp/RefinadorMalla.py` | A-06 (`CalidadInsuficiente` con arista real) |
| `GenerateModelsApp/EscalaMalla.py` | A-14 (escala fija; no encoger por el paso) |
| `web/LectorSuperficie.py` | A-16 (soldar tras resolver unidades) |
| `GenerateModelsApp/SuavizadoBorde.py` | A-22 (filtro de normales con perímetro físico) |
| `tests/geometria/test_normales_topologia.py` | regresiones |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.geometria.test_normales_topologia tests.geometria.test_escala_malla -v
→ OK
```
