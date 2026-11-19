# RES-2026-11-18-PLANTILLAS — Plantillas de lote, generación desatendida y GPU

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario + plan aprobado «Plantillas lote GPU»:
plantillas con nombre (1A), encolado fire-and-forget (2A), GPU opcional CuPy.

## Decisión

`RESUELTO` — `lote_plantillas` + CRUD UI; `Generar` en lote sin `_Seguir`
bloqueante; multi-plantilla hasta `maximo_pendientes`; `Arrays` con CuPy
opcional en hotspots de patrón.

## Evidencia

- `reflex compile --dry`: OK
- Tests unitarios de `Arrays` / `DistanciaCuadricula` y suite aplicacion_web
- Migración `a1b2c3d4e5f6` añadida (aplicar con `make migrar` en cada entorno)
