# RES-2026-11-18-BORDE-TACTIL — Contorno superior continuo al tacto

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: RESUELTO (alcance de esta entrega; no cierra hallazgos A/B históricos)
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-18, al aprobar el plan
«Borde superior continuo al tacto»:

> «Implement the plan as specified»

Alcance autorizado: endurecer el suavizado automático del contorno
(`border_smooth_wavelength_mm` / `border_smooth_max_mm` y segunda pasada en
`SuavizadoBorde.Aplicar`), pruebas geométricas y documentación canónica.
No cierra hallazgos A/B previos; no reabre A-22 (se conserva el filtro FFT con
perímetro físico). No habilita remallado del cascarón ni controles nuevos en UI.

## Archivos y hallazgos

| Archivo actual | Archivo en inventario histórico | Hallazgos | Decisión de esta entrega |
|---|---|---|---|
| `apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py` | `GenerateModelsApp/SuavizadoBorde.py` | A-22 (cerrado en RES-2026-11-12-ISSUE-3) | Doble pasada; perímetro físico intacto |
| `core/config/limites.json` | `GenerateModelsApp/config/limites.json` | A-03, A-11 (cerrados en issue-1) | `wavelength` 24 mm, `max` 8 mm |
| `tests/geometria/test_suavizado_borde.py` | (pruebas) | — | Criterio táctil &lt; 0,15 mm + estabilidad |
| Docs canónicas e índices | mantenimiento | — | Valores y doble pasada documentados |

## Decisión y trabajo realizado

1. Defaults 24 / 8 mm para eliminar dientes de malla al tacto.
2. `Aplicar` llama `_Pasada` dos veces (tope y salvaguarda de caras en cada una).
3. Pruebas del abanico, peine, cascarón y tercera pasada casi nula.
4. Riesgo documentado: muescas clínicas &lt; ~24 mm se redondean más; `wavelength ≤ 0` desactiva.

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.geometria.test_suavizado_borde -v
→ 5 OK
```

## Riesgo residual

No cierra la auditoría inicial ni desbloquea otros archivos del inventario.
El redondeo de muescas intencionales cortas queda como riesgo aceptado del plan.
