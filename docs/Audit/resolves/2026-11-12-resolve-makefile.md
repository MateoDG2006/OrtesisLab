# RES-2026-11-12-006 — Objetivos de Make

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-29-002. `README.md` también figura en AUD-2026-10-13-001.
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12:

> «Necesito que completes el makefile que esta actualmente con los comandos necesarios para instalar, levantar, testear, lintear las diferentes partes del repositorio. Para la base de datos necesito que simplifiquemos los comandos a maximo unos 5, se pueden utilizar scripts de bash o powershell para hacerlo mas sencillo y unificar comportamientos de diferentes comandos en uno solo.»

Alcance autorizado: reescribir los objetivos del `Makefile` y concentrar la infraestructura local en como máximo cinco comandos, con un script si hace falta unificar comportamientos. Actualizar solo la documentación que describe esos comandos para que coincida con el resultado. No cambia el esquema, los roles, el Compose ni la geometría. Los hallazgos de cada archivo siguen abiertos.

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | Decisión |
|---|---|---|
| `Makefile` | Inventario AUD-2026-10-29-002, revisión sin hallazgos | Sustituir los objetivos de infraestructura por cinco y añadir instalar, levantar, probar y lintear |
| `scripts/BaseLocal.py` | Archivo nuevo, fuera del inventario | Unificar las operaciones de Docker, respaldo y reinicio |
| `README.md` | B-17; también AUD-2026-10-13-001 | Describir los objetivos nuevos |
| `.env.example` | Inventario AUD-2026-10-29-002, revisión sin hallazgos | El comentario de OIDC apunta a `make db-up` |
| `docs/AppBackend/OPERACION_Y_PRUEBAS.md` | B-02, B-17 | Arranque, respaldo y diagnóstico |
| `docs/AppBackend/DATABASE.md` | B-02 | Los cinco objetivos y el reinicio |
| `docs/AppBackend/MODULOS.md` | B-17 | Ficha del Makefile y del script |
| `docs/AppFrontend/OPERACION_Y_PRUEBAS.md` | Revisión sin hallazgos | `make web` |
| `docs/BlenderPlugin/OPERACION_Y_PRUEBAS.md` | Revisión sin hallazgos | `make empaquetar` y `make test-blender` |
| `docs/Agents/INVENTARIO.md` | B-17 | Descripción del Makefile y del script nuevo |
| `docs/Agents/REGISTRO_CAMBIOS.md` | B-01 | Esta entrega |
| `tests/README.md` | B-17 | `make test` y `make test-blender` |
| `docs/Agents/SIMBOLOS.md` de las tres áreas y `docs/BlenderPlugin/CONFIGURACION_GENERADA.md` | Los regenera `GenerarIndices.py` | Sin edición manual |

## Decisión

Los hallazgos no se cierran. Esta autorización solo habilita el Makefile, el script nuevo y las frases de la documentación que quedarían falsas si siguieran citando los objetivos antiguos.

## Verificación

Se completa en el registro de cambios de esta entrega.
