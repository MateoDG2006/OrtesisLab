# Roadmap de mejora UI — todas las pantallas

Written against: `0965184`  
Fuente: [AUDITORIA_UI_2026-11-18.md](./AUDITORIA_UI_2026-11-18.md)  
Modo: Operate (herramienta clínica/técnica). No rediseñar la identidad teal/coral/Manrope; cerrar huecos.

## Objetivo

Subir de **12/20 → ≥16/20** en la rúbrica de auditoría técnica, con coherencia visual en auth/visor, Historial usable en móvil y a11y de controles críticos, sin cambiar contratos de generación.

## Fases

### Fase A — Identidad y theming (P0) · 1–2 días

| Pantalla | Trabajo | Plan |
|----------|---------|------|
| `/auth/*` | Plantilla HTML con tokens `--ol-*`, Manrope, marca, dark mode básico, autocomplete correcto | [01-auth-sistema-visual.md](./01-auth-sistema-visual.md) |
| `visor.html` | Fondo/texto alineados a tema host o `prefers-color-scheme` | [02-visor-theming.md](./02-visor-theming.md) |
| CSS global | Sustituir hex sueltos restantes por tokens (`focus`, upload icon) | incluido en 01/02 |

**Done when:** login/registro y el iframe no se ven de otro producto; dark mode no “rompe” el escenario 3D.

### Fase B — Estructura y responsive (P0/P1) · 2–3 días

| Pantalla | Trabajo | Plan |
|----------|---------|------|
| Shell + 3 rutas | `<main>`, un `<h1>` por ruta, landmark nav ya existente | [03-landmarks-jerarquia.md](./03-landmarks-jerarquia.md) |
| `/historial` | Vista cards / columnas prioritarias bajo 768px; empty state | [04-historial-responsive.md](./04-historial-responsive.md) |
| `/` · `/lote` | Empty states con una acción clara | [05-empty-states.md](./05-empty-states.md) |

**Done when:** Historial usable a 360–768px sin solo scroll ciego; cada página anuncia título y región principal.

### Fase C — Accesibilidad de interacción (P1) · 2–3 días

| Pantalla | Trabajo | Plan |
|----------|---------|------|
| `/` patrones | Teclado APG en mosaico radio / pressed | [06-patrones-teclado.md](./06-patrones-teclado.md) |
| Ayuda + carga | Hit areas ≥40px; CTA de superficie no como link frágil | mismo plan 06 o polish |
| Visor 3D | Controles orbit/zoom por botón **o** omitir foco + texto de limitación | [07-visor-controles.md](./07-visor-controles.md) |

**Done when:** flujo Diseño completable solo con teclado hasta Previsualizar; comparación 3D no depende solo del arrastre sin alternativa documentada en UI.

### Fase D — Copy y craft (P2) · 1 día

| Pantalla | Trabajo |
|----------|---------|
| `/` | Aclarar disclaimer PETG/moneda |
| `/lote` | Alinear microcopy de progreso/cancelar |
| Global | Pasada `baseline-ui` / `better-ui` (spacing, focus rings con token) |

Plan ligero: [08-copy-y-polish.md](./08-copy-y-polish.md)

### Fase E — Documentación de diseño (después de A–C)

- Generar `DESIGN.md` con `create-design-md` / `impeccable document` a partir del código ya corregido
- Actualizar `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md` § UX solo con comportamiento implementado
- Registrar en `docs/Agents/REGISTRO_CAMBIOS.md` las pruebas realmente ejecutadas

## Orden de ejecución recomendado

```text
A01 auth → A02 visor → B03 landmarks → B04 historial → B05 empty → C06 teclado → C07 visor controles → D08 copy → E docs
```

## Fuera de alcance (esta hoja)

- Cambiar algoritmos / parámetros / backend de lotes
- Rediseño “bolder” o nueva identidad de marca
- Sincronizar cámaras 3D entre iframes (oportunidad futura ya listada en docs)
- Auditoría WCAG formal con herramientas automatizadas en CI (siguiente iteración)

## Estado

**Implementado** el 2026-11-18 (instrucción del usuario). Ver `docs/Audit/resolves/2026-11-18-resolve-roadmap-mejora-ui.md` y `docs/Agents/REGISTRO_CAMBIOS.md`.
