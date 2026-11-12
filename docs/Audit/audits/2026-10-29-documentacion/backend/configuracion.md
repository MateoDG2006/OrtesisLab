# Backend · Configuración

**Estado:** propuesta, `implemented` en `e56df68`.
**Archivos:** `web/Ajustes.py`, `web/ConfiguracionBackend.py`, `config/*.yaml`,
`.env.example`, `rxconfig.py`, `GenerateModelsApp/config/*.json`.

Hay tres fuentes de configuración, con responsabilidades separadas:

| Fuente | Contiene | Lector | Cuándo se lee |
|---|---|---|---|
| Variables `ORTESISLAB_*` (entorno real > `.env` raíz) | Secretos, URL, credenciales | `Ajustes` | Al **acceder** al atributo; `Ajustes.Cargar()` se cachea una vez por proceso (`lru_cache`) |
| `config/<area>.yaml` | Límites, tiempos y tamaños del backend | `ConfiguracionBackend.Cargar(area)` | Al **importar** el módulo consumidor; caché por proceso, por lo que cambiarlo exige reiniciar |
| `GenerateModelsApp/config/*.json` | Defaults geométricos y límites del núcleo, compartidos con Blender | `Utilidades.Configuracion` | Bajo demanda, con caché y `Recargar()` |

## `web/Ajustes.py`

### `Variable(clave, defecto=None, prefijo="")` (descriptor)

- **E:** clave de entorno; `defecto=None` la hace obligatoria; `prefijo` exigido.
- **P:** `ajustes.valores.get(clave) or defecto`. Una cadena vacía cuenta como
  ausente.
- **S:** `str`.
- **Err:** `VariableFaltante(clave)` si no hay valor ni defecto;
  `VariableInvalida(clave, prefijo)` si no empieza por el prefijo.
- **Ef:** ninguno; no modifica `os.environ`.

### `Ajustes.Cargar() -> Ajustes`

Combina `_LeerArchivo(RAIZ/.env)` con `os.environ` (gana el entorno). El
parser de `.env`:

- una línea `CLAVE=valor` por entrada;
- ignora vacías y las que empiezan por `#`;
- quita espacios y **una** capa de comillas simples o dobles;
- **no** admite comentarios al final de la línea, `export` ni continuaciones.

Se cachea: un cambio en el entorno después de la primera llamada no se ve.

### `Ajustes.Faltante(*atributos) -> str`

Devuelve el mensaje de la primera variable sin definir o `""`. Lo usan las
pruebas para decidir si se omiten.

### Catálogo de variables

| Atributo | Variable | Defecto | Prefijo | Consumidores (lectura) |
|---|---|---|---|---|
| `database_url` | `ORTESISLAB_DATABASE_URL` | obligatoria | `postgresql+psycopg://` | `web/GenerateModelsApp.py:28` (arranque), `scripts/MigrarSubidas.py` |
| `worker_database_url` | `ORTESISLAB_WORKER_DATABASE_URL` | obligatoria | ídem | `scripts/EjecutarTrabajador.py:585` |
| `migrator_database_url` | `ORTESISLAB_MIGRATOR_DATABASE_URL` | obligatoria | ídem | `db/alembic/env.py:25` |
| `test_database_url`, `test_worker_database_url` | `ORTESISLAB_TEST_*` | obligatorias | ídem | `tests/persistencia/apoyo_persistencia.py` |
| `test_migrator_database_url` | `ORTESISLAB_TEST_MIGRATOR_DATABASE_URL` | obligatoria | ídem | Alembic con `-x base=test` |
| `s3_endpoint`, `s3_access_key`, `s3_secret_key` | `ORTESISLAB_S3_*` | obligatorias | — | `StorageS3.DesdeAjustes` (primer `Almacen.Actual()`) |
| `s3_public_url` | `ORTESISLAB_S3_PUBLIC_URL` | `""` (usa el endpoint) | — | Base de `object_url` |
| `s3_bucket` / `s3_region` | — | `ortesislab` / `us-east-1` | — | `StorageS3` |
| `redis_url` | `ORTESISLAB_REDIS_URL` | `""` (sin caché) | — | `CacheRedis._Cliente` |
| `oidc_issuer`, `oidc_client_id`, `oidc_client_secret`, `oidc_redirect_uri` | `ORTESISLAB_OIDC_*` | obligatorias | — | `AutenticacionOidc.Aplicacion` al construir `rx.App` |
| `session_secret` | `ORTESISLAB_SESSION_SECRET` | obligatoria | — | `SessionMiddleware` (cookie `ortesislab_oidc`) |
| `app_url` | `ORTESISLAB_APP_URL` | `http://localhost:3000` | — | Redirección tras login y logout |
| `cookie_secure` (propiedad) | `ORTESISLAB_COOKIE_SECURE` | `false` | — | `"true"` sin distinguir mayúsculas activa `Secure` |

