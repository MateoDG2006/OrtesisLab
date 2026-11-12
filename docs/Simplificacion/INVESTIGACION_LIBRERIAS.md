# Investigación: librerías que pueden asumir código propio

**Fecha:** 2026-11-12. **Estado:** investigación; no describe código implementado.
**Base revisada:** `9282cc0` en `master`, con cambios ajenos sin confirmar en
`apps/web/web/EstadoApp.py`, `PaginaComparacion.py` y `core/config/web.yaml`
(rediseño de lotes en curso). El plan derivado está en
[PLAN_SIMPLIFICACION.md](PLAN_SIMPLIFICACION.md).

## Método

1. Se leyeron completos los módulos de `apps/ortesis-plugin/OrtesisLabPlugin/`,
   `apps/web/web/`, `apps/db/`, `scripts/`, `core/config/`, `tests/` y `Makefile`.
   Se anotaron las piezas escritas a mano, con su archivo, tamaño y pruebas.
2. Para cada pieza se buscó, en este orden:
   - una función de una dependencia ya instalada (SQLAlchemy, boto3, Reflex,
     NumPy, three.js, stdlib);
   - una librería madura, con versión y ruedas comprobadas en PyPI el
     2026-11-12.
3. Se descartaron las librerías que solo ahorran unas pocas líneas: añadir una
   dependencia cuesta más que mantener 10 líneas legibles.

