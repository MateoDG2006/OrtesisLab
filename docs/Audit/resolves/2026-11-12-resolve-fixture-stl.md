# RES-2026-11-12-013 — Fixture STL de las pruebas

| Campo | Valor |
|---|---|
| Resolución | RES-2026-11-12-013 |
| Auditoría | AUD-2026-10-13-001 y auditorías que incluyen el test |
| Estado | EN_CURSO |
| Fecha | 2026-11-12 |
| Responsable | implementación pedida en el chat |

## Autorización

El usuario pidió ejecutar las pruebas con `tests/assets/OrtesisTest1model.stl` y revisar el error `NormalesInvalidas` de normales que no coinciden con las caras.

Esa frase autoriza que `test_carga_test_como_superficie_abierta` lea ese archivo en lugar de `tests/assets/Test.stl`, que ya no está en el árbol. No cierra hallazgos.

## Alcance

- `tests/aplicacion_web/test_generador_web.py`
- La mención vigente del fixture en `docs/AppBackend/OPERACION_Y_PRUEBAS.md` y en el inventario

## Fuera de alcance

No se cambia el umbral de normales ni se reescribe `superficie_interior_mm.npz`. No se cierran hallazgos.
