# Operación y pruebas del backend

## Entorno reproducible

Desde la raíz, con uv, Docker Compose y `make` disponibles:

```powershell
make install     # Python 3.14, uv sync --locked --all-groups y .env de ejemplo si faltan
make up          # PostgreSQL :5433, MinIO :9000/:9001, Redis :6379, bucket y alembic upgrade head
make worker      # otra terminal
make web         # otra terminal; http://localhost:3000
```

Variables de la aplicación: [`.env.example`](../../.env.example). Todas se declaran en un solo lugar, la clase `Ajustes` de [`web/Ajustes.py`](../../apps/web/web/Ajustes.py), y ningún otro archivo lee el entorno. `Cargar()` lee ese `.env` con python-dotenv (UTF-8, con o sin BOM), sin pisar variables que el proceso ya tenga. Esos valores quedan en el entorno del proceso y las referencias `$` se sustituyen. Una variable sin valor por defecto es obligatoria: leerla sin definirla, o con valor vacío, lanza `RuntimeError` («Falta la variable de entorno …»). Ese es el único error de clave ausente; la comprobación ocurre al leer la variable, de modo que cada proceso solo exige las que usa.

| Variable | Defecto | La usa |
|---|---|---|
| `ORTESISLAB_DATABASE_URL` | Obligatoria | Web (rol `ortesislab_app`) y `MigrarSubidas.py` |
| `ORTESISLAB_WORKER_DATABASE_URL` | Obligatoria | Trabajador (rol `ortesislab_worker`) |
| `ORTESISLAB_MIGRATOR_DATABASE_URL` | Obligatoria | Alembic |
| `ORTESISLAB_TEST_DATABASE_URL`, `ORTESISLAB_TEST_WORKER_DATABASE_URL` | Obligatorias | Pruebas de persistencia (si faltan, se omiten) |
| `ORTESISLAB_TEST_MIGRATOR_DATABASE_URL` | Obligatoria | Alembic con `-x base=test` |
| `ORTESISLAB_S3_ENDPOINT`, `ORTESISLAB_S3_ACCESS_KEY`, `ORTESISLAB_S3_SECRET_KEY` | Obligatorias | Web y trabajador |
| `ORTESISLAB_S3_PUBLIC_URL` | Vacía: se usa el endpoint | Base de `object_url` |
| `ORTESISLAB_S3_BUCKET` / `ORTESISLAB_S3_REGION` | `ortesislab` / `us-east-1` | Web y trabajador |
| `ORTESISLAB_REDIS_URL` | Vacía: sin caché | Web y trabajador |
| `ORTESISLAB_APP_URL` | `http://localhost:3000` | Redirección tras registro, login y logout |
| `ORTESISLAB_COOKIE_SECURE` | `false` | `true` añade `Secure` a las cookies |

La web abre PostgreSQL al arrancar. El alta y el acceso son usuario y contraseña en `/auth/registro` y `/auth/login`. Las variables S3 se exigen en la primera operación con el bucket. El trabajador exige las S3 y la suya de base al arrancar. Para añadir una variable se declara un atributo `Variable("ORTESISLAB_…", defecto)` en `Ajustes`, se añade a `.env.example` y se lee con `Ajustes.Cargar().<atributo>`. Las seis URL de base de datos deben escribirse con el driver de SQLAlchemy, `postgresql+psycopg://usuario:clave@host:puerto/base`. Si una no empieza así, leerla lanza `RuntimeError`; el código no las convierte.

### Valores ajustables (`config/*.yaml`)

Los límites, tiempos y tamaños del backend no van en el entorno ni en el código. Están en archivos YAML versionados en [`core/config/`](../../core/config/README.md), uno por área, que lee `ConfiguracionBackend.Cargar("<area>")` ([`web/ConfiguracionBackend.py`](../../apps/web/web/ConfiguracionBackend.py)). Qué hace cada archivo está en [core/config/README.md](../../core/config/README.md). Cada archivo se lee una vez por proceso, al importar el módulo que lo usa, así que un cambio exige reiniciar la web y el trabajador. Si falta un archivo o una clave, el proceso falla al importar ese módulo. Las constantes de contrato no están aquí: versiones de lector y exportador, prefijos de claves, nombre de la cookie y esquema SQL. Los estados, tipos y formatos son `StrEnum` en [`web/enums/`](../../apps/web/web/enums/__init__.py), porque deben coincidir con los `CHECK` del esquema; un YAML solo guarda sus etiquetas visibles.

