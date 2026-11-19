# RES-2026-11-18-RUIDO-INTERIOR — Suavizado Taubin del ruido de malla

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: RESUELTO (alcance de esta entrega; no cierra hallazgos A/B históricos)
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-18:

1. «Hay que suavizar el interior de la ortesis ya que se pueden ver
   irregularidades en la malla y eso tiene que quedar completamente liso»
2. Alcance confirmado: «Solo el ruido de la malla»
3. «Implement the plan as specified» sobre el plan «Suavizado de ruido en el interior»

## Archivos y hallazgos

| Archivo actual | Archivo en inventario histórico | Hallazgos | Decisión de esta entrega |
|---|---|---|---|
| `apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoSuperficie.py` | (nuevo) | — | Taubin interior |
| `apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py` | `GenerateModelsApp/Modeling.py` | (cerrados en issues) | Llamar suavizado antes del borde |
| `apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py` | `GenerateModelsApp/util/Utilidades.py` | — | Claves de límite |
| `core/config/limites.json` | `GenerateModelsApp/config/limites.json` | A-03/A-11 (cerrados) | Defaults Taubin |
| Tests y docs canónicas | mantenimiento | — | Criterio de ruido |

## Decisión y trabajo realizado

1. `SuavizadoSuperficie.Aplicar`: Taubin λ/μ, borde fijado, tope 0,4 mm, back-off de caras, normales desde caras.
2. `ConstruirGeometria` lo aplica tras `flip_normals` y antes de `SuavizadoBorde`.
3. Límites: `surface_smooth_iterations=5`, `lambda=0.5`, `mu=-0.53`, `max_mm=0.4`.

## Verificación

```
python -m unittest tests.geometria.test_suavizado_superficie tests.geometria.test_suavizado_borde tests.geometria.test_normales_topologia -v
→ 14 OK
```

## Riesgo residual

Ruido de amplitud &gt; 0,4 mm o de longitud de onda comparable a la anatomía
puede residualizarse o atenuarse parcialmente. No remalla ni ejecuta voxel en web.
