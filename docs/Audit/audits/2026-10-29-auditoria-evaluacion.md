# AUD-2026-10-29-002 — Auditoría y evaluación del proyecto

**Fecha:** 2026-10-29, America/Bogota. **Estado:** ABIERTA, sin resoluciones.
**Modo:** auditoría, evaluación (viabilidad, funcionalidad, escalabilidad) y
documentación granular propuesta. Sin correcciones de producción.
**Revisión de partida:** `e56df680e315c4de799c7c947727da5981c32fe8`, rama `master`
(merge del PR #19). Árbol de trabajo limpio al iniciar.

## Resultado

Se registran **22 hallazgos**: **1 P0**, **5 P1**, **12 P2** y **4 P3**.

El hallazgo P0 es bloqueante. En `master`, `import web.GenerateModelsApp` falla con
`ImportError`. El commit `7ac5834` eliminó de `web/persistence/Contratos.py`
cuatro constantes que todavía usan tres servicios y un script. La web, el
trabajador y `scripts/MigrarSubidas.py` no arrancan, y 27 de las 73 pruebas
declaradas no llegan a cargarse. Llegó a `master` porque no hay integración
continua que ejecute pruebas (B-03).

| Eje | Conclusión | Puntuación (1–5) | Confianza |
|---|---|---|---|
| Viabilidad | El diseño se ajusta a los objetivos: núcleo compartido, cola durable y propiedad por usuario. Hoy no puede desplegarse desde el repositorio: no importa (B-01) ni crea su esquema (B-02) | 2 | Alta |
| Funcionalidad | Núcleo geométrico: 38 pruebas pasan. Aplicación web: no funciona en `master`. La persistencia nunca se ha ejecutado contra PostgreSQL con esta implementación | 2 | Alta |
| Escalabilidad | Evaluación de diseño, **sin carga medida**. Hay una cola correcta con `SKIP LOCKED` y leases, pero la normalización se hace en el proceso web, el progreso se lee por sondeo, el conciliador recorre todo el bucket y falta una cuota de almacenamiento | 3 | Media |

La auditoría `AUD-2026-10-13-001` sigue **ABIERTA**. Desde su revisión de partida
(`2b74669`) el núcleo `GenerateModelsApp/` no ha cambiado; sus hallazgos A-01 a
A-22 siguen aplicándose a ese código ([estado por hallazgo](#estado-observado-de-aud-2026-10-13-001)).

## Alcance, propósito y método

**Alcance:** todos los archivos versionados en `e56df68`, salvo `docs/Audit/**`
(los registros de auditoría tienen su propio ciclo) y `.agents/**` (skills de
terceros instaladas con `skills-lock.json`; no son código del proyecto). Son 181
archivos (100 Python), con huella SHA-256 en el [inventario](2026-10-29-inventario.json);
53 de ellos ya pertenecían a `AUD-2026-10-13-001` y 57 tienen hallazgos de esta
auditoría.

**Propósito:** evaluar si el proyecto puede cumplir lo que declara y qué lo
impide; dejar una documentación más granular que la canónica y una lista
verificable de lo que falta documentar.

**Método:**

1. Lectura completa del backend web (`web/**`, 51 archivos Python), salvo
   `web/persistence/Modelos.py`, `web/PaginaComparacion.py` y
   `web/PaginaHistorial.py`, que se revisaron por estructura: tablas,
   restricciones e índices en el primero; componentes y bindings en las páginas.
   También se leyeron `scripts/EjecutarTrabajador.py`, `scripts/EmpaquetarBlender.py`,
   `infra/`, `db/`, `config/`, el visor y el workflow de GitHub.
   Del núcleo `GenerateModelsApp/` se leyeron `Modeling.py`, `Materials.py` y la
   configuración JSON. Del resto del núcleo se extrajo el catálogo de clases y
   funciones con `ast` y se contrastó con la auditoría anterior y con
   `docs/BlenderPlugin`.
2. Contraste de cada documento canónico (`docs/AppBackend`, `docs/AppFrontend`,
   `docs/BlenderPlugin`, `README.md`, `tests/README.md`) con el código vigente.
3. Comprobaciones ejecutadas (detalle en [evidencias](2026-10-29-evidencias.json)):
   suite `unittest`, importación del módulo web, comprobación documental,
   comparación del ZIP de Blender con sus fuentes, historial Git de las
   constantes eliminadas.

**No se ejecutó:** el arranque de Docker Compose, la base PostgreSQL ni las
pruebas de persistencia (necesitan una base migrada y no hay migraciones, B-02).
Tampoco se ejecutaron Blender (no está en el PATH de este equipo), pruebas E2E en
navegador, carga, escaneo de CVE, de licencias o de secretos, linters ni tipos
estáticos. Ninguna afirmación de escalabilidad se basa en mediciones.

### Criterios

- **P0:** impide que el producto funcione en la rama principal. **P1:** corrección,
  integridad, disponibilidad o seguridad significativas. **P2:** confiabilidad,
  mantenibilidad, contratos o escalabilidad. **P3:** observación de bajo impacto.
- **CONFIRMADO:** reproducido o inequívoco por lectura. **RIESGO:** consecuencia
  condicionada, no reproducida. **DISEÑO:** valoración sin medición.
- Las rutas son relativas a la raíz y las líneas corresponden a `e56df68`.

## Hallazgos priorizados

### B-01 · P0 · `master` no importa: se eliminaron constantes que siguen en uso

**Estado:** CONFIRMADO por reproducción.

- **Evidencia:** `web/persistence/Contratos.py` ya no define `ESQUEMA_PARAMETROS`,
  `ESQUEMA_NORMALIZACION`, `VERSION_LECTOR` ni `VERSION_EXPORTADOR`. Se eliminaron
  en el commit `7ac5834`; en `f02a184` valían `1`, `1`, `"LectorSuperficie-1"` y
  `"GeneradorWeb.Stl-1"`. Siguen importándolas:
  - `web/services/ServicioImports.py:26-31` y su uso en `:184`;
  - `web/services/ServicioLotes.py:17-22` y sus usos en `:199` y `:202`;
  - `web/services/ServicioVersiones.py:18` y su uso en `:77`;
  - `scripts/MigrarSubidas.py:27` y su uso en `:92`.

  `python -c "import web.GenerateModelsApp"` termina con
  `ImportError: cannot import name 'ESQUEMA_NORMALIZACION'`.
- **Consecuencia:** no arrancan la web (`rxconfig.py` → `web.GenerateModelsApp`
  → `GeneradorWeb` → `ServicioImports`), el trabajador
  (`TrabajadorGeneracion` importa `ServicioImports`) ni la migración de subidas.
  Tres módulos de prueba fallan al importarse y 27 casos no se ejecutan.
- **Agravante documental:** la entrada del 2026-10-13 de
  `docs/Agents/REGISTRO_CAMBIOS.md` afirma que las constantes «no tenían
  consumidores». La evidencia citada allí, una búsqueda en el repositorio, no
  basta para respaldar esa afirmación.
- **Recomendación:** restituirlas con los mismos valores, porque se graban en
  columnas `*_version` y una variación rompería la trazabilidad. También es
  posible moverlas a un módulo de contrato y corregir todos los imports. Añadir
  una prueba de humo que importe `web.GenerateModelsApp` y
  `web.jobs.TrabajadorGeneracion`.
- **Validación:** importar ambos módulos sin errores; `unittest discover` sin
  `_FailedTest`.

### B-02 · P1 · No hay revisiones Alembic: el esquema no se puede crear desde el repositorio

**Estado:** CONFIRMADO.

- **Evidencia:** `db/alembic/versions/` solo contiene `.gitkeep`.
  `docs/AppBackend/OPERACION_Y_PRUEBAS.md` («Base de datos: inicializar y migrar»)
  explica que la función y el trigger `model_versions_comprobar`, los `GRANT` de
  `ortesislab_app`/`ortesislab_worker` y la FK circular
  `batch_items_winning_attempt_fk` deben añadirse a mano. Su SQL solo existe como
  texto en `DATABASE.md` §12. `db/test/preparar_base.sql` no crea tablas.
- **Consecuencia:** un clon nuevo no puede crear la base. Los roles de aplicación
  no tienen permisos sobre tablas hasta que alguien escriba la migración. Las
  pruebas de persistencia se omiten siempre. El propio repositorio declara que
  la persistencia SQLAlchemy «no se ha probado contra PostgreSQL».
- **Recomendación:** versionar la revisión inicial con trigger, `GRANT` y FK
  diferida explícitos, y añadir un job de CI con PostgreSQL de servicio que
  ejecute `alembic upgrade head`, `alembic check` y `tests/persistencia`.
- **Validación:** `make db-test-reset && uv run alembic -x base=test upgrade head`;
  pruebas de persistencia sin omisiones.

### B-03 · P1 · No hay integración continua de pruebas ni de calidad

**Estado:** CONFIRMADO.

- **Evidencia:** `.github/workflows/` solo contiene `notion-to-issues.yml`. No hay
  ningún job de `uv sync`, `unittest`, importación ni `GenerarIndices --comprobar`.
- **Consecuencia:** B-01 entró en `master` mediante el PR #18 sin que nada lo
  detectara. La deriva documental (B-17) tampoco se bloquea.
- **Recomendación:** un workflow por PR con `uv sync --locked`, la prueba de humo
  de B-01, `unittest discover -s tests`, `GenerarIndices.py --comprobar` y, al
  resolver B-02, un servicio PostgreSQL, MinIO (o moto) y Redis.
- **Validación:** un PR que reintroduzca B-01 debe fallar en CI.

### B-04 · P1 · La normalización de superficies consume CPU en el proceso web

**Estado:** DISEÑO + CONFIRMADO por lectura; impacto no medido.

- **Evidencia:** `EstadoApp.CargarSuperficie` (`web/EstadoApp.py:240`) llama, con
  `asyncio.to_thread`, a `GeneradorWeb.GuardarSuperficie` →
  `ServicioImports.Importar` → `LectorSuperficie.Preparar` →
  `AnalizadorMalla.Preparar`. El proceso trata hasta 50 MiB de STL/NPZ: fusión
  de vértices con `np.unique`, topología y Dijkstra. Además,
  `CargarPredeterminados` (`:313-314`) llama a `GeneradorWeb.EjeMayor("")` en
  cada carga de página. Sin Redis, eso prepara la plantilla completa cada vez
  (`GeneradorWeb.Cruda` → `ServicioImports.PrepararPlantilla`).
- **Consecuencia:** las subidas concurrentes ocupan el `ThreadPoolExecutor` por
  defecto, de `min(32, CPU+4)` hilos. Ese pool también atiende la resolución de
  sesión de todos los eventos, así que la interfaz completa se ralentiza. Esto
  contradice la intención de «mover la generación fuera del proceso web».
- **Recomendación:** convertir la normalización en trabajo del trabajador, con
  un import en estado `validating` encolado. Como alternativa, usar un
  `ProcessPoolExecutor` acotado. Guardar el eje mayor de la plantilla en una
  constante calculada una vez por proceso.
- **Validación:** prueba de carga con N subidas simultáneas y medición de la
  latencia de un evento trivial (`set_*`) durante la subida.

### B-05 · P1 · No hay cuota de almacenamiento ni límite de tasa por usuario

**Estado:** CONFIRMADO por ausencia de controles; agotamiento no provocado.

- **Evidencia:** `ServicioImports._Registrar` (`web/services/ServicioImports.py:158-231`)
  guarda el original (≤ 50 MiB) y el NPZ normalizado sin consultar cuánto ocupa
  ya el usuario. `ConciliadorArchivos` solo borra objetos `staged` vencidos e
  imports rechazados. Los imports `ready` y los STL/JSON de resultados no tienen
  retención. Los YAML de `config/` no tienen ninguna clave de cuota de bytes,
  de imports ni de inicios de sesión. El único límite es 3 lotes pendientes y
  12 ítems (`persistencia.yaml`).
- **Consecuencia:** un usuario autenticado puede llenar el bucket o el disco de
  MinIO subiendo variantes de un archivo o generando lotes en bucle. Lo heredado
  de A-03 sigue vigente en la nueva arquitectura.
- **Recomendación:** cuota de bytes e imports por usuario, comprobada bajo el
  advisory lock del usuario; tasa máxima de subidas y lotes por ventana; política
  de retención documentada.
- **Validación:** prueba de persistencia que supere la cuota y reciba
  `CuotaExcedida`.

### B-06 · P1 · Un import puede quedar en `received` indefinidamente

**Estado:** CONFIRMADO por lectura; fallo no provocado.

- **Evidencia:** en `ServicioImports._Registrar`, la transacción `recibir` confirma
  el import (`received`) y el asset original (`staged`) **antes** de
  `Almacen.Actual().Publicar(...)` (`:191-192`). Solo se capturan `ValueError` y
  `OrtesisLabError` (`:196`). Si la subida falla con `AlmacenamientoNoDisponible`,
  si la normalización lanza otra excepción (`MemoryError`, `IndexError` de NumPy)
  o si falla la subida del NPZ (`:216`), el import queda `received` sin evento
  `import_rejected`. El conciliador borra el asset `staged` a las 24 h, pero no
  toca el import.
- **Consecuencia:** quedan filas `imports` huérfanas que apuntan a un asset
  `deleted`. El historial no registra ningún fallo y las métricas de imports se
  distorsionan.
- **Recomendación:** usar `try/except BaseException` para marcar `rejected` con
  `error_code` antes de relanzar, y que el conciliador barra los imports en
  `received`/`validating` antiguos.
- **Validación:** prueba con un almacén falso que lance en `Publicar`; el import
  debe quedar `rejected`.

### B-07 · P3 · La deduplicación de imports no es atómica

**Estado:** CONFIRMADO por lectura (no hay restricción única); carrera no provocada.

- **Evidencia:** `RepositorioImports.ListoPorOriginal` solo encuentra imports
  `ready`, y la comprobación se hace fuera del alta. `Modelos.py` no tiene una
  restricción única `(user_id, project_id, sha256)` para imports.
- **Consecuencia:** dos subidas simultáneas del mismo archivo (dos pestañas)
  crean dos imports y duplican el almacenamiento.
- **Recomendación:** tomar el advisory lock del usuario durante el alta, o un
  índice único parcial sobre el SHA del original.

### B-08 · P2 · Límites de lote duplicados entre YAML y esquema

**Estado:** CONFIRMADO.

- **Evidencia:** `web/persistence/Modelos.py:361` fija `CHECK total_items BETWEEN 1 AND 12`.
  El máximo se declara también en `config/persistencia.yaml` (`lotes.maximo_items`)
  y `config/web.yaml` (`maximo_variantes`). La documentación presenta los YAML
  como el lugar donde ajustar estos valores.
- **Consecuencia:** subir ambos valores por encima de 12 hace que el `INSERT` falle
  con `IntegrityError`. Ese error no es `ErrorPersistencia`, cae en la rama
  genérica de `EstadoApp.Generar` (`:406-413`) y el usuario solo ve «No se pudo
  registrar la generación».
- **Recomendación:** una sola fuente. Si el `CHECK` se conserva, documentar que
  cambiar el máximo exige una migración y verificarlo al arrancar.

### B-09 · P2 · La configuración YAML no se valida al cargarse

**Estado:** CONFIRMADO.

- **Evidencia:** `ConfiguracionBackend.Cargar` (`web/ConfiguracionBackend.py:18-22`)
  devuelve el `dict` de `yaml.safe_load` sin esquema. Una clave ausente provoca
  `KeyError` al importar el módulo consumidor. Un tipo erróneo, como
  `lease_s: "120"`, falla después en tiempo de ejecución. Las relaciones
  `latido_s < lease_s` y `maximo_variantes ≤ maximo_items` están documentadas
  como «que el código no comprueba».
- **Recomendación:** dataclasses tipadas por área y validación de relaciones al
  arrancar web y trabajador.

### B-10 · P2 · El progreso se obtiene por sondeo y `Crear` bloquea un hilo hasta 600 s

**Estado:** DISEÑO; carga no medida.

- **Evidencia:** `EstadoApp._Seguir` (`web/EstadoApp.py:550-566`) ejecuta
  `ServicioLotes.Progreso` cada `intervalo_progreso_s` (1 s) por pestaña con un
  lote abierto. La consulta es `RepositorioLotes.Items`: seis tablas unidas más
  una subconsulta correlacionada `UltimoError` por ítem. `GeneradorWeb.Crear`
  (`web/GeneradorWeb.py:155-175`) llama a `ServicioLotes.Esperar`, que hace
  `time.sleep` en un hilo hasta `espera_crear_s` (600 s).
- **Consecuencia:** el coste en PostgreSQL crece linealmente con las pestañas
  abiertas (≈ 1 consulta pesada/s cada una). Cada llamada a `Crear` retiene un
  hilo del pool compartido.
- **Recomendación:** notificación (`LISTEN/NOTIFY` o pub/sub de Redis) o, como
  mínimo, sondeo con retroceso progresivo y una consulta ligera que solo
  compruebe el estado.

### B-11 · P2 · Capacidad del trabajador sin medir y serializada por usuario

**Estado:** DISEÑO.

- **Evidencia:** `RepositorioLotes._Candidato` excluye a los usuarios con un ítem
  `running` y cada proceso trabajador procesa un ítem cada vez
  (`TrabajadorGeneracion.Ciclo`). La interfaz anuncia «cerca de 20 segundos»
  por variante (`EstadoApp.mensaje`), una cifra que no tiene evidencia medida en
  el repositorio.
- **Consecuencia:** un lote de 12 variantes tarda ≈ 12 × t por usuario, sin
  importar cuántos trabajadores haya. La capacidad total es procesos × 1/t.
- **Recomendación:** medir t por patrón y tamaño de malla, publicar la capacidad
  y permitir configurar la concurrencia por usuario.

### B-12 · P2 · El conciliador recorre todo el bucket en cada pasada

**Estado:** DISEÑO.

- **Evidencia:** `ConciliadorArchivos.Ejecutar` (`web/jobs/ConciliadorArchivos.py:66-73`)
  lista todo `usuarios/` cada `conciliacion_s` (600 s) y consulta la base en
  bloques de 500 claves. Además hace `HEAD` de 200 assets `ready` por pasada
  (`lote_comprobacion`).
- **Consecuencia:** el coste es O(objetos) por pasada. Con N assets `ready`, una
  vuelta completa de comprobación tarda N/200 × 600 s, unos 35 días para un
  millón.
- **Recomendación:** reglas de ciclo de vida del bucket o S3 Inventory, cursor
  por fecha y métricas de conciliación.

### B-13 · P2 · Retención y borrado de datos sin definir

**Estado:** CONFIRMADO por ausencia.

- **Evidencia:** no hay purga de `auth_sessions` vencidas o revocadas ni de
  `history_events`. `EstadoUsuario.DELETION_PENDING` (`web/enums/Usuarios.py`) y
  `TipoEvento.PROJECT_ARCHIVED` existen sin ningún flujo que los use. No hay
  exportación ni borrado de cuenta.
- **Consecuencia:** las superficies proceden de anatomía de pacientes, por lo que
  son datos potencialmente sensibles. Sin una política de retención ni de
  borrado no se puede atender una solicitud de supresión, y las tablas crecen
  sin límite.
- **Recomendación:** definir una política (decisión del responsable del producto),
  un job de purga y un flujo de borrado de cuenta que recorra base y bucket.

### B-14 · P2 · Los STL se leen sin autenticación y el visor carga código de terceros sin integridad

**Estado:** CONFIRMADO; decisión de diseño documentada sin `RIESGO_ACEPTADO`.

- **Evidencia:** `infra/database/minio/politica-lectura-stl.json` concede
  `s3:GetObject` anónimo a `usuarios/*/assets/*.stl`. `assets/visor.html:14`
  importa `three@0.169.0` desde unpkg sin `integrity`, y en `:18` y `:78` hace
  `fetch` de cualquier `src` sin comprobar el origen.
- **Consecuencia:** quien obtenga la URL (por historial, registros, Referer o
  copiar y pegar) descarga la geometría derivada del paciente sin caducidad. Un
  compromiso de unpkg ejecuta código en el origen de la aplicación.
  `docs/AppBackend/ARQUITECTURA.md` lo recoge como «decisión de esta entrega»,
  pero no hay ningún resolve con autorización explícita del riesgo.
- **Recomendación:** URL prefirmadas de vida corta o un proxy autenticado; servir
  Three.js localmente con SRI; restringir `src` a la base pública del bucket.
  Si se mantiene, registrar `RIESGO_ACEPTADO` con autorización.

### B-15 · P3 · El cierre de sesión acepta GET y no se verifica el origen

**Estado:** CONFIRMADO por lectura; ataque no reproducido.

- **Evidencia:** `Route("/logout", logout)` (`web/services/AutenticacionOidc.py:86`, handler en `:72-79`)
  responde a GET. `rxconfig.py` no configura `cors_allowed_origins`.
- **Consecuencia:** cualquier página puede cerrar la sesión con una navegación de
  primer nivel (CSRF de logout). El impacto es bajo, porque `SameSite=Lax`
  impide el envío cruzado en subrecursos y WebSocket.
- **Recomendación:** logout por POST con token y orígenes permitidos explícitos.

### B-16 · P2 · El ZIP de Blender versionado no coincide con su guía

**Estado:** CONFIRMADO.

- **Evidencia:** los 26 `.py`/`.json` de `GenerateModelsApp.zip` coinciden byte a
  byte con las fuentes, pero `GenerateModelsApp/LEEME.md` del ZIP no coincide
  con `docs/BlenderPlugin/LEEME.md` (SHA-256 distinto). La última modificación
  del ZIP es del 2026-10-05.
- **Recomendación:** regenerar con `scripts/EmpaquetarBlender.py`, ejecutar
  `tests/blender/blender_paquete_zip.py` y comprobar la coincidencia en CI.

### B-17 · P2 · Deriva documental y conflicto entre la regla de mantenimiento y el bloqueo

**Estado:** CONFIRMADO.

- **Evidencia:**
  - `python docs/Agents/Scripts/GenerarIndices.py --comprobar` informa de que
    `docs/AppBackend/SIMBOLOS.md` y `docs/Agents/INVENTARIO.md` están
    desactualizados, y de que hay 4 archivos sin descripción en el inventario.
  - `docs/README.md:9` enlaza `audit/README.md`, pero la carpeta es `Audit`. El
    enlace se rompe en sistemas sensibles a mayúsculas (GitHub, Linux). El
    comprobador no lo detecta en Windows porque `Path.exists` no distingue
    mayúsculas y además excluye `Audit` de la revisión de enlaces.
  - `docs/AppBackend/CONTRATOS.md` documenta `mode` = `single`, `batch`,
    `retry`; el código y el `CHECK` usan `sweep` (`web/enums/Lotes.py:12`,
    `web/EstadoApp.py:393`).
  - `docs/AppBackend/MODULOS.md` y `OPERACION_Y_PRUEBAS.md` describen
    «constantes de versión» de `Contratos.py` que ya no existen (B-01).
  - La línea base de pruebas documentada (73 pruebas: 50 aprobadas y 23
    omitidas) no se reproduce: hoy se cargan 46 casos, aprueban 38, se omiten 8
    y 27 no se cargan.
  - `AGENTS.md` exige regenerar `INVENTARIO.md`, `SIMBOLOS.md` y
    `REGISTRO_CAMBIOS.md` en cada cambio. Esos archivos pertenecen al inventario
    bloqueado de `AUD-2026-10-13-001`, así que la regla de mantenimiento y la de
    bloqueo se contradicen.
- **Recomendación:** autorización explícita para tocar la documentación afectada,
  registrada en un resolve. Hacer el comprobador sensible a mayúsculas y
  comprobar también `docs/README.md` frente a `docs/Audit`.

### B-18 · P2 · No hay estándares de ingeniería ejecutables

**Estado:** CONFIRMADO.

- **Evidencia:** `pyproject.toml` no configura linter, formateador ni verificador
  de tipos. Su `description` sigue siendo la de la plantilla («Add your
  description here»). `src/generatemodelsapp/__init__.py` y el script
  `generatemodelsapp` son un saludo de plantilla, y `.vscode/settings.json` está
  vacío. `docs/Agents/ESTANDAR_DOCUMENTACION.md` regula la documentación, no el
  código.
- **Recomendación:** adoptar `ruff` (lint y formato) y `mypy` o `pyright` con una
  línea base en CI. La convención PascalCase de métodos es del proyecto y debe
  quedar declarada como excepción.

### B-19 · P2 · Las versiones web guardan parámetros que no influyen en la geometría web

**Estado:** CONFIRMADO por lectura.

- **Evidencia:** `repair` y `resolution_mm` forman parte de las 17 opciones y del
  hash de la versión (`ServicioVersiones.Insertar`). Sin embargo,
  `Model3DForPrinting.ConstruirGeometria` (`GenerateModelsApp/Modeling.py:113-160`)
  no los usa: solo sirven al voxel de Blender. La web produce el alcance
  `pre_voxel_shell` y siempre `validation_status = not_checked`.
- **Consecuencia:** dos versiones con geometría idéntica tienen huellas
  distintas, y `/historial` presenta como «cambios» parámetros sin efecto.
- **Recomendación:** documentarlo en el contrato de versión o excluir esas claves
  del hash y de la comparación en la web.

### B-20 · P3 · Un ítem puede terminar `succeeded` en un lote cancelado

**Estado:** CONFIRMADO por lectura; carrera no provocada.

- **Evidencia:** el trabajador consulta `CancelacionPedida` antes de publicar
  (`web/jobs/TrabajadorGeneracion.py:95`), pero `ServicioLotes.Confirmar` no lo
  vuelve a comprobar dentro de su transacción.
- **Consecuencia:** un lote `cancelled` puede contener ítems `succeeded` con un
  STL publicado. El impacto es bajo, pero contradice el mensaje «Lote cancelado».
- **Recomendación:** decidir la política y comprobarla en `Confirmar`.

### B-21 · P3 · La sincronización Notion → GitHub no es atómica

**Estado:** CONFIRMADO por lectura.

- **Evidencia:** `.github/scripts/notion_sync_issues.py:113-117` crea la issue y
  después actualiza Notion. Si la actualización falla, la siguiente ejecución
  duplica la issue. Los identificadores de la base están fijos en el workflow.
- **Recomendación:** buscar una issue existente por un marcador antes de crearla.

### B-22 · P2 · La cancelación de lotes no tiene control en la interfaz

**Estado:** CONFIRMADO por lectura.

- **Evidencia:** `EstadoApp.CancelarLote` (`web/EstadoApp.py:441-451`) no aparece
  en ningún componente: `grep CancelarLote web/Pagina*.py` no devuelve nada.
  `docs/AppBackend/CONTRATOS.md` lo presenta como evento público de `/`.
  `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md:144` sí reconoce que falta el botón.
- **Consecuencia:** el usuario no puede liberar la cuota de 3 lotes pendientes
  ni detener un lote erróneo de 12 variantes; tiene que esperar a que termine.
- **Recomendación:** añadir un botón «Cancelar» visible con un lote abierto
  (`ocupado`), o documentar que la cancelación no está expuesta.
- **Validación:** prueba E2E: lote de 12 variantes, cancelar, lote `cancelled`.

## Matriz de impacto y esfuerzo

| Prioridad | Hallazgo | Impacto | Esfuerzo | Orden |
|---|---|---|---|---|
| P0 | B-01 | Bloqueante | Bajo (restituir 4 constantes y añadir una prueba) | 1 |
| P1 | B-03 | Alto (previene regresiones) | Bajo | 2 |
| P1 | B-02 | Alto | Medio (revisión inicial y CI con PostgreSQL) | 3 |
| P1 | B-06 | Medio | Bajo | 4 |
| P1 | B-05 | Alto en producción | Medio | 5 |
| P1 | B-04 | Alto bajo carga | Medio/alto | 6 |
| P2 | B-17, B-16 | Medio (confianza en la documentación) | Bajo, requiere autorización | 7 |
| P2 | B-08, B-09 | Medio | Bajo | 8 |
| P2 | B-14 | Medio (privacidad) | Medio | 9 |
| P2 | B-13 | Medio (cumplimiento) | Medio; requiere decisión | 10 |
| P2 | B-10, B-11, B-12 | Medio a escala | Medio | 11 |
| P2 | B-22 | Medio (cuota bloqueada) | Bajo | 12 |
| P2 | B-18, B-19 | Bajo/medio | Bajo | 13 |
| P3 | B-07, B-15, B-20, B-21 | Bajo | Bajo | 14 |

## Estado observado de AUD-2026-10-13-001

`git diff --stat 2b74669 HEAD -- GenerateModelsApp/` está vacío: el núcleo no
cambió. Ninguna fila cierra hallazgos: cerrarlos exige un resolve con evidencia.

| Hallazgo | Ubicación principal | Observación en `e56df68` |
|---|---|---|
| A-01, A-04, A-05, A-06, A-11, A-13, A-14, A-15, A-16, A-17, A-22 | Núcleo `GenerateModelsApp/` y `web/LectorSuperficie.py` | Código sin cambios; siguen aplicándose |
| A-08, A-09 | Adaptadores Blender | Sin cambios |
| A-02 | Subidas en carpeta servida | La arquitectura cambió: originales y NPZ van al bucket, sin lectura anónima. Requiere un resolve con evidencia (por ejemplo, `uploaded_files/` vacío y política aplicada) |
| A-03 | Presupuestos y almacenamiento | Parcialmente reemplazado por cuotas de lote; sin cuota de bytes (B-05) |
| A-07 | Descarga web sin validación final | Sigue: `validation_status = not_checked` en la web |
| A-10 | Publicación STL/JSON no consistente | Ahora hay registro `staged` → `ready` en una transacción (`ServicioLotes.Confirmar`); requiere verificación con base real |
| A-12 | Cachés globales | Sustituidas por Redis por contenido; `GeneradorWeb._HuellaPlantilla` sigue con `lru_cache` |
| A-18, A-19 | Contratos/EPS y cobertura | Siguen; ver [faltantes](2026-10-29-documentacion/faltantes.md) |
| A-20, A-21 | Accesibilidad y visor | Sin cambios en el visor; ver B-14 |

## Documentación granular producida

Está en [2026-10-29-documentacion/](2026-10-29-documentacion/README.md). Es una
**propuesta** que no sustituye a los documentos canónicos, bloqueados por
`AUD-2026-10-13-001`. Incluye:

- el mapa por áreas;
- el registro de cobertura de cada archivo mantenido;
- la documentación por módulo y función del backend, el frontend y el núcleo;
- las máquinas de estado;
- la configuración completa;
- la infraestructura local;
- la matriz de pruebas;
- la [lista de aspectos que faltan](2026-10-29-documentacion/faltantes.md).

## Riesgos residuales y cuestiones abiertas

| Cuestión | Responsable | Bloquea |
|---|---|---|
| ¿Se acepta la lectura anónima de STL (B-14) o se pasa a URL prefirmadas? | Responsable del producto | Cierre de B-14 |
| ¿Qué política de retención y borrado aplica a las superficies de pacientes? | Responsable del producto / legal | B-13 |
| ¿Se autoriza editar documentación canónica bloqueada para corregir la deriva? | Usuario | B-17 y la regla de mantenimiento de `AGENTS.md` |
| ¿Qué capacidad objetivo (usuarios simultáneos, lotes por hora) debe soportarse? | Responsable del producto | Puntuar escalabilidad con medición (B-10–B-12) |

Esta auditoría no prueba ausencia de vulnerabilidades, no midió carga y no
ejecutó la persistencia contra PostgreSQL. Los archivos del
[inventario](2026-10-29-inventario.json) quedan `PENDIENTE` y bloqueados según
`AGENTS.md`. Los que ya estaban en `AUD-2026-10-13-001` necesitan resolución de
**ambas** auditorías.