| Archivo | Claves | Lo usa |
|---|---|---|
| [`persistencia.yaml`](../../core/config/persistencia.yaml) | `conexion`: `reintentos` 3, `pausa_reintento_s` 0.05, `espera_adquisicion_s` 5, `timeout_conexion_s` 10. `lotes`: `maximo_pendientes` 3, `maximo_intentos` 3, `espera_reintento_s` 5. Un lote no tiene tope de variantes. `historial`: `limite_defecto` 25, `limite_maximo` 100, `maximo_comparacion` 3. `cuotas`: `max_bytes_usuario` 1 GiB, `max_imports_ready` 100, `max_subidas_por_hora` 30. `retencion`: `sesiones_dias` 90, `eventos_historial_dias` 730 | `ConexionPostgres`, `Contratos`, `ServicioLotes`, `ServicioHistorial`, `ServicioImports`, `ConciliadorArchivos` |
| [`trabajador.yaml`](../../core/config/trabajador.yaml) | `lease_s` 120, `latido_s` 30, `supervision_s` 30, `conciliacion_s` 600, `capacidad_variante_s` 20. `conciliador`: `horas_staged` 24, `dias_rechazo` 30, `lote_comprobacion` 200, `explorar_bucket` false | `TrabajadorGeneracion`, `ConciliadorArchivos`, `EstadoApp` |
| [`cache.yaml`](../../core/config/cache.yaml) | `ttl_s` 604800 (7 días), `reintento_s` 30, `timeout_s` 0.5, `max_entrada_bytes` 64 MiB | `CacheRedis` |
| [`almacen.yaml`](../../core/config/almacen.yaml) | `timeout_conexion_s` 3, `timeout_lectura_s` 30, `intentos` 3 | `StorageS3` |
| [`sesion.yaml`](../../core/config/sesion.yaml) | `duracion_horas` 12 | `ContextoUsuario` |
| [`web.yaml`](../../core/config/web.yaml) | `intervalo_progreso_s` 1, `espera_crear_s` 600, `maximo_bytes` 50 MiB, `maximo_descomprimido_bytes` 128 MiB; `patrones` (5) y `ejes` (11): clave y etiqueta visible, en el orden de los selectores; `ayudas` (15): texto de ayuda de cada parámetro del formulario, con su rango; `estados_visibles` (5): etiqueta de cada estado de ítem en `/historial` y `/lote` | `EstadoApp`, `GeneradorWeb`, `LectorSuperficie`, `EstadoHistorial`, `PaginaComparacion` |

`generation_batches.total_items` solo exige al menos una variante. `latido_s` debe ser bastante menor que `lease_s`, o el trabajador pierde la reserva mientras construye; el código no lo comprueba.

Los JSON de geometría están en `core/config/`. El ZIP de Blender los copia a `OrtesisLabPlugin/config/`, porque el complemento instalado no ve el monorepo. El Python de Blender no incluye PyYAML, así que esa configuración no pasa a YAML.

En desarrollo, `/auth/registro` y `/auth/login` responden en el backend Reflex (puerto 8000). Con `reflex run --env prod`, la aplicación sirve frontend y backend en un único puerto (3000). Blender no es requisito web ni del trabajador. El visor descarga Three.js desde unpkg.

Para trasladar subidas de la arquitectura anterior: `uv run python scripts/MigrarSubidas.py --simular` y después sin `--simular`. Cada archivo se borra de `uploaded_files/` solo después de verificar su objeto en el bucket.

Antes de crear/modificar código Reflex o iniciar/depurar procesos, aplicar las skills del repositorio `reflex-docs`, `setup-python-env` y `reflex-process-management` según [AGENTS.md](../../AGENTS.md).

## Base de datos

La infraestructura local son cinco objetivos. El detalle de cada `ACCION` sale en `make help` y en [`scripts/BaseLocal.py`](../../scripts/BaseLocal.py).

