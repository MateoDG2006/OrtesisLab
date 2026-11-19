# RES-2026-11-18-NORMALES-PLANTILLA — Corregir normales de la plantilla

Fecha: 2026-11-18 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: RESUELTO (alcance de esta entrega; no cierra A-04 ni hallazgos A/B históricos)
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-18:

> «Normales de la superficie inválidas. Necesito que se corrijan las normales
> para poder realizar la generacion en masa»

Esa frase autoriza reparar las normales de la plantilla incluida y el camino
`ServicioImports.PrepararPlantilla` / `AsegurarPlantilla` que bloqueaba el
encolado de lotes. No baja el umbral A-04 de `AnalizadorMalla.Preparar`.

## Archivos y hallazgos

| Archivo actual | Archivo en inventario histórico | Hallazgos | Decisión de esta entrega |
|---|---|---|---|
| `apps/web/assets/superficie_interior_mm.npz` | `assets/superficie_interior_mm.npz` | (sin hallazgo individual; asset bloqueado) | `normals` reescritas desde las caras |
| `apps/web/web/services/ServicioImports.py` | `web/services/ServicioImports.py` | B-04/B-05 (cerrados) | `PrepararPlantilla` usa `NormalesDeCaras` |
| Docs canónicas / registro | mantenimiento | — | CONTRATOS, MODULOS, REGISTRO |

## Decisión y trabajo realizado

1. Diagnóstico: 35 de 52125 vértices con acuerdo &lt; 0,5 (mín. ≈ 0,24).
2. NPZ reescrito con `AnalizadorMalla.NormalesDeCaras`; acuerdo mínimo ≈ 1,0.
3. `PrepararPlantilla` recalcula siempre las normales desde la topología antes de
   `Preparar(..., suavizarNormales=False)`.
4. A-04 intacto: `test_a04_rechaza_normales_tangenciales` sigue rechazando.

## Verificación

```
PrepararPlantilla(PLANTILLA): OK — 52125 / 102878 / 52125 / 52125
python -m unittest tests.geometria.test_normales_topologia -v
→ 5 OK
```

## Riesgo residual

Un NPZ **subido** por el usuario vía `LectorSuperficie._Npz` sigue usando las
normales del archivo; si no cuadran con las caras, A-04 las rechaza. Solo la
plantilla incluida y su preparación forzada quedan alineadas.
