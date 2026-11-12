# Backend · Persistencia

**Estado:** propuesta. `implemented` y **no validado contra PostgreSQL**: no hay
revisiones Alembic (B-02). **Archivos:** `web/persistence/**`, `web/enums/**`.

## Reglas transversales

- Los repositorios **reciben una `Session` abierta, nunca hacen commit** y
  devuelven DTO (`dataclass(frozen=True)`) o `dict`. No exponen modelos ORM.
- Toda consulta de un recurso filtra por `user_id`. Solo las operaciones de la
  cola y la conciliación recorren varios usuarios.
- Un recurso ajeno o inexistente produce el mismo `AccesoDenegado`.
- Las sentencias usan las tablas `Table` (`Modelo.__table__`), con alias en
  `repositorios/Consultas.py`.
- Las transacciones las abren los servicios con `ConexionPostgres.Ejecutar(fn)`,
  y nunca abarcan geometría ni transferencias S3.

## `ConexionPostgres.py`

| Método | E → S | Comportamiento | Errores |
|---|---|---|---|
| `Abrir(dsn, minimo=1, maximo=4, nombre)` | DSN → `None` | Si ya hay motor, no hace nada. `create_engine(pool_size=maximo, max_overflow=0, pool_timeout=5, pool_pre_ping=True, connect_timeout=10, application_name=ortesislab-<nombre>)`. Abre y cierra `max(1, minimo)` conexiones para fallar al arrancar | `PersistenciaNoDisponible` si `DBAPIError` |
| `Cerrar()` | — | `dispose()` del motor; deja la clase sin motor | — |
| `Abierta()` | → `bool` | ¿Hay motor? | — |
| `Transaccion()` (context manager) | → `Session` | `sessionmaker(expire_on_commit=False).begin()`: commit al salir y rollback ante excepción | Sin motor: `PersistenciaNoDisponible`. `exc.TimeoutError` → `PersistenciaNoDisponible`. `OperationalError` no reintentable → `PersistenciaNoDisponible`; reintentable → se relanza |
| `Ejecutar(fn)` | `fn(Session) -> T` → `T` | Hasta 3 intentos si `error.orig` es `SerializationFailure` o `DeadlockDetected`, con pausa `0.05 × n` | El último error se relanza |

Pools: web 1–4 conexiones (`"backend"`), trabajador 1–2 (`"trabajador"`), uno
por proceso. El hilo de latido del trabajador comparte el pool de 2.

## `Contratos.py`: DTO y errores

### Errores (todos heredan de `ErrorPersistencia`, con mensaje visible)

| Clase | Mensaje por defecto | Lo lanza |
|---|---|---|
| `PersistenciaNoDisponible` | (variable) | `ConexionPostgres` |
| `SesionInvalida` | «Inicie sesión para guardar y consultar su trabajo.» | `ContextoUsuario` |
| `AccesoDenegado` | «El recurso no existe o no le pertenece.» | `_DelUsuario` y servicios |
| `SolicitudIdempotenteEnConflicto` | «Esa solicitud ya se registró con otros parámetros.» | `ServicioLotes.Solicitar` |
| `ConflictoRevision` | «Las preferencias cambiaron en otra pestaña…» | `RepositorioPreferencias.Guardar` |
| `CuotaExcedida` | (variable) | `ServicioLotes.Solicitar` |
| `AlmacenamientoNoDisponible`, `ObjetoAusente` | Ver [integraciones](integraciones.md) | Almacén |

### DTO campo a campo