**Momento de fallo:**

- La web falla al importar `web.GenerateModelsApp` si faltan OIDC o la sesión.
- Si falta `database_url`, el arranque registra el error, pero los handlers
  devuelven `PersistenciaNoDisponible`.
- Las variables S3 fallan en la primera operación con el bucket.
- El trabajador exige S3 y su URL de base al arrancar.

## `web/ConfiguracionBackend.py`

### `ConfiguracionBackend.Cargar(area: str) -> dict`

- **E:** nombre de área.
- **P:** abre `config/<area>.yaml` y aplica `yaml.safe_load`.
- **S:** `dict` sin validar.
- **Err:** `FileNotFoundError` y `yaml.YAMLError`; un `KeyError` aparece después,
  en el consumidor.
- **Ef:** caché por proceso.

No valida tipos, rangos ni relaciones (hallazgo B-09).

### Claves YAML: valor, unidad, consumidor y efecto

| Archivo · clave | Valor | Unidad | Consumidor | Efecto |
|---|---|---|---|---|
| `persistencia.conexion.reintentos` | 3 | intentos | `ConexionPostgres.Ejecutar` | Repite la transacción ante `SerializationFailure` o `DeadlockDetected` |
| `persistencia.conexion.pausa_reintento_s` | 0.05 | s | ídem | Pausa `0.05 × n` antes del reintento n |
| `persistencia.conexion.espera_adquisicion_s` | 5.0 | s | `create_engine(pool_timeout)` | Espera por conexión libre; al agotarse lanza `PersistenciaNoDisponible` |
| `persistencia.conexion.timeout_conexion_s` | 10 | s | `connect_args.connect_timeout` | Apertura de conexión con PostgreSQL |
| `persistencia.lotes.maximo_items` | 12 | ítems | `Contratos.MAXIMO_ITEMS_LOTE` → `ServicioLotes.Solicitar` | Rechaza el lote con `CuotaExcedida`. **También** hay un `CHECK 1..12` fijo en el esquema (B-08) |
| `persistencia.lotes.maximo_pendientes` | 3 | lotes | `Contratos.MAXIMO_LOTES_PENDIENTES` | Cuota de lotes `queued`/`running` |
| `persistencia.lotes.maximo_intentos` | 3 | intentos | `batch_items.max_attempts` al insertar | Reintentos por ítem |
| `persistencia.lotes.espera_reintento_s` | 5.0 | s | `ServicioLotes.Fallar` | `available_at = now + 5 × 2^(n-1)` |
| `persistencia.historial.limite_defecto` / `limite_maximo` | 25 / 100 | filas | `ServicioHistorial.Listar` | Tamaño de página, acotado a `[1, 100]` |
| `persistencia.historial.maximo_comparacion` | 3 | versiones | `ServicioHistorial.Comparar`, `EstadoHistorial.Seleccionar` | Rechaza la cuarta |
| `trabajador.lease_s` | 120 | s | `ReservarPendiente`, `RenovarLease` | Vigencia de la reserva |
| `trabajador.latido_s` | 30 | s | Hilo de latido | Debe ser `< lease_s`; no se comprueba |
| `trabajador.supervision_s` | 30 | s | `TrabajadorGeneracion.Ejecutar` | Periodo de `AbandonarVencidos` |
| `trabajador.conciliacion_s` | 600 | s | ídem | Periodo de `ConciliadorArchivos.Ejecutar` |
| `trabajador.conciliador.horas_staged` | 24 | h | `StagedVencidos`, borrado de huérfanos | Antigüedad para borrar |
| `trabajador.conciliador.dias_rechazo` | 30 | días | `RechazadosVencidos` | Retención de imports rechazados |
| `trabajador.conciliador.lote_comprobacion` | 200 | assets | `ListosParaComprobar` | `HEAD` por pasada |
| `cache.ttl_s` | 604800 | s (7 días) | `CacheRedis` | Expiración de cada clave |
| `cache.reintento_s` | 30.0 | s | `CacheRedis._Fallo` | Caché apagada tras un fallo |
| `cache.timeout_s` | 0.5 | s | Cliente Redis | Timeout de socket y de conexión |
| `almacen.timeout_conexion_s` / `timeout_lectura_s` | 3 / 30 | s | boto3 `Config` | Timeouts S3 |
| `almacen.intentos` | 3 | intentos | boto3 `retries` (`standard`) | Reintentos por operación |
| `sesion.duracion_horas` | 12 | h | `ContextoUsuario.DURACION_SESION` | `expires_at` y `max_age` de la cookie |
| `sesion.intercambio_oidc_s` | 600 | s | `SessionMiddleware.max_age` | Vida de `state` y `nonce` |
| `web.intervalo_progreso_s` | 1.0 | s | `EstadoApp._Seguir` | Periodo de sondeo (B-10) |
| `web.maximo_variantes` | 12 | variantes | `GeneradorWeb.Combinaciones` | Rechaza antes de crear el lote |
| `web.espera_crear_s` | 600.0 | s | `GeneradorWeb.Crear` | Bloqueo máximo del hilo |
| `web.maximo_bytes` | 52428800 | bytes (50 MiB) | `LectorSuperficie`, `ServicioImports`, `EstadoApp.CargarSuperficie` | Tamaño máximo de subida; la UI dice «MB» |
| `web.maximo_descomprimido_bytes` | 134217728 | bytes (128 MiB) | `LectorSuperficie._Npz` | Suma de `file_size` **declarados** en el ZIP (A-01) |
| `web.patrones` | 5 claves | — | `GeneradorWeb.PATRONES`, selectores | Orden y etiquetas |
| `web.ejes` | 11 claves | — | `GeneradorWeb.EJES` | Ejes de barrido |
| `web.estados_visibles` | 5 claves | — | `EstadoHistorial` | Etiqueta por `EstadoItem` |

