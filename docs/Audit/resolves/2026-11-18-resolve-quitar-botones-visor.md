# RES-2026-11-18-VISOR-BTNS — Quitar toolbar del visor

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

Instrucción del usuario, 2026-11-18 (captura de Izquierda/Derecha/Arriba/Abajo/Reiniciar):

> «Elimina estos botones»

Alcance: `apps/web/assets/visor/controles.js` (+ CSS hint), docs VISOR/REGISTRO.
No cierra hallazgos A/B históricos.

## Decisión

`RESUELTO` — se elimina la toolbar del iframe; quedan arrastre, rueda y teclado
(flechas, `+`/`-`, Home).
