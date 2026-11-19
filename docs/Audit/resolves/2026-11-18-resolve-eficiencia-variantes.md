# RES-2026-11-18-EFIC — Contar variantes sin materializar el producto

Fecha: 2026-11-18 (America/Bogota)
Estado: RESUELTO
Responsable: agente de implementación, por instrucción del usuario

## Autorización

> «cuando guaqrdo una configuracion grande el contenedor se pone al maximo,
> corrige las inneficiencias que estan en el programa»

## Decisión

`RESUELTO` — `GeneradorWeb.ContarCombinaciones` + `_ContarVariantes` en
`EstadoApp` para resumen, validez y guardar plantilla. Solo `Generar`/`PedirLote`
materializa la lista al registrar el lote.

## Evidencia

- `unittest` generador: conteo = `len(Combinaciones)` en casos de prueba.
