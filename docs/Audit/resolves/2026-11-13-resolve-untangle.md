# RES-2026-11-13-001 — Desenredo estructural

Fecha: 2026-11-13 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción del usuario el 2026-11-13, al ejecutar `/untangle-codebase` y, en la
pregunta siguiente, elegir «Yes — edit the source, tests, and the docs this
untangle requires». Esa respuesta autoriza editar el código de la aplicación,
las pruebas y la documentación que este desenredo toque, y registrar esta
autorización antes del primer cambio. No cierra hallazgos de auditoría. No
autoriza borrar columnas, cambiar qué sólidos se aceptan al exportar, ni
sustituir la cola o la configuración por librerías nuevas.

## Decisión

Las piezas que cambian juntas quedan en un solo sitio:

- El STL binario (cabecera, registro, abanico de polígonos y rechazo float32)
  vive en `OrtesisLabPlugin/StlBinario.py`. La web, el lector y el exportador
  de Blender lo llaman.
- Un patrón declara si tiene celosía y si pide semilla. Los `if pattern ==
  "SOLID"` y `== "VORONOI"` del núcleo, el trabajador y el panel leen eso.
- El tope de variantes de la página es `persistencia.yaml` `lotes.maximo_items`.
  Desaparece la copia `web.yaml` `maximo_variantes`.
- Se quitan reenvíos sin lógica propia (`ChangePattern`, `Cascaron.Cerrar`,
  `GeneradorWeb.Escribir`, `Ver`, los `set_*` que solo asignan el campo,
  `ValidacionMalla._Componentes`, las clases `Triangle` y `Minimalistic` y el
  catálogo sin lectores) y la caché de superficie que `Recargar` ya intentaba
  vaciar.

El suavizado, la heurística de cruces y el esquema de PostgreSQL no se tocan.

## Archivos

El alcance es el código de `apps/`, `tests/`, `core/config/web.yaml` y la
documentación canónica que describa estas piezas. El detalle queda en
`docs/Agents/REGISTRO_CAMBIOS.md` al cerrar la verificación.