| DTO | Campos (tipo) | Origen |
|---|---|---|
| `UsuarioAutenticado` | `user_id` UUID, `display_name` str, `email` str?, `project_id` UUID | `ContextoUsuario.Requerir` |
| `Asset` | `id`, `user_id`, `storage_key`, `object_url?`, `kind`, `original_name?`, `media_type`, `size_bytes`, `sha256`, `status` | `file_assets` |
| `ImportDTO` | `id`, `project_id`, `original_asset_id`, `normalized_asset_id?`, `source_kind`, `status`, `format`, `vertex_count?`, `face_count?`, `raw_dimensions_mm?` list[float], `error_code?`, `error_message?`, `created_at` | `imports` |
| `VersionDTO` | `id`, `project_id`, `import_id`, `parent_version_id?`, `version_number`, `label?`, `change_note?`, `parameters` dict, `auto_scale`, `material_snapshot` dict, `parameters_sha256`, `created_at` | `model_versions` |
| `SolicitudLote` | `import_id`, `request_id`, `mode` (`single`/`sweep`/`retry`), `definition` dict, `variantes` list[dict], `auto_scale`, `parent_version_id?`, `change_note?`, `version_ids?` | Construido por `EstadoApp`, `GeneradorWeb.Crear` y `ServicioHistorial` |
| `LoteDTO` | `id`, `project_id`, `request_id`, `mode`, `status`, `total_items`, `cancel_requested_at?`, `created_at`, `finished_at?` | `generation_batches` |
| `ResultadoDTO` | `id`, `attempt_id`, `volume_mm3` float, `weight_g` float, `estimated_price` Decimal, `currency?`, `vertices`, `triangles`, `dimensions_mm`, `validation_status`, `warnings`, `effective_scale?`, `stl_asset_id?`, `stl_url?`, `stl_status?` | `ColumnasResultado` |
| `ItemLote` | `id`, `batch_id`, `position`, `status`, `version_id`, `version_number`, `parameters`, `attempt_count`, `error_message?` (del último intento), `resultado?` | `RepositorioLotes.Items` |
| `ProgresoLote` | `lote`, `items`; propiedades `terminados` (ítems en `ITEMS_TERMINALES`) y `abierto` (lote en `LOTES_ABIERTOS`) | Servicios |
| `TrabajoReservado` | `item_id`, `attempt_id`, `attempt_number`, `lease_token`, `user_id`, `project_id`, `batch_id`, `version_id`, `parameters`, `auto_scale`, `normalized_asset_id`, `max_attempts`, `material_snapshot` | `ReservarPendiente` |
| `ResultadoGeometrico` | métricas, `price_per_gram` y `density_g_cm3` Decimal, `currency?`, `vertices`, `triangles`, `dimensions_mm`, `effective_scale`, `effective_step_mm?`, `warnings`, `configuracion`, `execution_parameters` | `GeneradorGeometrico.Construir` |
| `FilaHistorial` | ítem, lote, versión, proyecto, patrón, parámetros, fecha, estado, métricas opcionales, `validation_status?`, `stl_url?`, `stl_status?`, `error_message?` | `RepositorioHistorial.Listar` |
| `PaginaHistorial` | `filas`, `cursor_siguiente?` | `ServicioHistorial.Listar` |
| `IntentoDTO` | `id`, `attempt_number`, `status`, `worker_id`, `generator_version`, `code_revision`, `effective_scale?`, `effective_step_mm?`, `error_code?`, `error_message?`, `started_at`, `finished_at?`, `duration_ms?` | `RepositorioResultados.Intentos` |
| `DetalleVersion` | `version`, `importacion`, `parametros_padre?`, `intentos`, `resultados`, `eventos` | `ServicioHistorial.Detalle` |
| `Preferencias` | `user_id`, `auto_scale`, `locale`, `display_currency?`, `default_parameters`, `revision` | `user_preferences` |

Constantes exportadas: `MAXIMO_ITEMS_LOTE`, `MAXIMO_LOTES_PENDIENTES` y
`MAXIMO_INTENTOS`, desde `persistencia.yaml`. **Faltan** las cuatro constantes
de versión (B-01).

## Enums (`web/enums/`)

Son `StrEnum` que deben coincidir con los `CHECK`; añadir un valor exige una
migración.

