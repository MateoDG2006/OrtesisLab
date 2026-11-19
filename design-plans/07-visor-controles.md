# Alternativa al arrastre en el visor 3D

Written against: `0965184`

## Evidence chain

- Surface: iframe de previsualización / comparación
- Problem: copy «arrastre para girar»; sin controles de cámara por teclado (docs)
- Design evidence: `COMPONENTES_Y_FLUJOS.md` § UX; `visor.html` pointer controls
- Owner: `visor.html` + copy en `PaginaLote.Comparacion` / posibles botones host
- Scope: interacción de cámara; no cambiar pipeline STL
- Uncertainty: esfuerzo Three.js vs. mitigación (sacar iframe del tab order + texto)

## Design decision

Preferido: botones Orbit izq/der, Zoom +/−, Reset en el documento del visor (focusables), respetando `prefers-reduced-motion` (saltos sin tween largo).  
Mínimo aceptable: `tabindex=-1` en iframes de comparación + texto visible «La vista 3D se controla con el ratón o el dedo; use Descargar STL para inspeccionar fuera.»

## Reuse

- Estilos del plan 02; iconos Lucide ya usados en host si los controles viven fuera del iframe

## Changes

1. `visor.html`: botones o mitigación documentada
2. Copy en Lotes/Diseño alineado a la decisión real

## Validation

- Teclado llega a controles; reduced-motion no bloquea el cambio de vista

## Stop conditions

- Stop if se exige sincronizar cámaras entre iframes (fuera de alcance).

## Design documentation

- `VISOR_3D.md` debe describir la decisión implementada.