| Objetivo | Efecto |
|---|---|
| `make db-up` | Valida Compose, arranca PostgreSQL, MinIO y Redis y crea el bucket. No migra |
| `make db-down` | Retira los contenedores y conserva los volúmenes. `ACCION=parar` solo los detiene. `ACCION=destruir CONFIRM=ELIMINAR` borra los volúmenes; los archivos de `apps/db/backups/` se quedan |
| `make db-estado` | `pg_isready`, `mc ready` y `redis-cli ping`. `ACCION=logs` muestra las últimas 200 líneas. `ACCION=consola` abre `psql` como `ortesislab_migrator` |
| `make db-respaldo FILE=x.dump` | `pg_dump` del esquema `ortesislab` y copia del bucket en `apps/db/backups/objetos`. No sobrescribe un `.dump` ya existente. El nombre admite letras, números, punto, guion y guion bajo |
| `make db-respaldo ACCION=restaurar FILE=x.dump CONFIRM=RESTAURAR` | Restaura ese volcado en `ortesislab_dev` y después los objetos. Exige que existan el `.dump` y `apps/db/backups/objetos`. `mc mirror` sobrescribe las claves presentes en la copia y no borra el resto del bucket |
| `make db-reset CONFIRM=ELIMINAR` | Borra y vuelve a crear `ortesislab_dev` vacía, con el esquema y los permisos de `preparar_base.sql`. Solo esa base. Las tablas llegan cuando exista una revisión y se ejecute `make migrar` |

El primer `make db-up` sobre un volumen nuevo ejecuta `apps/db/init/01_roles.sh`: roles y esquema `ortesislab` vacío, sin tablas. No hay fixture ni base de pruebas: los datos salen del uso de la aplicación. `make up` es `db-up` seguido de `make migrar` (`alembic upgrade head`).

Las tablas las genera y aplica quien mantiene el esquema. `apps/db/alembic/versions/` no tiene revisiones, así que `make migrar` no crea tablas. Cambiar primero [`Modelos.py`](../../apps/web/web/persistence/Modelos.py) y generar la revisión contra una base cuyo esquema `ortesislab` ya existe:

```powershell
uv run alembic revision --autogenerate -m "descripcion"
uv run alembic upgrade head
```

