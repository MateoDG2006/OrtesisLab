# Visor 3D alineado al tema OrtesisLab

Written against: `0965184`

## Evidence chain

- Surface: iframe `/visor.html` embebido en Diseño, Lotes, Historial
- Problem: estilos fijos `#eef1f4` / `#1c2024` ajenos a `--ol-stage` / dark
- Design evidence: `ortesislab.css` `--ol-stage`, `--ol-text`, `--ol-bg`; host usa `html.dark`
- Owner: `apps/web/assets/visor.html`
- Scope: CSS (+ opcional lectura de tema del parent)
- Uncertainty: cross-origin del object_url STL no afecta CSS del documento visor

## Design decision

Sustituir colores del documento del visor por variables alineadas a `--ol-*`, con fallback dark vía `prefers-color-scheme` y, si es viable, sincronizar con `parent.document.documentElement.classList` cuando same-origin.

## Reuse

- `--ol-stage` como fondo del canvas area; `--ol-text` / `--ol-coral` para mensajes
- Exemplar: sección `Escenario` (`background: var(--ol-stage)`)

## Changes

1. `apps/web/assets/visor.html`
   - Change: definir `:root` / `html.dark` o media query con los mismos hex que `ortesislab.css` (o importar CSS si el asset pipeline lo permite)
   - Preserve: Three.js, validación de URL, modo miniatura
   - Verify: en dark mode el iframe no queda gris claro dentro del escenario teal oscuro

## Scope

- Inherit: todos los `Visor` / `Marco`
- Exclude: nuevos controles de cámara (plan 07)

## Validation

- Interface: previsualización en `/` claro y oscuro; miniatura en `/lote`
- Repository: diff solo en `visor.html` (+ CSS si se comparte)

## Stop conditions

- Stop if el iframe se sirve de origen distinto y no puede leer al parent — usar solo `prefers-color-scheme`.

## Design documentation

- Actualizar `docs/AppFrontend/VISOR_3D.md` con la dependencia de tema.
