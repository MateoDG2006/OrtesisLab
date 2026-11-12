# Calidad · Pruebas y estándares

**Estado:** propuesta. La línea base se **ejecutó el 2026-10-29** sobre `e56df68`.

## Línea base actual

Comando: `.venv/Scripts/python.exe -m unittest discover -s tests`. Resultado:
`Ran 49 tests … FAILED (errors=3, skipped=8)`.

| Módulo | Casos declarados | Cargados | Aprobados | Omitidos | No cargan | Causa |
|---|---|---|---|---|---|---|
| `nucleo/test_nucleo.py` | 14 | 14 | 14 | 0 | 0 | — |
| `geometria/test_escala_malla.py` | 12 | 12 | 12 | 0 | 0 | — |
| `geometria/test_refinador_malla.py` | 3 | 3 | 3 | 0 | 0 | — |
| `geometria/test_suavizado_borde.py` | 4 | 4 | 4 | 0 | 0 | — |
| `geometria/test_superficie_abierta.py` | 5 | 5 | 5 | 0 | 0 | — |
| `persistencia/test_propiedad_datos.py` | 8 | 8 | 0 | 8 | 0 | Sin `ORTESISLAB_TEST_*`, base ni esquema |
| `aplicacion_web/test_generador_web.py` | 13 | 0 | — | — | 13 | `ImportError` (B-01) |
| `persistencia/test_almacen_import.py` | 6 | 0 | — | — | 6 | `ImportError` (B-01) |
| `persistencia/test_lotes_trabajador.py` | 8 | 0 | — | — | 8 | `ImportError` (B-01) |
| **Total** | **73** | **46** | **38** | **8** | **27** | |

Los casos declarados por archivo se contaron con `grep -c '    def test'`, y el
total de aprobados es coherente con 38 = 14 + 12 + 3 + 4 + 5. No se ejecutaron `tests/blender/*.py` (Blender no está
disponible).

La documentación canónica afirma «73 pruebas, 50 aprobadas y 23 omitidas,
2026-10-13». Esa cifra **no se reproduce** en `e56df68`.

## Qué cubre cada archivo y qué falta

| Archivo | Cubre | No cubre (huecos) |
|---|---|---|
| `nucleo/test_nucleo.py` | Equivalencia con la referencia, catálogo, validación de parámetros, importación sin Blender, volumen y material | Reproducción de A-04, A-05, A-15 |
| `geometria/test_escala_malla.py` | Factores decimales, desactivación, alcance del paso, presupuesto | Cambio de tamaño físico (A-14) como criterio de aceptación |
| `geometria/test_refinador_malla.py` | Subdivisión, recorte refinado, escala y paso | Éxito sin alcanzar el paso (A-06) |
| `geometria/test_suavizado_borde.py` | Dientes, tramo recto, borde corto, marco | Unidades del filtro de normales (A-22) |
| `geometria/test_superficie_abierta.py` | Pared sin tapas, inversión, rechazo de capas, duplicados, sueltos y orientación | Vértice no manifold (A-05) |
| `aplicacion_web/test_generador_web.py` | Combinaciones y límites, semilla, STL, lectura STL/NPZ, autoescala con import persistido, expansión e índices inválidos | NPY con cabecera grande (A-01), STL ASCII patológico |
| `persistencia/test_almacen_import.py` | Import con URL y hash, deduplicación, rechazo, aislamiento, plantilla, migración de subidas | Fallo S3 a mitad de import (B-06), carrera de deduplicación (B-07), cuota (B-05) |
| `persistencia/test_lotes_trabajador.py` | Idempotencia, cuota de lotes, lote parcial, lease vencido, cancelación, sin Redis, restauración, conciliación | Cancelación durante la confirmación (B-20), `CHECK` frente a YAML (B-08) |
| `persistencia/test_propiedad_datos.py` | Acceso entre usuarios, FK compuestas, URL en `ready`, revisión de preferencias, permisos de rol, sesiones | Purga de sesiones (B-13) |
| `blender/blender_superficie_abierta.py` | Complemento en Blender: superficie abierta | Exportación de la malla evaluada (A-08), fallo de voxel (A-09) |
| `blender/blender_paquete_zip.py` | ZIP aislado | Coincidencia de `LEEME.md` (B-16) |

### Pruebas inexistentes que la evaluación considera necesarias

1. Humo: importar `web.GenerateModelsApp`, `web.jobs.TrabajadorGeneracion` y
   `scripts/MigrarSubidas.py` (B-01).
2. Migración: `alembic upgrade head` + `alembic check` sobre base vacía (B-02).
3. E2E de navegador: login OIDC de pruebas, subida, lote, comparación,
   descarga, historial, restaurar (no hay herramienta configurada).
4. Carga: N subidas y M pestañas sondeando, con medición de latencia (B-04, B-10).
5. Contrato del visor: STL con contador incoherente (A-21).

## Herramientas y estándares

| Aspecto | Estado en el repositorio |
|---|---|
| Versión de Python | `>=3.14` (`pyproject.toml`), `.python-version` = 3.14 |
| Gestor | `uv` con `uv.lock`; `reflex.lock/` para el frontend (bun) |
| Linter / formato | **Ninguno** configurado |
| Tipos | Anotaciones parciales; sin `mypy`/`pyright` |
| Pruebas | `unittest` de la biblioteca estándar; `moto[server]` como dependencia de desarrollo para S3 en pruebas |
| Convenciones | Métodos y clases en PascalCase, también en métodos estáticos; textos y comentarios en español; DTO `dataclass(frozen=True)`; enums `StrEnum` |
| Docstrings | Formato «Entrada / Proceso / Salida / Errores / Efectos» en los métodos públicos clave; incompleto (A-18) |
| Documentación | `docs/Agents/ESTANDAR_DOCUMENTACION.md` y `GenerarIndices.py` (inventario y símbolos); regla de bloqueo por auditoría |
| CI | Ninguno para calidad (B-03) |
| Dependencia interna frágil | `web/PaginaComparacion.py` importa `reflex_base.vars.base.Var` (API interna de Reflex) |

### Propuesta mínima de estándar ejecutable

No está aplicada. Requiere una tarea aparte y autorización por el bloqueo.

1. `ruff` (lint + formato) con la excepción de nombres PascalCase declarada
   (`N802`, `N803`).
2. `pyright` en modo básico sobre `web/` y `GenerateModelsApp/` con una línea
   base congelada.
3. Un workflow de CI que ejecute las pruebas de humo, `unittest`,
   `GenerarIndices --comprobar` y, cuando haya migraciones, PostgreSQL de
   servicio.