**Restricción del complemento.** `bl_info` exige Blender ≥ 5.0. Blender 5.0
incluye Python 3.11 (`cp311`) y Blender 5.1+ incluye Python 3.13
([notas de 5.1](https://developer.blender.org/docs/release_notes/5.1/python_api/)).
Una dependencia del núcleo tiene que viajar como rueda dentro de la extensión,
mediante `blender_manifest.toml` y `wheels = [...]`
([manual de Blender](https://docs.blender.org/manual/en/latest/advanced/extensions/python_wheels.html)).
Por eso las librerías en Python puro (`py3`) cuestan poco y las compiladas
obligan a empaquetar una rueda por plataforma.

## Defectos encontrados durante la revisión

Estos defectos no dependen de ninguna librería, pero cualquier refactorización
los va a encontrar. Todos están comprobados en el código actual.

| # | Defecto | Evidencia | Efecto |
|---|---|---|---|
| D-1 | `LIMITES_POSITIVOS` exige `min_plausible_surface_extent_mm` y `max_plausible_surface_extent_mm`, que no están en `core/config/limites.json` | `util/Utilidades.py:189-190` | `Configuracion.ValorLimite(...)` lanza `KeyError` y rompe casi todo el núcleo. Parece un resto del autoescalado retirado |
| D-2 | `ConfiguracionBackend.ValidarEnArranque` no existe | `apps/web/web/OrtesisLabApp.py:30` | `AttributeError` en el arranque. El `try` solo captura `ErrorPersistencia` |
| D-3 | `RepositorioImports.ColgadosVencidos` no existe | `jobs/ConciliadorArchivos.py:77` | La conciliación falla siempre, y el error escapa del bucle del trabajador |
| D-4 | `ServicioVersiones.CLAVES_SOLO_VOXEL` no existe | `EstadoHistorial.py:261` | La comparación de versiones falla |
| D-5 | `RepositorioHistorial.PurgarAntiguos` hace `DELETE`, pero el diseño de roles solo concede `SELECT, INSERT` | `RepositorioHistorial.py:30-33`, `tests/persistencia/test_propiedad_datos.py:95-96` | La purga falla con los permisos documentados |
| D-6 | No hay migraciones Alembic ni `GRANT` sobre tablas | `apps/db/alembic/versions/` solo tiene `.gitkeep` | Las pruebas de persistencia siempre se saltan, y por eso no detectan D-3 a D-5 |

## Inventario por responsabilidad

**Cómo leer las tablas.** LOC son líneas aproximadas del código propio que
desaparecerían o se reducirían. **Veredicto:**

- **Adoptar:** la librería resuelve la responsabilidad entera con menos riesgo.
- **Usar lo instalado:** la solución ya está en una dependencia actual.
- **Opcional:** el beneficio existe, pero el coste o el riesgo son comparables.
- **Mantener:** el código es de dominio o es más corto que la alternativa.

### 1. Cola de generación y trabajador

| Código actual | LOC | Responsabilidad |
|---|---|---|
| `persistence/repositorios/RepositorioLotes.py:219-503` | ~280 | Selección `FOR UPDATE SKIP LOCKED`, reserva y *lease*, latido, liberación con reintento y `available_at`, abandono de *leases* vencidos |
| `services/ServicioLotes.py:221-266` | ~45 | Retraso exponencial `ESPERA_REINTENTO_S * 2^(n-1)` y supervisor de vencimientos |
| `jobs/TrabajadorGeneracion.py:71-153` | ~80 | Bucle con `Event.wait`, hilo de latido, planificador periódico con `monotonic` |
| `scripts/EjecutarTrabajador.py` | 51 | `argparse` y señales |

**Candidatas:**

| Librería | Versión (PyPI) | Backend | Cubre |
|---|---|---|---|
| [procrastinate](https://procrastinate.readthedocs.io/) | 3.11.0, `py3` | PostgreSQL (psycopg 3, `LISTEN/NOTIFY`, `SELECT … FOR UPDATE`) | Reintentos con estrategia exponencial, tareas periódicas `@app.periodic(cron=…)`, latido del trabajador y recuperación de trabajos estancados (`get_stalled_jobs` + `retry_job`), cancelación, bloqueos de cola, CLI del trabajador |
| [pgqueuer](https://pypi.org/project/pgqueuer/) | 2.0.0, `py3` | PostgreSQL | Equivalente, más reciente y con menos historial |
| [rq](https://pypi.org/project/rq/) 3.0.0 / [dramatiq](https://pypi.org/project/dramatiq/) 2.2.1 | `py3` | Redis | Cola completa. Hoy Redis es **opcional**: el código funciona sin él (`test_lotes_trabajador.py`, caso sin Redis) |

**Veredicto: adoptar procrastinate.** PostgreSQL ya es obligatorio y Redis no lo
es, así que una cola sobre Redis convertiría a Redis en un punto de fallo
nuevo. procrastinate cubre *lease*, latido, reintento, periodicidad y CLI.

Quedan como dominio:

- las tablas `batches`/`batch_items`/`generation_attempts`, que son estado de
  producto e historial;
- `Recalcular` (agregado de estado del lote);
- la clave de idempotencia con hash de petición;
- las cuotas por usuario con *advisory lock*.

procrastinate añade su propio esquema, que tendrá que instalarse con una
migración.

### 2. E/S y validación de mallas

| Código actual | LOC | Responsabilidad |
|---|---|---|
| `Exportacion.py:38-59` (`_EscribirStl`) | ~22 | Escritura de STL binario |
| `apps/web/web/GeneradorWeb.py:316-345` | ~30 | **Segundo** escritor de STL binario, con su triangulación en abanico |
| `apps/web/web/LectorSuperficie.py:88-139` | ~50 | Lector de STL binario y ASCII, y soldado de vértices con `np.unique` |
| `ValidacionSolido.py:23-76` | ~55 | Triangulación, componentes conexas (union-find), aristas abiertas o no-manifold, áreas degeneradas |
| `Cascaron.py:162-186` (`VolumenMm3`) | ~25 | Volumen por tetraedros firmados. Duplica la triangulación de `ValidacionSolido` |
| `Malla.py:27-145, 160-194` | ~150 | Normales por vértice, validación topológica (degeneradas, duplicadas, bordes, no-manifold, orientación, conexidad) y comprobación de abanico por vértice |
| `RefinadorMalla.py:36-144` | ~95 | Partición de aristas largas hasta el paso del patrón |
| `SuavizadoBorde.py:108-141` (`_Bucles`) | ~35 | Extracción de bucles de borde |
| `ValidacionSolido.py:79-120` | ~40 | Heurística O(n²) de solapes coplanares, limitada a 800 triángulos. **No detecta intersecciones reales** |

**Candidatas:**

| Librería | Versión | Licencia / ruedas | Cubre |
|---|---|---|---|
| [trimesh](https://trimesh.org/) | 5.2.0, `py3` (solo requiere NumPy) | MIT; viaja a Blender sin compilar | `trimesh.load`/`export` STL binario y ASCII, `merge_vertices`, `nondegenerate_faces`/`unique_faces`, `is_watertight`, `is_winding_consistent`, `fix_normals`, `volume`, `vertex_normals`, `outline()` (bucles de borde), `split`/`graph.connected_components`, `remesh.subdivide_to_size` |
| [networkx](https://pypi.org/project/networkx/) | 3.7, `py3` | BSD; ya está en `uv.lock` (por moto) | Motor de grafos que trimesh usa para `split` sin SciPy |
| [manifold3d](https://pypi.org/project/manifold3d/) | 3.5.4, ruedas cp311…cp314 | Apache-2.0 | Booleanas y volúmenes garantizados como variedad. **No** desplaza superficies abiertas ni recorta por campo escalar |
| [numpy-stl](https://pypi.org/project/numpy-stl/) | 4.1.3, `py3` | BSD | Solo E/S STL. Lo cubre trimesh |
| [pymeshlab](https://pypi.org/project/pymeshlab/) | 2025.7.post1, compilada | **GPL-3** | Detección real de autointersecciones. La licencia contamina la distribución del complemento |

**Veredicto: adoptar trimesh** para E/S STL, volumen, comprobaciones de
estanqueidad, orientación y conexidad, y bucles de borde.

`RefinadorMalla` puede pasar a `subdivide_to_size` **solo** si se acepta otra
topología de refinado: divide todas las aristas de cada cara, no las ocho
configuraciones actuales. Hay que verificarlo contra
`core/config/comprobacion_geometrica.json` y `tests/geometria/test_refinador_malla.py`.

Se mantienen:

- `Cascaron.Recortar` (recorte por campo escalar) y `Cascaron.Engrosar`
  (cascarón de una superficie abierta con paredes en el borde): ninguna
  librería revisada lo hace para superficies abiertas;
- el filtro FFT de `SuavizadoBorde`;
- la geodésica de `Malla._Geodesica`: son 30 líneas de Dijkstra con `heapq`.

La heurística de solapes no se reemplaza con pymeshlab por la licencia GPL.
Hay dos opciones:

- declarar «autointersecciones no comprobadas» en el modo sin Blender;
- usar `mathutils.bvhtree`, que ya usa `ValidacionMalla` dentro de Blender.

Dentro de Blender, `ReparacionMalla` ya usa `bmesh.ops`, que es la plataforma.
Solo sobran sus búsquedas de componentes (BFS) duplicadas: `ReparacionMalla.py:29-47`,
`Objeto.py:51-72` y `ValidacionMalla.py:27-45`.

### 3. Patrones de nervaduras

`constants/Paterns.py:103-116` compara cada punto con todas las semillas, con
coste O(puntos × semillas), y tiene un recurso de corrección en `:95-99`.
[SciPy](https://pypi.org/project/scipy/) `spatial.cKDTree.query(k=2)` daría las
dos semillas más cercanas y la distancia a su bisectriz con menos código.

**Veredicto: opcional.** SciPy 1.18 necesita Python ≥ 3.12, así que **no tiene
rueda para Blender 5.0 (cp311)**. Habría que exigir Blender ≥ 5.1 y empaquetar
unos 40 MB por plataforma. Solo conviene si el rendimiento del patrón se mide
como problema.

### 4. Configuración, ajustes y contratos de datos

| Código actual | LOC | Responsabilidad |
|---|---|---|
| `apps/web/web/Ajustes.py` | 82 | Descriptor `Variable`, obligatorias y valores por defecto, `bool` a mano, `load_dotenv` |
| `apps/web/web/ConfiguracionBackend.py` + ~15 módulos | 21 + accesos | YAML sin esquema, leído con `["clave"]` al importar. Regla entre archivos (`maximo_variantes` ≤ `lotes.maximo_items`) solo en un comentario |
| `util/Utilidades.py:251-322` | ~70 | Claves exactas, límites tipados (enteros, positivos, razones, mín ≤ máx). D-1 es un fallo de esta sincronización manual |
| `Modeling.py:80-128` (`ValidarOpciones`) | ~50 | Validación de las 17 opciones |
| `contratos.py` | 69 | Segunda validación, más débil, de las mismas opciones y de las fichas. Solo la usan pruebas |
| `Interfaz.py:60-96` | — | Tercera copia de los rangos, como `min`/`max` de propiedades Blender |
| `EstadoApp.py:588-621` (`_Opciones`, `_Numero`) | ~35 | Cuarta conversión y validación, desde texto del formulario |
| `constants/Materials.py:19-45` | ~25 | Validación de `Material` |
| `persistence/Contratos.py` | 284 | 16 DTO congelados sin validación |

**Candidatas:**

- [pydantic](https://pypi.org/project/pydantic/) 2.14.3 / [pydantic-settings](https://pypi.org/project/pydantic-settings/) 2.16.2.
  Hoy solo llegan por `moto` (desarrollo), no en ejecución. Ofrecen campos
  tipados, `SecretStr`, prefijo de entorno, `.env`, fuente YAML
  (`YamlConfigSettingsSource`) y validadores cruzados.
- [msgspec](https://pypi.org/project/msgspec/) 0.22.0 es más rápido, pero no
  carga ajustes.

**Veredicto: adoptar pydantic-settings en la web**, para `Ajustes` y un modelo
por YAML validado en el arranque. Ese modelo es el `ValidarEnArranque` que
falta (D-2).

**En el núcleo: un único modelo `Opciones`**, que ocupe el lugar de
`ValidarOpciones`, `contratos.ValidarOpciones`, `_Numero`/`_Opciones` y las
claves de `limites.json`. Cuesta una rueda compilada de `pydantic-core` por
plataforma en la extensión Blender.

Alternativa sin dependencias para el núcleo: `dataclasses` con `__post_init__`
y una sola tabla de rangos que lean Modeling, Interfaz y la web. Cualquiera de
las dos opciones elimina la cuádruple copia, que es el problema real.

### 5. Persistencia

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `Modelos.py:85-104` (`_Valores`, `_Check`) más ~20 usos, sincronizados a mano con `enums/*` | ~40 | `sqlalchemy.Enum(StrEnum, native_enum=False, create_constraint=True, values_callable=…)` genera el `CHECK` | **Usar lo instalado** |
| `RepositorioBase.py:23-52` y conversiones fila→DTO en cada repositorio (`RepositorioResultados.py:61-84`, `RepositorioLotes.py:505-518`, …) | ~120 | Mapeo ORM con `MappedAsDataclass`, para que la entidad sea el DTO y sobren `persistence/Contratos.py` y `_Construir` | **Opcional**: es el mayor ahorro de persistencia, pero cambia todos los repositorios |
| `RepositorioHistorial.py:61-137` y `ServicioHistorial.py:41-52` (paginación por conjunto de claves y cursor base64) | ~90 | [sqlakeyset](https://pypi.org/project/sqlakeyset/) 2.0, `select_page` con `select` Core y marcadores serializados | **Adoptar** |
| `RepositorioPreferencias.py:28-49` (bloqueo optimista) | ~20 | `version_id_col` solo funciona con el ORM | **Mantener** salvo que se adopte el ORM |
| `ConexionPostgres.py:87-98` (reintento por `SerializationFailure`) | ~12 | [tenacity](https://pypi.org/project/tenacity/) | **Mantener**: no compensa una dependencia por 12 líneas |
| Filtro `user_id ==` repetido en cada consulta y `_DelUsuario` | — | Políticas RLS de PostgreSQL | **Opcional**: más seguro, pero es un cambio de seguridad que exige migración y pruebas propias |
| Roles y esquema duplicados en `apps/db/init/01_roles.sh` y `preparar_base.sql`; sin `GRANT` de tablas (D-6) | — | Una migración Alembic con roles, `GRANT` y esquema de procrastinate | **Usar lo instalado** |

### 6. Almacenamiento de objetos

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `storage/StorageS3.py:59-70`: `head_object` tras subir, para comparar tamaño y SHA-256 | ~12 | `put_object(ChecksumAlgorithm="SHA256", ChecksumSHA256=…)`: el servidor rechaza el objeto si no coincide | **Usar lo instalado** (boto3) |
| `jobs/ConciliadorArchivos.py`: borrado de objetos huérfanos y de *staged* viejos | ~60 de 137 | Reglas de ciclo de vida S3/MinIO (ILM) por prefijo o etiqueta | **Opcional**: solo si los objetos *staged* tienen un prefijo o etiqueta propios. El marcado en base de datos se mantiene |
| Abstracción `AlmacenamientoPrivado` | 84 | fsspec / [obstore](https://pypi.org/project/obstore/) | **Mantener**: hay un único backend |

### 7. Caché

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `Superficie.py:40, 132-145`: LRU con `OrderedDict` que respeta `max_refined_cache_entries` pero **ignora `max_refined_cache_bytes`** | ~20 | [cachetools](https://pypi.org/project/cachetools/) 8.0, `LRUCache(maxsize, getsizeof=lambda v: v.nbytes)` (`py3`) | **Adoptar**: corrige el límite de bytes ignorado y viaja a Blender sin compilar |
| `cache/CacheRedis.py`: cliente perezoso, cortacircuitos de 5 líneas, serialización NPZ, TTL | 101 | dogpile.cache, cashews, pybreaker | **Mantener**: es pequeño y la serialización NPZ es propia |
| `Modeling.py:62-78, 218-233`: memoización de volumen con *setters* | ~25 | `functools.cached_property` | **Usar lo instalado** |

### 8. Registro (logging)

`util/Utilidades.py:25-103` configura a mano los manejadores de consola y
archivo desde `registro.json`. `logging.config.dictConfig` hace lo mismo con
el JSON como diccionario. **Usar lo instalado** (stdlib): ahorra unas 60 líneas.

`structlog` no se justifica, porque no se pidió registro estructurado.

`Excepciones.py` define unas 40 clases cuya base escribe en el registro al
construirse. No es tarea de una librería, pero el registro debería hacerse
donde se captura el error, no en el constructor.

### 9. Lectura de NPZ

`InspeccionNpz.py:23-60` vuelve a implementar el análisis de la cabecera NPY.
`numpy.lib.format.read_magic` y `read_array_header_1_0`/`_2_0` son públicos.
**Usar lo instalado.** Además, el módulo no tiene llamadores en la aplicación,
solo `tests/geometria/test_carga_presupuesto.py`. La guardia contra bombas zip
real está en `LectorSuperficie.py:71-86`.

### 10. Interfaz web y visor

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `assets/visor.html:90-114`: lector de STL binario | ~25 | `STLLoader` de los complementos de three.js 0.169 (`examples/jsm/loaders/STLLoader.js`), que también lee ASCII | **Adoptar**: misma versión ya vendida, solo se añade el archivo |
| `assets/visor.html:138-217`: cámara orbital | ~80 | `OrbitControls` (`listenToKeyEvents` para el teclado) | **Adoptar**. Se mantienen la lista de orígenes permitidos y el tope de 64 MB (`:17-88`), porque son una frontera de confianza |
| `EstadoApp.py:105-203`: 25 manejadores `set_*` | ~100 | Reflex 0.9 dejó de generar *setters* por defecto (`state_auto_setters` está obsoleto y se elimina en 1.0, según la [guía 0.8→0.9](https://reflex.dev/blog/upgrading-reflex-0-8-to-0-9)). La vía estable es `rx.form` con `on_submit`, que recibe el diccionario completo y lo valida con el modelo `Opciones` del §4 | **Usar lo instalado**. Hay un rediseño en curso en estos archivos |
| Mensajes con `rx.text`/`rx.callout` | — | `rx.toast` (sonner ya instalado) | Opcional, cosmético |
| Tablas `rx.table` + `rx.foreach` y paginación manual | ~50 | `reflex-ag-grid` | **Mantener**: la paginación pasa a sqlakeyset en el servidor y la tabla es simple |
| `PaginaComparacion.py:367-384`: usa `Var(_js_expr=…)` y `_get_all_var_data` privados | ~18 | Var con f-string pública | **Usar lo instalado**: evita una API privada |

### 11. Pruebas

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `tests/persistencia/apoyo_persistencia.py`: lectura de URL, sondeo, `skipIf`, puerto libre, servidor moto, Redis db 15, cambio de rol | 181 | [pytest](https://pypi.org/project/pytest/) 9.2 con *fixtures*, y [testcontainers](https://pypi.org/project/testcontainers/) 4.15 (`PostgresContainer`, `MinioContainer`, `RedisContainer`). Alternativa: [pytest-postgresql](https://pypi.org/project/pytest-postgresql/) 10.0 | **Adoptar**. Hoy esas pruebas siempre se saltan (D-6); con contenedores efímeros se ejecutan de verdad |
| `SesionPrueba` (`:48-56`) | ~10 | `Session.begin()` de SQLAlchemy | **Usar lo instalado** |
| Nombre `tests/aplicacion_web` para esquivar el *shadowing* de `unittest` | — | `--import-mode=importlib` de pytest | Consecuencia de adoptar pytest |
| `tests/assets/*.log` y `resultado_blender.json` versionados | — | Artefactos de CI | Eliminar: el propio `tests/README.md` dice que no prueban la versión actual |

### 12. Empaquetado, entorno y herramientas

| Código actual | LOC | Alternativa | Veredicto |
|---|---|---|---|
| `scripts/EmpaquetarBlender.py` y `bl_info` | 36 | `blender_manifest.toml` y `blender --command extension build --split-platforms` | **Adoptar**: es además el único mecanismo oficial para llevar ruedas (trimesh, cachetools) dentro del complemento |
| `sys.path.insert` en `rxconfig.py`, `alembic/env.py`, `scripts/IniciarConsola.py`, `EjecutarOrtesisLab.py`, `EjecutarTrabajador.py`, `MigrarSubidas.py` | ~6 sitios | Espacio de trabajo uv (`[tool.uv.workspace]` con `apps/ortesis-plugin` como paquete editable) | **Usar lo instalado** |
| `scripts/BaseLocal.py`: envoltorio de `docker compose` | 229 | `docker compose` con perfiles y *healthchecks*, con objetivos de `make` | **Opcional**. El respaldo y la restauración (`pg_dump`, `mc mirror`) y la confirmación siguen siendo propios |
| `Makefile` | 84 | poethepoet / just | **Mantener**: funciona y cambiarlo no reduce código |
| `docs/Agents/Scripts/GenerarIndices.py`: índice de símbolos por AST | ~40 de 260 | Se solapa con `.codegraph/`; pdoc 16 / mkdocstrings | **Mantener** mientras la política documental exija `SIMBOLOS.md` |

## Descartadas expresamente

| Candidata | Motivo |
|---|---|
| tenacity, pybreaker, Babel, canonicaljson, limits | Cada una sustituiría menos de 15 líneas propias claras |
| pymeshlab | Licencia GPL-3 |
| SciPy en el núcleo | Sin rueda cp311 para Blender 5.0; unos 40 MB por plataforma |
| rq, arq, dramatiq, celery | Harían obligatorio Redis, que hoy es opcional |
| reflex-local-auth | La autenticación ya está en authlib (OIDC) con sesiones de servidor revocables |
| fsspec, obstore | Hay un único backend S3 |
| reflex-ag-grid | Las tablas son simples |
| structlog | No hay requisito de registro estructurado |

## Fuentes

- Versiones y ruedas consultadas en `https://pypi.org/pypi/<paquete>/json` el
  2026-11-12.
- [Blender: ruedas Python en extensiones](https://docs.blender.org/manual/en/latest/advanced/extensions/python_wheels.html)
  y [notas de la API Python de 5.1](https://developer.blender.org/docs/release_notes/5.1/python_api/).
- [procrastinate: reintentar trabajos estancados](https://procrastinate.readthedocs.io/en/stable/howto/production/retry_stalled_jobs.html).
- [Reflex: actualizar de 0.8 a 0.9](https://reflex.dev/blog/upgrading-reflex-0-8-to-0-9).
- [trimesh](https://trimesh.org/), [manifold](https://github.com/elalish/manifold)
  y [testcontainers-python](https://github.com/testcontainers/testcontainers-python).
