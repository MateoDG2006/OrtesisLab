# Auth alineado al sistema OrtesisLab

Written against: `0965184`

## Evidence chain

- Surface: `/auth/login`, `/auth/registro` (`Autenticacion._Pagina`)
- Problem: HTML genérico `system-ui` sin tokens `--ol-*`, sin marca, sin dark mode; registro comparte `autocomplete="current-password"`
- Design evidence: `apps/web/assets/ortesislab.css`; shell `Sesion.Barra` (Manrope, teal/coral, paneles)
- Owner: `apps/web/web/services/Autenticacion.py`
- Scope: plantilla HTML de auth únicamente
- Uncertainty: si `cookie_secure` / redirect ya están OK — no tocar

## Design decision

Rehacer `_Pagina` para que use la misma paleta y tipografía que la app (enlace a `/ortesislab.css` + Manrope), layout tipo card centrada, marca «OrtesisLab», y atributos autocomplete distintos para login vs registro.

## Reuse

- Tokens: `--ol-bg`, `--ol-panel`, `--ol-text`, `--ol-muted`, `--ol-accent`, `--ol-line`, `--ol-coral`
- Exemplar visual: `Sesion.Barra` + `ol-card`
- CSS existente: `/ortesislab.css` (servido por Reflex)

## Changes

1. `apps/web/web/services/Autenticacion.py` · `_Pagina`
   - Change: stylesheet Manrope + ortesislab.css; body con fondo `--ol-bg`; formulario en panel; botón accent; error con color coral y `role="alert"`
   - Preserve: POST actions, cookie, redirects, textos ES
   - Verify: login/registro se ven como OrtesisLab en claro/oscuro (`html.dark` / `prefers-color-scheme` si no hay toggle en auth)

2. Misma función: parámetro o rama registro
   - Change: registro → `autocomplete="new-password"`; login → `current-password`
   - Preserve: `username` en ambos
   - Verify: DevTools muestra tokens distintos

## Scope

- Inherit: solo respuestas HTML de auth
- Verify: botones «Crear cuenta» / «Iniciar sesión» en `Sesion` siguen apuntando a las mismas rutas
- Exclude: migrar auth a páginas Reflex; OAuth; copy legal

## Validation

- Product: usuario crea cuenta e inicia sesión y vuelve a `/`
- Interface: 360px y 1280px; claro/oscuro del SO
- System: no nuevos colores hex fuera de tokens
- Repository: inspección visual + `curl` HTML contiene `ortesislab.css`

## Stop conditions

- Stop if auth debe moverse a Reflex State (amplía alcance).

## Design documentation

- Tras aceptar: anotar en `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md` que `/auth/*` comparte tokens `--ol-*`.
