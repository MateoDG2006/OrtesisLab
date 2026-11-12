# Issue #6 — Caché y métricas (A-12, A-13)

Estado: RESUELTO  
Fecha: 2026-11-12  
Auditoría: AUD-2026-10-13-001

## Hallazgos

| ID | Decisión |
|---|---|
| A-12 | RESUELTO — `SuperficieInterior` con `Lock`, presupuesto en bytes y `Configuracion.Recargar` invalida caché; `CacheRedis` copia lecturas y omite entradas > `max_entrada_bytes`. |
| A-13 | RESUELTO — Propiedades `vertices`/`faces` en `Model3DForPrinting` invalidan `_volumen_mm3`. |

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.nucleo.test_cache_metricas -v
```
