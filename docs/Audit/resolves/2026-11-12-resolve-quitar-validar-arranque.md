# RES-2026-11-12-011 — Quitar `ValidarEnArranque` del arranque

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002. El módulo era `web/GenerateModelsApp.py` y ahora es `apps/web/web/OrtesisLabApp.py`.
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

El arranque de `make web` falló con:

> AttributeError: type object 'ConfiguracionBackend' has no attribute 'ValidarEnArranque'

Alcance: dejar de llamar ese método. `Cargar` sigue siendo la única lectura del YAML. No se cierra B-09.

## Decisión

`PoolPostgres` abre PostgreSQL y captura `ErrorPersistencia` si la base no responde. La llamada sobraba.

## Verificación

No se reinició Reflex en esta corrección: el trabajador ya había salido. Hay que volver a ejecutar `make web`.
