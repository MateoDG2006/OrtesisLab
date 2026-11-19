# Teclado y hit areas en parámetros

Written against: `0965184`

## Evidence chain

- Surface: mosaicos de patrón (Diseño radiogroup, Lotes pressed); ayuda; CTA superficie
- Problem: `role=radio` sin flechas APG; ayuda `size=1`; link «Cambiar archivo» `min_height:24px`
- Design evidence: `ol-tile:focus-visible` ya existe; switches ya piden `min_height=44px`
- Owner: `Mosaico`, `Etiqueta`, `Cargador` trigger
- Scope: controles de formulario compartidos

## Design decision

1. Radiogroup: implementar roving tabindex + ArrowLeft/Right/Up/Down (o sustituir por primitivo Radix radio si encaja sin romper iconos).
2. Grupo Lotes (`aria-pressed`): Space/Enter ya nativos en `button`; asegurar foco visible.
3. Hit areas: ayuda ≥ size 2; CTA superficie como botón underline con padding ≥40px alto táctil.

## Reuse

- Clase `ol-tile`, tokens focus `--focus-8` / `#12B8B0` → preferir `var(--focus-8)` en CSS

## Changes

1. `Mosaico` + handlers teclado en radiogroup Diseño
2. `Etiqueta` icon_button size
3. `Cargador` trigger styles
4. `ortesislab.css` outline usa `var(--focus-8)`

## Validation

- Solo teclado: elegir patrón, abrir ayuda, abrir diálogo superficie, Previsualizar
- Touch: targets no se solapan

## Stop conditions

- Stop if Reflex no permite key handlers en `rx.el.button` del mosaico sin JS custom — entonces evaluar componente Radix.

## Design documentation

- Actualizar § UX accesibilidad en `COMPONENTES_Y_FLUJOS.md`.
