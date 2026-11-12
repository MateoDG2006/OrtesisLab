# RES-2026-11-12-001 — Cierre de issues AUD-2026-10-13-001 (plan autorizado)

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: EN_CURSO (autorización vigente; cierres por hallazgo en issue-1…issue-9)
Responsable: agente de implementación, por instrucción del usuario (Mateo Del Giudice)

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12, al aprobar el plan
«Cierre de las 9 issues de GitHub»:

> «Implement the plan as specified»

Alcance autorizado: editar los archivos listados en ese plan para cerrar los
hallazgos A-01 a A-22 y el prerrequisito de importación (B-01). También
autoriza `RIESGO_ACEPTADO` de la lectura anónima del STL (A-02 / issue #2),
con fecha de revisión **2027-05-12**. No habilita cambios ajenos a ese alcance
ni cierra B-02 a B-22 salvo lo que el plan indique (B-01; tramo STL anónimo de
B-14; B-03 y Three.js de B-14 en la issue #8).

## Archivos y hallazgos (alcance EN_CURSO)

| Archivo desde la raíz | Hallazgos |
|---|---|
| `web/persistence/Contratos.py` | B-01 |
| `web/LectorSuperficie.py` | A-01, A-03, A-16 |
| `GenerateModelsApp/Superficie.py` | A-01, A-03, A-12 |
| `GenerateModelsApp/util/Utilidades.py` | A-11, A-12 |
| `GenerateModelsApp/config/limites.json` | A-03, A-11 |
| `GenerateModelsApp/constants/Paterns.py` | A-03, A-11, A-17 |
| `GenerateModelsApp/RefinadorMalla.py` | A-03, A-06 |
| `GenerateModelsApp/Excepciones.py` | A-01…A-15 (tipos de error) |
| `config/trabajador.yaml` | A-03 |
| `config/cache.yaml` | A-12 |
| `web/jobs/TrabajadorGeneracion.py` | A-03, A-07 |
| `web/services/GeneradorGeometrico.py` | A-03, A-07 |
| `web/GeneradorWeb.py` | A-07, A-15, A-17 |
| `web/EstadoApp.py` | A-17 |
| `web/PaginaComparacion.py` | A-20 |
| `web/cache/CacheRedis.py` | A-12 |
| `GenerateModelsApp/Malla.py` | A-04, A-05, A-17, A-22 |
| `GenerateModelsApp/ValidacionMalla.py` | A-05, A-07, A-08, A-17 |
| `GenerateModelsApp/Cascaron.py` | A-04, A-17 |
| `GenerateModelsApp/EscalaMalla.py` | A-14 |
| `GenerateModelsApp/SuavizadoBorde.py` | A-22 |
| `GenerateModelsApp/Exportacion.py` | A-08, A-10, A-15 |
| `GenerateModelsApp/Modeling.py` | A-07, A-13 |
| `GenerateModelsApp/Objeto.py` | A-09, A-17 |
| `GenerateModelsApp/Interfaz.py` | A-09, A-10 |
| `GenerateModelsApp/ReparacionMalla.py` | A-17 |
| `GenerateModelsApp/config/parametros_defecto.json` | A-17, A-18 |
| `assets/visor.html` | A-20, A-21, B-14 |
| `pyproject.toml` | A-18, A-19 |
| `scripts/IniciarConsola.py` | A-18 |
| `tests/blender/blender_paquete_zip.py` | A-19 |
| Documentación canónica y `docs/Agents/REGISTRO_CAMBIOS.md` | mantenimiento |

Archivos nuevos del plan (no estaban en el inventario congelado al nacer):
`GenerateModelsApp/InspeccionNpz.py`, `GenerateModelsApp/contratos.py`,
`GenerateModelsApp/ValidacionSolido.py` (si hace falta), pruebas nuevas,
`.github/workflows/pruebas.yml`, `assets/vendor/three-0.169.0.module.js`,
resolves de cierre por issue.

## Decisión

Abrir este resolve `EN_CURSO` para desbloquear las correcciones del plan.
Cada issue deja su resolve de cierre con evidencia. Este archivo se actualiza
al cerrar B-01 y al consolidar el índice en la issue #9.

## Verificación (parcial, prerrequisito / B-01)

2026-11-12, venv `.venv`:

```
.venv\Scripts\python.exe -c "import web.GenerateModelsApp; import web.jobs.TrabajadorGeneracion; from web.persistence.Contratos import ESQUEMA_PARAMETROS, ESQUEMA_NORMALIZACION, VERSION_LECTOR, VERSION_EXPORTADOR; print(...)"
→ 1 1 LectorSuperficie-1 GeneradorWeb.Stl-1

.venv\Scripts\python.exe -m unittest tests.aplicacion_web.test_humo_import -v
→ 2 OK
```

B-01 queda cubierto en este resolve; el cierre formal de B-01 se confirma
cuando la suite carga sin `_FailedTest` al final del plan.
