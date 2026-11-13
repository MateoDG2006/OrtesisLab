# RES-2026-11-12-016 — Normal de un pliegue al refinar

| Campo | Valor |
|---|---|
| Resolución | RES-2026-11-12-016 |
| Auditoría | AUD-2026-10-13-001 y AUD-2026-10-29-002 |
| Estado | EN_CURSO |
| Fecha | 2026-11-12 |
| Responsable | implementación pedida en el chat |

## Autorización

El trabajador, ya en marcha, repite este fallo al refinar la superficie:

```text
Superficie refinada sin Blender: 242645 vértices, 482717 triángulos, paso 1.000 mm.
NormalesInvalidas: Normales de la superficie inválidas. | Las normales no coinciden con la orientación de las caras.
```

Esa traza autoriza corregir ese rechazo en el refinado. No cierra A-04 ni ningún otro hallazgo.

## Alcance

| Inventario | Archivo vigente |
|---|---|
| `GenerateModelsApp/Malla.py` | `apps/ortesis-plugin/OrtesisLabPlugin/Malla.py` |
| `GenerateModelsApp/RefinadorMalla.py` | `apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py` |
| `docs/BlenderPlugin/ALGORITMOS.md` | el mismo |

## Fuera de alcance

No se baja el umbral de 0,5 ni se reescriben normales de `superficie_interior_mm.npz`.