| Enum | Valores |
|---|---|
| `EstadoUsuario` | `active`, `disabled`, `deletion_pending` (sin flujo, B-13) |
| `TipoAsset` | `import_original`, `surface_npz`, `result_stl`, `export_json` |
| `EstadoAsset` | `staged`, `ready`, `quarantined` (sin productor), `missing`, `deleting` (sin productor), `deleted` |
| `ExtensionSuperficie` | `.stl`, `.npz` |
| `OrigenImport` | `upload`, `included_template` |
| `EstadoImport` | `received`, `validating` (sin productor), `ready`, `rejected` |
| `FormatoImport` | `stl_binary`, `stl_ascii`, `npz` |
| `BackendGeneracion` | `python_core` |
| `ModoLote` | `single`, `sweep`, `retry` |
| `EstadoLote` | `queued`, `running`, `succeeded`, `partial`, `failed`, `cancelled` |
| `EstadoItem` | `queued`, `running`, `succeeded`, `failed`, `cancelled` |
| `EstadoIntento` | `running`, `succeeded`, `failed`, `abandoned`, `cancelled` |
| `EstadoValidacion` | `not_checked`, `passed`, `failed` (la web solo produce `not_checked`) |
| `AlcanceGeometria` | `pre_voxel_shell` |
| `FormatoExport` | `stl_binary`, `parameters_json` |
| `UnidadExport` | `mm` |
| `EstadoExport` | `ready`, `missing`, `deleted` |
| `TipoEvento` | 13 tipos; ver [servicios y flujos](servicios-y-flujos.md#eventos-de-historial) |

Tuplas: `ITEMS_TERMINALES = (succeeded, failed, cancelled)` y
`LOTES_ABIERTOS = (queued, running)`.

## Esquema (`Modelos.py`)

Hay 13 tablas, sin `schema` declarado (`search_path = ortesislab` por rol). La
convención de nombres reproduce los del esquema original. Los `CHECK ... IN`
salen de los enums (`_Valores`). El detalle de columnas e índices está en
`docs/AppBackend/DATABASE.md` §4–5; aquí solo se listan los invariantes que usa
el código:

| Tabla | Invariantes que el código asume |
|---|---|
| `app_users` | Única `(auth_issuer, auth_subject)`; `status` = `active` para iniciar sesión |
| `auth_sessions` | Se guarda el SHA-256 del token, nunca el token; `revoked_at`, `expires_at` |
| `user_preferences` | Una fila por usuario; `revision` para control optimista |
| `file_assets` | Única `(user_id, id)` para FK compuestas; `object_url` obligatoria en `ready` (según `test_propiedad_datos`) |
| `projects` | `next_version_number` reservado con `UPDATE … RETURNING` |
| `imports` | FK compuestas a assets del mismo usuario; **sin** unicidad por SHA del original (B-07) |
| `model_versions` | Única `(project_id, version_number)`; trigger `model_versions_comprobar` (manual, B-02) |
| `generation_batches` | Única `(user_id, request_id)`; `CHECK total_items BETWEEN 1 AND 12` (B-08) |
| `batch_items` | `winning_attempt_id` con FK circular diferida (`use_alter`) |
| `generation_attempts` | `lease_token`, `heartbeat_at`, `retryable`, `duration_ms` |
| `generation_results`, `exports`, `history_events` | Propiedad por `user_id`; los eventos referencian versión, lote, intento y export |

## Repositorios: ficha por método

### `RepositorioBase`

| Método | Contrato |
|---|---|
| `_Uno(c, q)` / `_Todos(c, q)` | Primera fila o todas como `dict` |
| `_Construir(dto, fila)` | Crea el DTO con los campos del dataclass; ignora columnas sobrantes; `KeyError` si falta una |
| `_Dto`, `_Opcional`, `_Lista` | Conversión con `cls.DTO` |
| `_DelUsuario(c, user_id, *cond, bloquear=False)` | `SELECT … WHERE user_id = :u AND cond [FOR UPDATE]`; `AccesoDenegado` si no hay fila |

### `RepositorioUsuarios`

| Método | E → S | SQL / efectos |
|---|---|---|
| `Upsert(c, issuer, subject, email, nombre)` | → `user_id` | `INSERT … ON CONFLICT (issuer, subject) DO UPDATE email, display_name, updated_at`; `display_name = nombre[:120] or subject[:120]` |
| `Estado(c, user_id)` | → `str?` | `status` |
| `CrearSesion(c, user_id, token_sha256, expira)` | — | `INSERT auth_sessions` |
| `ResolverSesion(c, token_sha256)` | → `{id, display_name, email}?` | Sesión no revocada, no vencida (`expires_at > now()`) y usuario `active` |
| `RevocarSesion(c, token_sha256)` | — | `revoked_at = now()` si no estaba revocada |

### `RepositorioPreferencias`

| Método | Contrato |
|---|---|
| `Obtener(c, user_id)` | `INSERT … ON CONFLICT DO NOTHING` y después `SELECT`: siempre hay fila (efecto: escribe en una lectura) |
| `Guardar(c, user_id, auto_scale, parametros, revision_esperada)` | `UPDATE … WHERE revision = :esperada SET revision+1 RETURNING *`; `ConflictoRevision` si 0 filas |

### `RepositorioProyectos`

| Método | Contrato |
|---|---|
| `Predeterminado(c, user_id)` | El proyecto no archivado más antiguo llamado «Proyecto principal»; si no existe, lo crea. **Se llama en cada `Requerir`** |
| `Crear(c, user_id, nombre, descripcion?)` | `INSERT`, devuelve el id |
| `PorNombre(c, user_id, nombre)` / `Listar(c, user_id)` | Lecturas; `Listar` excluye archivados, ordenado por `updated_at` descendente. Sin consumidor en la UI |

### `RepositorioAssets`

| Método | Contrato |
|---|---|
| `CrearStaged(c, user_id, asset_id, clave, kind, nombre?, media, tamaño, sha)` | `INSERT status=staged` |
| `MarcarListo(c, user_id, asset_id, url)` | `staged → ready` con `object_url` y `ready_at`; `AccesoDenegado` si no estaba `staged` |
| `MarcarEstado(c, asset_id, estado)` | Sin filtro de usuario (solo conciliación); `deleted_at` si `deleted` |
| `Obtener`, `PorClave` | `_DelUsuario` por id o `storage_key` |
| `ListoPorSha(c, user_id, sha, kind)` | El `ready` más antiguo con ese SHA y tipo (sin consumidor actual) |
| `StagedVencidos(c, horas)` | `staged` con `created_at < now - horas`, máximo 200 |
| `RechazadosVencidos(c, dias)` | Assets (original o normalizado) de imports `rejected` con `finished_at` antiguo, máximo 200 |
| `ListosParaComprobar(c, desde_id?, limite)` | `ready` ordenados por id, con cursor |
| `ClavesRegistradas(c, claves)` | Claves presentes en cualquier estado |
| `MarcarExportsFaltantes(c, asset_id)` | Exports `ready → missing` |

### `RepositorioImports`

| Método | Contrato |
|---|---|
| `Crear(c, user, import_id, original_id, source_kind, formato, reader_version, esquema)` | `INSERT status=received` en el proyecto del usuario |
| `MarcarListo(c, user_id, import_id, normal_id, vertices, caras, dimensiones)` | `ready`, `finished_at` |
| `MarcarRechazado(c, user_id, import_id, codigo, mensaje)` | `rejected`, `error_code[:80]`, `error_message[:500]` |
| `Obtener` | `_DelUsuario` |
| `ListoPorNormalizado(c, user_id, asset_id)` | Import `ready` más reciente con ese NPZ |
| `ListoPorOriginal(c, user_id, project_id, sha, source_kind)` | Import `ready` cuyo original tiene ese SHA y cuyo NPZ está `ready` (deduplicación) |
| `NombreOriginal(c, user_id, import_id)` | `original_name` o `""` |

### `RepositorioVersiones`

| Método | Contrato |
|---|---|
| `ReservarNumeros(c, user_id, project_id, n)` | `UPDATE projects SET next_version_number += n RETURNING next - n`. Bloquea la fila del proyecto hasta el commit. `AccesoDenegado` si el proyecto está archivado o es ajeno |
| `Insertar(c, …, parametros, esquema, auto_scale, material, sha, padre?, nota?)` | `INSERT` con `requested_backend = python_core` |
| `Obtener` | `_DelUsuario` |

### `RepositorioLotes` (admisión, cola y lease)

| Método | Contrato |
|---|---|
| `BloquearUsuario(c, user_id)` | `pg_advisory_xact_lock(hashtextextended(user_id, 0))` |
| `IntentarBloquearUsuario(c, user_id)` | `pg_try_advisory_xact_lock(...)` → `bool` |
| `PorRequest(c, user_id, request_id)` | Lote previo (idempotencia) |
| `ContarPendientes(c, user_id)` | Lotes en `queued`/`running` |
| `InsertarLote`, `InsertarItem` | `INSERT`; el ítem lleva `max_attempts` |
| `Obtener(c, user_id, batch_id, bloquear)`, `Ultimo(c, user_id)` | Lecturas |
| `Items(c, user_id, batch_id)` | Ítems con versión, último error, resultado ganador, export STL y asset; ordenados por `position` |
| `SolicitarCancelacion(c, user_id, batch_id)` | Si el lote está abierto y sin cancelación: `cancel_requested_at = now()` y ítems `queued → cancelled`. Devuelve `bool` |
| `Recalcular(c, user_id, batch_id)` | Bloquea el lote (`FOR UPDATE`). Con ítems `queued`/`running` → `queued` o `running`. Si no, `cancelled` (si se pidió), `succeeded` (todos), `partial` (alguno) o `failed`; emite `batch_finished` una vez |
| `_Candidato()` | Ítem `queued` con `available_at <= now`, lote sin cancelación, usuario `active` y **sin otro ítem `running` del mismo usuario**; orden `available_at, created_at, id`; `FOR UPDATE OF items SKIP LOCKED LIMIT 1` |
| `ReservarPendiente(c, trabajador_id, lease_s, generador, revision, runtime)` | Candidato → `try_advisory_lock` del usuario (si falla, `None`) → comprueba otra vez que no haya `running` → ítem `running`, `attempt_count+1`, `lease_token`, `lease_expires_at` → `INSERT` del intento → lote `queued → running` → evento `attempt_started` → `TrabajoReservado` |
| `RenovarLease(c, trabajo, lease_s)` | `UPDATE` con `lease_token` vigente; `heartbeat_at` del intento; `False` si se perdió |
| `BloquearVigente(c, trabajo)` | `SELECT … FOR UPDATE` del ítem con su token |
| `CancelacionPedida(c, trabajo)` | `bool` |
| `CerrarIntento(c, trabajo, estado, ms, codigo?, mensaje?, reintentable)` | Intento `running →` estado |
| `Exito(c, trabajo, resultado, ms)` | Intento `succeeded` con escala, paso y parámetros de ejecución; ítem `succeeded`, `winning_attempt_id`, lease a `NULL` |
| `Liberar(c, user_id, item_id, reintentar, espera_s)` | `cancelled` (si se pidió cancelación), `queued` con `available_at = now + espera` (si quedan intentos) o `failed` |
| `AbandonarIntento(c, user_id, item_id)` | Intento `running → abandoned` con `error_code = lease_expired` |
| `Vencidos(c)` | Hasta 50 ítems `running` con lease vencido, `FOR UPDATE SKIP LOCKED` |

### `RepositorioResultados`

| Método | Contrato |
|---|---|
| `Insertar(c, trabajo, resultado, alcance)` | `INSERT generation_results` → `result_id` |
| `InsertarExport(c, user_id, result_id, asset_id, formato, version)` | `INSERT exports units=mm` |
| `Dto(fila)` | Convierte `ColumnasResultado` a `ResultadoDTO` (float, Decimal) |
| `Intentos(c, user_id, version_id)` | Todos los intentos de la versión (en todos sus lotes) |
| `DeVersion(c, user_id, version_id)` | Resultados con su STL, del más reciente al más antiguo |
| `ExportStl(c, user_id, asset_id)` | Export STL, estado, ítem, versión, lote, clave y URL |

### `RepositorioHistorial`

| Método | Contrato |
|---|---|
| `Evento(c, user_id, project_id, tipo, *, version_id?, batch_id?, attempt_id?, export_id?, payload?)` | `INSERT history_events` |
| `Listar(c, user_id, filtros, cursor?, limite)` | Una fila por ítem; filtros `project_id`, `pattern` (`parameters->>'pattern'`), `status`, `desde`, `hasta` (exclusivo); cursor `(created_at, id) <`; pide `limite+1` para saber si hay más |
| `EventosDeVersion(c, user_id, version_id)` | `event_type`, `payload`, `created_at` ordenados |

### `Consultas.py`

Alias de tablas, `AHORA = func.now()`, `Segundos(v)` → `timedelta`.
`UltimoError()` es una subconsulta correlacionada con el mensaje del intento de
mayor número. `ConStlGanador(origen)` hace `LEFT JOIN` de resultado ganador,
export STL y asset. `ColumnasResultado(intento)` es la proyección común.