### Constantes que no son configuración

| Constante | Valor | Archivo |
|---|---|---|
| `NOMBRE_COOKIE` | `ortesislab_sesion` | `web/services/ContextoUsuario.py:24` |
| Cookie OIDC | `ortesislab_oidc` | `web/services/AutenticacionOidc.py:92` |
| `PREFIJO` Redis | `ortesislab:superficie:` | `web/cache/CacheRedis.py:22` |
| `PREFIJO_SUPERFICIE` | `superficie-` | `web/services/ServicioImports.py:37` |
| `VERSION` del generador | `GeneradorGeometrico-1` | `web/services/GeneradorGeometrico.py:23` |
| `NOMBRE_PROYECTO_PREDETERMINADO` | `Proyecto principal` | `RepositorioProyectos.py:13` |
| `ESQUEMA_*`, `VERSION_LECTOR`, `VERSION_EXPORTADOR` | **No definidas** (B-01); antes `1`, `1`, `LectorSuperficie-1`, `GeneradorWeb.Stl-1` | `web/persistence/Contratos.py` |

## `rxconfig.py`

`app_name="GenerateModelsApp"`, `app_module_import="web.GenerateModelsApp"`,
plugins `SitemapPlugin`, `TailwindV4Plugin` y `RadixThemesPlugin` (indigo,
slate, radio `medium`). No fija `api_url`, `cors_allowed_origins` ni
`db_url`; Reflex usa sus valores por defecto: backend en `:8000` y frontend
en `:3000` en desarrollo.

## Cambiar la configuración con seguridad

1. Añadir la variable a `Ajustes` y a `.env.example`, o la clave al YAML.
2. Comprobar las relaciones: `maximo_variantes ≤ maximo_items ≤ 12` (el último
   valor exige migración del `CHECK`) y `latido_s < lease_s`.
3. Reiniciar web y trabajador; ningún valor se recarga en caliente.
4. Actualizar este catálogo y `OPERACION_Y_PRUEBAS.md`.
