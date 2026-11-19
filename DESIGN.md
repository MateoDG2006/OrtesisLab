# OrtesisLab — design language

Generated from the implemented product UI (Reflex web app). Mode: **Operate**.

## Product surface

Routes: `/` (Diseño), `/lote`, `/historial`, plus `/auth/login` and `/auth/registro` (Starlette HTML on the API host) and embedded `/visor.html`.

## Foundations

| Token | Light | Dark | Role |
|---|---|---|---|
| `--ol-bg` | `#F3EDE6` | `#0A1719` | Page background |
| `--ol-panel` | `#FFFFFF` | `#102427` | Cards / chrome / navbar / aside |
| `--ol-panel2` | `#FAF6F1` | `#15302F` | Nested surfaces |
| `--ol-text` | `#12292B` | `#F3EDE6` | Body |
| `--ol-muted` | `#4F6567` | `#9FB5B3` | Secondary labels |
| `--ol-accent` | `#195A5F` | `#12B8B0` | Primary actions / selected tiles |
| `--ol-onaccent` | `#FFFFFF` | `#04201F` | Text on accent |
| `--ol-coral` | `#A9483A` | `#E8937F` | Errors / cancel |
| `--ol-stage` | `#E6F1EF` | `#0D1E21` | 3D stage |
| `--ol-mesh` | `#138F89` | `#12B8B0` | Pattern icons / upload dashed |
| `--ol-safe` | `24px` (`16px` ≤960px) | Same | Inset from viewport edges |
| `--ol-aside` | `440px` | Same | Diseño side panel width |

Typography: **Manrope** 400–700 via Google Fonts; roles via `--ol-fs-label` (12px), `--ol-fs-body` (14px), `--ol-fs-ui` (15px), `--ol-fs-title` (18px), `--ol-fs-brand` (20px); line-heights `--ol-lh-tight` / `--ol-lh-body`. Radix Themes `large` radius and teal/sage mapping through `--accent-*`.

Shape: panels and cards `16px` radius (`ol-card` / slots), pills for nav and primary buttons, pattern tiles `12px`.

## Layout shell

- `ol-shell` (column, `100dvh`) → `header.ol-navbar` → `main.ol-main`
- Diseño: `ol-workspace` = `ol-stage` (flex grow) + `aside.ol-aside` (full remaining height, scroll)
- Lotes / Historial: `ol-main-pad` with safe margins around content

## Components (owners)

- Shell / navbar: `Sesion.Barra` + `PaginaComparacion.Pagina`
- Tokens/CSS: `apps/web/assets/ortesislab.css`
- Auth (inline tokens, no Reflex): `PlantillaAuth` + `assets/auth/`
- Visor theme + controls: `assets/visor/` (no on-canvas buttons; drag/wheel/keys)
- Pattern icons: Lucide through `rx.icon` (`ICONOS_PATRON`)

## Interaction notes

- Pattern radiogroup: arrow keys via `EstadoApp.TeclaPatron` on `_GrupoTeclado`
- Historial: table ≥769px; card list ≤768px (`ol-solo-*`)
- Visor: drag, wheel, arrows/`+`/`-`/`Home`; follows host `html.dark` when same-origin

## Explicit non-goals (current)

- Synchronized cameras across iframes
- Full WCAG CI gate
- Brand logo beyond wordmark text