`make migrar` aplica `upgrade head`. Alembic usa la URL de desarrollo. Revisar el autogenerado: la FK circular, el trigger de versiones y los `GRANT` se añaden a mano, como indica [DATABASE.md](DATABASE.md#lo-que-alembic-no-genera). Alembic no bloquea migraciones concurrentes: ejecutarlas desde un único operador.

## Comprobación funcional

1. Sin sesión, pulsar Previsualizar: mensaje `Inicie sesión para continuar.` y ninguna fila nueva.
2. Iniciar sesión: la cookie `ortesislab_sesion` es HttpOnly; la barra muestra el nombre.
3. Previsualizar: progreso `En cola…`, ficha con métricas y STL en el visor cargado desde su `object_url`.
4. Recargar la página: el último lote reaparece desde la base.
5. Lote de varias variantes: progreso `x de y` y comparación de hasta tres vistas.
6. Descargar: `Content-Disposition: attachment` y evento `export_downloaded`.
7. `/historial`: filtrar, comparar versiones (diferencias de parámetros) y restaurar (versión nueva con `parent_version_id`).
8. Cerrar sesión y entrar con otro usuario: no ve fichas, historial ni archivos del anterior.
9. `make db-respaldo FILE=x.dump` y `make db-respaldo ACCION=restaurar FILE=x.dump CONFIRM=RESTAURAR` sobre `ortesislab_dev`.

## Pruebas existentes y trazabilidad

Las pruebas de persistencia se omiten si no existen `ORTESISLAB_TEST_DATABASE_URL` y `ORTESISLAB_TEST_WORKER_DATABASE_URL` apuntando a una base preparada aparte. Este repositorio no trae esa base. Sin base, sin esquema o sin variables se omiten con un motivo explícito. Cada rol abre su propia `Session` de SQLAlchemy, que confirma al salir del `with`. Los errores de PostgreSQL se comprueban en `DBAPIError.orig`. Levantan un `ThreadedMotoServer` (API S3 por HTTP en lugar de MinIO) y usan Redis local en la base 15 si responde; si no, prueban sin caché.

```powershell
make test
make lint
```

El detalle de cada carpeta está en [tests/README.md](../../tests/README.md).

| Archivo de prueba | Evidencia que aporta |
|---|---|
| `tests/aplicacion_web/test_generador_web.py` | Combinaciones y límites, semilla, STL, lectura STL/NPZ que conserva las coordenadas, archivo `tests/assets/OrtesisTest1model.stl`, expansión e índices inválidos |
| `tests/persistencia/test_almacen_import.py` | 6 casos: import con `object_url` y hash, deduplicación, rechazo, aislamiento entre usuarios, plantilla por usuario y migración de `uploaded_files` |
| `tests/persistencia/test_lotes_trabajador.py` | 8 casos: idempotencia, cuota, lote parcial con STL en el bucket, lease vencido, cancelación, generación sin Redis, restauración y conciliación |
| `tests/persistencia/test_propiedad_datos.py` | 8 casos: acceso entre usuarios, FK compuestas, URL obligatoria en `ready`, revisión de preferencias, permisos de roles app/trabajador y validez de sesiones |
| `tests/geometria/test_escala_malla.py` | 12 casos: factores decimales, desactivación, selección por paso y conservación de tamaño ante presupuesto |
| `tests/nucleo/test_nucleo.py` | 14 casos: equivalencia algorítmica con referencia, catálogo, validación, importación sin Blender, volumen/material |
| `tests/geometria/test_refinador_malla.py` | 3 casos: subdivisión, rejilla recortada y escala/paso |
| `tests/geometria/test_suavizado_borde.py` | 4 casos: dientes, tramo recto, borde corto e integración del marco |
| `tests/geometria/test_superficie_abierta.py` | 5 casos: cierre local del espesor, inversión, rechazo de capas/duplicados/sueltos/orientación |

Línea base con SQLAlchemy: **73 pruebas, 50 aprobadas y 23 omitidas, el 2026-10-13** con `.venv\Scripts\python.exe -B -m unittest discover -s tests`. Se omitieron todas las de `tests/persistencia/` porque no existían `ortesislab_dev` ni `ortesislab_test` ni migraciones. La persistencia SQLAlchemy no se ha probado contra PostgreSQL. Sí se compilaron con el dialecto PostgreSQL las sentencias de los 59 métodos de repositorio. La comprobación funcional 1–9 y las 73 pruebas sin omisiones se ejecutaron antes, con la implementación Psycopg/dbmate: no validan la versión actual. Ver [registro](../Agents/REGISTRO_CAMBIOS.md).

## Diagnóstico

| Síntoma | Revisar |
|---|---|
| `Inicie sesión para continuar.` con sesión iniciada | Cookie ausente o vencida (12 h), o sesión revocada |
| `/auth/login` muestra la página 404 de la app | El enlace debe navegar con recarga completa hasta el puerto del backend |
| `RuntimeError: Falta la variable de entorno …` al arrancar o en la primera subida | Definir esa variable en el entorno o en `.env` |
| `RuntimeError: … debe empezar por postgresql+psycopg://` | Cambiar el esquema de esa URL de `postgresql://` a `postgresql+psycopg://` |
| Lote queda `En cola…` | El trabajador no está corriendo o no alcanza la base; revisar su log |
| Base no disponible | Motor SQLAlchemy no abierto al arrancar (log `web`); `make db-estado` |
| `relation "..." does not exist` | Base sin migrar: `make migrar` |
| Visor: `El STL ya no está en el almacén` | Objeto borrado o fila `missing`; volver a generar |
| Visor: `No se pudo contactar con el almacén` | MinIO caído, `ORTESISLAB_S3_PUBLIC_URL` incorrecta o política de lectura de STL no aplicada |
| Superficie rechazada | Debe ser abierta, orientada y conectada; un STL de una ortesis con espesor no sirve como base |
| Generación lenta tras reinicio de Redis | Caché vacía; se reconstruye por contenido |
| Demora o mucha memoria | Paso, ancho de nervadura, número de caras, tamaño de celda y número de variantes |
| `EntornoBlenderRequerido` al importar web | Importación accidental de adaptadores Blender |

Logs: `ortesislab.<subsistema>`, consola INFO y archivo DEBUG `OrtesisLabPlugin/logs/ortesislab.log`, según `config/registro.json`.

## Despliegue y recuperación

El repositorio incluye Compose para desarrollo local con puertos ligados a 127.0.0.1. No hay infraestructura cloud, CI ni TLS configurados. Para varias instancias Reflex se necesita el mismo PostgreSQL, bucket y Redis; los lotes se recuperan desde la base tras reiniciar cualquier proceso y los leases vencidos vuelven a la cola. `make db-respaldo` copia metadatos y objetos en un solo paso; la restauración devuelve los dos y solo está permitida sobre `ortesislab_dev`. Alembic no bloquea migraciones concurrentes: ejecutarlas desde un único operador.
