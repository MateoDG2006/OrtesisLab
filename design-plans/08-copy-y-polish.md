# Copy y polish final

Written against: `0965184`

## Evidence chain

- Surface: disclaimer PETG bajo el escenario; microcopy de badges/estados
- Problem: párrafo de precio/moneda denso; hex residuales; letter-spacing de marca (intencional del canvas — **no cambiar** salvo petición)
- Design evidence: textos actuales en `Escenario`; badges en CSS
- Owner: `PaginaComparacion.Escenario`, CSS puntual
- Scope: copy + detalles visuales menores

## Design decision

Acortar el disclaimer a dos líneas máximas o tooltip «Cómo se calcula el precio». Pasada `baseline-ui`: spacing consistente en cards, focus rings con token.

## Reuse

- `ol-muted`, tooltips existentes (`Etiqueta`)

## Changes

1. Texto precio/volumen en `Escenario`
2. Revisar mensajes `Inicie sesión…` para tono uniforme (ya correctos en español)
3. CSS: eliminar hex duplicados donde exista token

## Validation

- Lectura en 5 s del pie del escenario; sin regresión de layout

## Stop conditions

- Stop if finanzas debe declarar moneda real (requiere decisión de producto/backend).

## Design documentation

- Ninguna si solo copy; si cambia regla de precio, `PARAMETROS` / contratos.
