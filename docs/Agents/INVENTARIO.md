# Inventario completo del repositorio

> Generado por `python docs/Agents/Scripts/GenerarIndices.py`. Incluye archivos versionados y nuevos no ignorados; excluye Git, dependencias y salidas locales ignoradas. Las descripciones de la tabla se editan a mano y el script las conserva.

Los catálogos de [backend](../AppBackend/MODULOS.md), [frontend](../AppFrontend/COMPONENTES_Y_FLUJOS.md) y [plugin](../BlenderPlugin/MODULOS.md) explican las colaboraciones. Aquí se asigna propósito a cada archivo propio; no se atribuye lógica de aplicación a librerías de terceros.

| Archivo | Propósito |
|---|---|
| [.agents/skills/reflex-docs/SKILL.md](../../.agents/skills/reflex-docs/SKILL.md) | Skill local Reflex: instrucciones y referencias para agentes. |
| [.agents/skills/reflex-process-management/SKILL.md](../../.agents/skills/reflex-process-management/SKILL.md) | Skill local Reflex: instrucciones y referencias para agentes. |
| [.agents/skills/setup-python-env/SKILL.md](../../.agents/skills/setup-python-env/SKILL.md) | Skill local Reflex: instrucciones y referencias para agentes. |
| [.codegraph/.gitignore](../../.codegraph/.gitignore) | Excluye el índice local de CodeGraph del versionado. |
| [.env.example](../../.env.example) | Plantilla de variables `ORTESISLAB_*` de la aplicación, el trabajador y las pruebas. |
| [.gitignore](../../.gitignore) | Excluye entornos, compilación, estados, subidas anteriores, logs y `.env`. |
| [.python-version](../../.python-version) | Selecciona el intérprete Python del proyecto para uv. |
| [.vscode/settings.json](../../.vscode/settings.json) | Configuración local de editor; actualmente objeto vacío. |
| [AGENTS.md](../../AGENTS.md) | Instrucciones Reflex y obligación de mantenimiento documental para agentes. |
| [CLAUDE.md](../../CLAUDE.md) | Entrada de instrucciones que remite a AGENTS.md. |
| [Makefile](../../Makefile) | Instalar, levantar, probar y lintear. Cinco objetivos de infraestructura local: `db-up`, `db-down`, `db-estado`, `db-respaldo` y `db-reset`. |
| [README.md](../../README.md) | Presentación, instalación y entradas a documentación. |
| [alembic.ini](../../alembic.ini) | Configuración de Alembic: carpeta `apps/db/alembic`, plantilla de revisiones y logging. La URL la aporta `env.py` desde `Ajustes`. |
| [apps/db/.env.example](../../apps/db/.env.example) | Plantilla de secretos, usuarios y puertos de Compose. |
| [apps/db/.gitattributes](../../apps/db/.gitattributes) | Fuerza LF en scripts, SQL y JSON que se ejecutan en contenedores. |
| [apps/db/.gitignore](../../apps/db/.gitignore) | Excluye .env y volcados de backups. |
| [apps/db/alembic/env.py](../../apps/db/alembic/env.py) | Entorno de Alembic: migra el esquema ortesislab con el rol migrador. |
| [apps/db/alembic/script.py.mako](../../apps/db/alembic/script.py.mako) | Plantilla con la que Alembic crea cada archivo de revisión. |
| [apps/db/alembic/versions/.gitkeep](../../apps/db/alembic/versions/.gitkeep) | Conserva la carpeta de revisiones de Alembic. |
| [apps/db/alembic/versions/20261112_1118_cuentas_locales.py](../../apps/db/alembic/versions/20261112_1118_cuentas_locales.py) | cuentas_locales |
| [apps/db/alembic/versions/20261112_1135_purga_trabajador.py](../../apps/db/alembic/versions/20261112_1135_purga_trabajador.py) | purga del trabajador |
| [apps/db/alembic/versions/20261112_1716_select_sesiones_trabajador.py](../../apps/db/alembic/versions/20261112_1716_select_sesiones_trabajador.py) | select de sesiones para el trabajador |
| [apps/db/backups/.gitkeep](../../apps/db/backups/.gitkeep) | Conserva la carpeta de volcados; su contenido se ignora. |
| [apps/db/compose.yaml](../../apps/db/compose.yaml) | PostgreSQL 17, Redis, MinIO y cliente mc. |
| [apps/db/init/01_roles.sh](../../apps/db/init/01_roles.sh) | Crea los roles separados al inicializar el volumen de PostgreSQL. |
| [apps/db/minio/inicializar.sh](../../apps/db/minio/inicializar.sh) | Crea bucket, políticas y cuenta de servicio en MinIO. |
| [apps/db/minio/politica-aplicacion.json](../../apps/db/minio/politica-aplicacion.json) | Permisos S3 de la cuenta de servicio del backend. |
| [apps/db/minio/politica-lectura-stl.json](../../apps/db/minio/politica-lectura-stl.json) | Lectura anónima solo de `usuarios/*/assets/*.stl`. |
| [apps/db/preparar_base.sql](../../apps/db/preparar_base.sql) | Tras `make db-reset`, recrea el esquema `ortesislab` y los permisos. No crea tablas. |
| [apps/ortesis-plugin/OrtesisLabPlugin/ApiBlender.py](../../apps/ortesis-plugin/OrtesisLabPlugin/ApiBlender.py) | API de Blender, separada del núcleo geométrico. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py) | Recorte de celdas y cascarón de espesor variable. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py) | Errores de OrtesisLab. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py) | Exporta el STL en milímetros y un JSON con parámetros y comprobación. |
| [apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py) | Inspección de cabeceras NPY dentro de un NPZ, sin materializar arrays grandes. |
| [apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py) | Instantánea evaluada de mallas Blender y publicación atómica de archivos. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py) | Panel N y operadores de OrtesisLab en la vista 3D. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Malla.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py) | Análisis de la superficie abierta, sin Blender. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py) | Modelo de impresión y construcción de la geometría. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py) | Crea o actualiza el objeto OL_Ortesis en la escena de Blender. |
| [apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py) | Complemento OrtesisLab dentro del paquete. |
| [apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py) | Refinamiento triangular independiente de Blender para evaluar patrones. |
| [apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py) | Limpieza segura de la superficie base dentro de Blender. |
| [apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py) | Suavizado del contorno exterior antes de dar espesor. |
| [apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py) | Carga y lectura de la superficie interior dentro de Blender. |
| [apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py) | Comprobación geométrica de la malla ya generada. |
| [apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py) | Validación de mallas sólidas solo con NumPy (sin Blender). |
| [apps/ortesis-plugin/OrtesisLabPlugin/__init__.py](../../apps/ortesis-plugin/OrtesisLabPlugin/__init__.py) | Paquete del complemento de Blender y del núcleo de geometría. |
| [apps/ortesis-plugin/OrtesisLabPlugin/consola.py](../../apps/ortesis-plugin/OrtesisLabPlugin/consola.py) | Punto de entrada de consola ``ortesislab``. |
| [apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py) | Materiales de impresión. |
| [apps/ortesis-plugin/OrtesisLabPlugin/constants/Nombres.py](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Nombres.py) | Nombres estables de objetos, atributos y archivos. |
| [apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py) | Patrones de nervadura. |
| [apps/ortesis-plugin/OrtesisLabPlugin/constants/__init__.py](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/__init__.py) | Constantes de OrtesisLab: nombres, patrones, materiales y límites. |
| [apps/ortesis-plugin/OrtesisLabPlugin/contratos.py](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py) | Contratos compartidos entre núcleo, Blender y la web. |
| [apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py) | Registro de mensajes y lectura de la carpeta config. |
| [apps/ortesis-plugin/OrtesisLabPlugin/util/__init__.py](../../apps/ortesis-plugin/OrtesisLabPlugin/util/__init__.py) | Utilidades compartidas: registro de ejecución y lectura de JSON. |
| [apps/web/.gitignore](../../apps/web/.gitignore) | Excluye `.web`, bytecode, bases SQLite, `.states`, `assets/external/` y `__pycache__` de la aplicación Reflex. |
| [apps/web/assets/README.md](../../apps/web/assets/README.md) | Assets de la aplicación |
| [apps/web/assets/favicon.ico](../../apps/web/assets/favicon.ico) | Icono del sitio. |
| [apps/web/assets/superficie_interior_mm.npz](../../apps/web/assets/superficie_interior_mm.npz) | Superficie de ejemplo incluida para la web. |
| [apps/web/assets/vendor/three-0.169.0.module.js](../../apps/web/assets/vendor/three-0.169.0.module.js) | Three.js que el visor importa para dibujar el STL. |
| [apps/web/assets/visor.html](../../apps/web/assets/visor.html) | Visor Three.js que carga el STL binario desde su object_url. |
| [apps/web/reflex.lock/bun.lock](../../apps/web/reflex.lock/bun.lock) | Resolucion de dependencias del frontend generado. |
| [apps/web/reflex.lock/package.json](../../apps/web/reflex.lock/package.json) | Dependencias del frontend generado por Reflex. |
| [apps/web/requirements.txt](../../apps/web/requirements.txt) | Declara Reflex 0.9.12 para la aplicación web. |
| [apps/web/rxconfig.py](../../apps/web/rxconfig.py) | Marcador de paquete. |
| [apps/web/web/Ajustes.py](../../apps/web/web/Ajustes.py) | Variables de entorno de OrtesisLab: el único lugar que las declara y las lee. |
| [apps/web/web/ConfiguracionBackend.py](../../apps/web/web/ConfiguracionBackend.py) | Valores ajustables del backend, leídos de ``core/config/<area>.yaml``. |
| [apps/web/web/EstadoApp.py](../../apps/web/web/EstadoApp.py) | Estado de la página de comparación. |
| [apps/web/web/EstadoHistorial.py](../../apps/web/web/EstadoHistorial.py) | Estado de /historial: filtros, cursor y comparación de hasta tres versiones. |
| [apps/web/web/GeneradorWeb.py](../../apps/web/web/GeneradorWeb.py) | Genera cascarones para la aplicación web. |
| [apps/web/web/LectorSuperficie.py](../../apps/web/web/LectorSuperficie.py) | Lectura de superficies subidas a la aplicación web. |
| [apps/web/web/OrtesisLabApp.py](../../apps/web/web/OrtesisLabApp.py) | Aplicación Reflex de comparación de ortesis. |
| [apps/web/web/PaginaComparacion.py](../../apps/web/web/PaginaComparacion.py) | Pantalla para previsualizar una ortesis o un lote de variantes. |
| [apps/web/web/PaginaHistorial.py](../../apps/web/web/PaginaHistorial.py) | Pantalla /historial: generaciones del usuario, comparación y restauración. |
| [apps/web/web/PaginaLote.py](../../apps/web/web/PaginaLote.py) | Pantalla /lote: progreso de un lote con una miniatura por variante. |
| [apps/web/web/Sesion.py](../../apps/web/web/Sesion.py) | Barra de sesión común a la comparación y al historial. |
| [apps/web/web/__init__.py](../../apps/web/web/__init__.py) | Aplicación Reflex. |
| [apps/web/web/cache/CacheRedis.py](../../apps/web/web/cache/CacheRedis.py) | Caché compartida de superficies preparadas. |
| [apps/web/web/cache/__init__.py](../../apps/web/web/cache/__init__.py) | Marcador de paquete. |
| [apps/web/web/enums/Archivos.py](../../apps/web/web/enums/Archivos.py) | Tipos y estados de los objetos del bucket registrados en ``file_assets``. |
| [apps/web/web/enums/Historial.py](../../apps/web/web/enums/Historial.py) | Tipos de evento de ``history_events``. |
| [apps/web/web/enums/Imports.py](../../apps/web/web/enums/Imports.py) | Origen, estado y formato de una superficie importada (``imports``). |
| [apps/web/web/enums/Lotes.py](../../apps/web/web/enums/Lotes.py) | Backend de versión, modos de lote y estados de lotes, ítems e intentos. |
| [apps/web/web/enums/Resultados.py](../../apps/web/web/enums/Resultados.py) | Validación y alcance de ``generation_results`` y formato, unidad y estado de ``exports``. |
| [apps/web/web/enums/Usuarios.py](../../apps/web/web/enums/Usuarios.py) | Estados de una cuenta de ``app_users``. |
| [apps/web/web/enums/__init__.py](../../apps/web/web/enums/__init__.py) | Valores cerrados del dominio. Deben coincidir con los ``CHECK`` del esquema. |
| [apps/web/web/jobs/ConciliadorArchivos.py](../../apps/web/web/jobs/ConciliadorArchivos.py) | Conciliación entre filas de ``file_assets`` y objetos del bucket. |
| [apps/web/web/jobs/TrabajadorGeneracion.py](../../apps/web/web/jobs/TrabajadorGeneracion.py) | Trabajador de generación: un ítem a la vez, con lease y latido. |
| [apps/web/web/jobs/__init__.py](../../apps/web/web/jobs/__init__.py) | Marcador de paquete. |
| [apps/web/web/persistence/ConexionPostgres.py](../../apps/web/web/persistence/ConexionPostgres.py) | Motor SQLAlchemy y sesiones por proceso. |
| [apps/web/web/persistence/Contratos.py](../../apps/web/web/persistence/Contratos.py) | DTO y errores de la persistencia. No son entidades ORM. |
| [apps/web/web/persistence/Modelos.py](../../apps/web/web/persistence/Modelos.py) | Modelos declarativos de SQLAlchemy del esquema ``ortesislab``. |
| [apps/web/web/persistence/__init__.py](../../apps/web/web/persistence/__init__.py) | Acceso a PostgreSQL con SQLAlchemy 2.0; el esquema se versiona con Alembic. |
| [apps/web/web/persistence/repositorios/Consultas.py](../../apps/web/web/persistence/repositorios/Consultas.py) | Tablas y fragmentos de consulta que comparten varios repositorios. |
| [apps/web/web/persistence/repositorios/RepositorioAssets.py](../../apps/web/web/persistence/repositorios/RepositorioAssets.py) | Filas de ``file_assets``: el contenido vive en el bucket. |
| [apps/web/web/persistence/repositorios/RepositorioBase.py](../../apps/web/web/persistence/repositorios/RepositorioBase.py) | Clase padre de los repositorios: lectura de filas y conversión a DTO. |
| [apps/web/web/persistence/repositorios/RepositorioHistorial.py](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py) | Eventos de historial y listado de ejecuciones por versión. |
| [apps/web/web/persistence/repositorios/RepositorioImports.py](../../apps/web/web/persistence/repositorios/RepositorioImports.py) | Importaciones de superficies: original recibido y NPZ normalizado. |
| [apps/web/web/persistence/repositorios/RepositorioLotes.py](../../apps/web/web/persistence/repositorios/RepositorioLotes.py) | Lotes, ítems y cola del trabajador: admisión, reserva, lease y cierre. |
| [apps/web/web/persistence/repositorios/RepositorioPreferencias.py](../../apps/web/web/persistence/repositorios/RepositorioPreferencias.py) | Preferencias por usuario con control optimista de revisión. |
| [apps/web/web/persistence/repositorios/RepositorioProyectos.py](../../apps/web/web/persistence/repositorios/RepositorioProyectos.py) | Proyectos del usuario; cada cuenta tiene uno predeterminado. |
| [apps/web/web/persistence/repositorios/RepositorioResultados.py](../../apps/web/web/persistence/repositorios/RepositorioResultados.py) | Resultados geométricos, intentos de una versión y exports STL. |
| [apps/web/web/persistence/repositorios/RepositorioUsuarios.py](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py) | Cuentas locales y sus sesiones de servidor. |
| [apps/web/web/persistence/repositorios/RepositorioVersiones.py](../../apps/web/web/persistence/repositorios/RepositorioVersiones.py) | Versiones inmutables numeradas por proyecto. |
| [apps/web/web/persistence/repositorios/__init__.py](../../apps/web/web/persistence/repositorios/__init__.py) | Repositorios SQLAlchemy, uno por archivo. Reciben una ``Session`` ya abierta y no hacen commit. |
| [apps/web/web/services/Autenticacion.py](../../apps/web/web/services/Autenticacion.py) | Rutas de registro e inicio de sesión: /auth/registro, /auth/login y /auth/logout. |
| [apps/web/web/services/ContextoUsuario.py](../../apps/web/web/services/ContextoUsuario.py) | Principal autenticado de cada operación. |
| [apps/web/web/services/GeneradorGeometrico.py](../../apps/web/web/services/GeneradorGeometrico.py) | Construcción numérica de una versión: métricas, STL y JSON de parámetros. |
| [apps/web/web/services/ServicioHistorial.py](../../apps/web/web/services/ServicioHistorial.py) | Historial por usuario: listado paginado, detalle, restauración y reintento. |
| [apps/web/web/services/ServicioImports.py](../../apps/web/web/services/ServicioImports.py) | Importación de superficies: original y NPZ normalizado en el bucket. |
| [apps/web/web/services/ServicioLotes.py](../../apps/web/web/services/ServicioLotes.py) | Admisión de lotes, progreso y transiciones del trabajador. |
| [apps/web/web/services/ServicioPreferencias.py](../../apps/web/web/services/ServicioPreferencias.py) | Preferencias por usuario con control optimista de revisión. |
| [apps/web/web/services/ServicioVersiones.py](../../apps/web/web/services/ServicioVersiones.py) | Versiones inmutables: snapshot de parámetros, material y escala. |
| [apps/web/web/services/__init__.py](../../apps/web/web/services/__init__.py) | Marcador de paquete. |
| [apps/web/web/storage/AlmacenamientoPrivado.py](../../apps/web/web/storage/AlmacenamientoPrivado.py) | Contrato del almacén de bytes y claves de objeto. |
| [apps/web/web/storage/StorageS3.py](../../apps/web/web/storage/StorageS3.py) | Almacén de bytes en un bucket S3 (MinIO en desarrollo). |
| [apps/web/web/storage/__init__.py](../../apps/web/web/storage/__init__.py) | Marcador de paquete. |
| [core/config/README.md](../../core/config/README.md) | Para qué sirve cada YAML del backend y cada JSON de geometría. |
| [core/config/almacen.yaml](../../core/config/almacen.yaml) | Timeouts de conexion y lectura e intentos del cliente S3. |
| [core/config/cache.yaml](../../core/config/cache.yaml) | TTL, pausa de reintento y timeout de Redis. |
| [core/config/comprobacion_geometrica.json](../../core/config/comprobacion_geometrica.json) | Mediciones historicas de referencia, no umbrales de aceptacion. |
| [core/config/limites.json](../../core/config/limites.json) | Umbrales, tolerancias y presupuestos de algoritmos. |
| [core/config/parametros_defecto.json](../../core/config/parametros_defecto.json) | Valores iniciales de las 17 opciones geometricas. |
| [core/config/persistencia.yaml](../../core/config/persistencia.yaml) | Conexion PostgreSQL, cuotas de lotes y limites del historial. |
| [core/config/registro.json](../../core/config/registro.json) | Niveles de logging y nombre de archivo. |
| [core/config/sesion.yaml](../../core/config/sesion.yaml) | Duración de la sesión de servidor. |
| [core/config/trabajador.yaml](../../core/config/trabajador.yaml) | Lease, latido, supervision y conciliacion del trabajador. |
| [core/config/web.yaml](../../core/config/web.yaml) | Progreso, espera de creacion, tamanos de subida y etiquetas de la app. |
| [docs/Agents/ESTANDAR_DOCUMENTACION.md](ESTANDAR_DOCUMENTACION.md) | Estándar documental |
| [docs/Agents/GUIA_REFLEX.md](GUIA_REFLEX.md) | Reflex Documentation |
| [docs/Agents/INVENTARIO.md](INVENTARIO.md) | Inventario de carpetas y archivos propios (instantánea). |
| [docs/Agents/MANTENIMIENTO.md](MANTENIMIENTO.md) | Mantenimiento automático y revisión de documentación |
| [docs/Agents/README.md](README.md) | Agents |
| [docs/Agents/REGISTRO_CAMBIOS.md](REGISTRO_CAMBIOS.md) | Registro de cambios documentales |
| [docs/Agents/Scripts/GenerarIndices.py](Scripts/GenerarIndices.py) | Regenera los catálogos de hechos de la documentación y comprueba enlaces. |
| [docs/AppBackend/ARQUITECTURA.md](../AppBackend/ARQUITECTURA.md) | Arquitectura interna de AppBackend |
| [docs/AppBackend/CONTRATOS.md](../AppBackend/CONTRATOS.md) | Contratos de AppBackend |
| [docs/AppBackend/DATABASE.md](../AppBackend/DATABASE.md) | Base de datos |
| [docs/AppBackend/MODULOS.md](../AppBackend/MODULOS.md) | Carpetas y archivos de AppBackend |
| [docs/AppBackend/OPERACION_Y_PRUEBAS.md](../AppBackend/OPERACION_Y_PRUEBAS.md) | Operación y pruebas del backend |
| [docs/AppBackend/README.md](../AppBackend/README.md) | AppBackend |
| [docs/AppBackend/SIMBOLOS.md](../AppBackend/SIMBOLOS.md) | Índice de clases, funciones y métodos del backend (instantánea). |
| [docs/AppFrontend/ARQUITECTURA.md](../AppFrontend/ARQUITECTURA.md) | Arquitectura del frontend Reflex |
| [docs/AppFrontend/COMPONENTES_Y_FLUJOS.md](../AppFrontend/COMPONENTES_Y_FLUJOS.md) | Componentes, archivos y flujos de interfaz |
| [docs/AppFrontend/OPERACION_Y_PRUEBAS.md](../AppFrontend/OPERACION_Y_PRUEBAS.md) | Operación y verificación del frontend |
| [docs/AppFrontend/README.md](../AppFrontend/README.md) | AppFrontend |
| [docs/AppFrontend/SIMBOLOS.md](../AppFrontend/SIMBOLOS.md) | Índice de componentes y estado relacionados con el frontend (instantánea). |
| [docs/AppFrontend/VISOR_3D.md](../AppFrontend/VISOR_3D.md) | Visor 3D: código, datos e interacción |
| [docs/Audit/README.md](../Audit/README.md) | Auditorías y resoluciones |
| [docs/Audit/audits/2026-10-13-auditoria-base-codigo.md](../Audit/audits/2026-10-13-auditoria-base-codigo.md) | AUD-2026-10-13-001 — Auditoría de la base de código |
| [docs/Audit/audits/2026-10-13-evidencias.json](../Audit/audits/2026-10-13-evidencias.json) | Archivo auxiliar versionado; revisar su contrato al modificarlo. |
| [docs/Audit/audits/2026-10-13-export-evidence.json](../Audit/audits/2026-10-13-export-evidence.json) | Archivo auxiliar versionado; revisar su contrato al modificarlo. |
| [docs/Audit/audits/2026-10-13-inventario.json](../Audit/audits/2026-10-13-inventario.json) | Archivo auxiliar versionado; revisar su contrato al modificarlo. |
| [docs/Audit/audits/2026-10-29-adenda-cierre-b.md](../Audit/audits/2026-10-29-adenda-cierre-b.md) | Adenda — cierre de hallazgos B-01…B-22 |
| [docs/Audit/audits/2026-10-29-auditoria-evaluacion.md](../Audit/audits/2026-10-29-auditoria-evaluacion.md) | AUD-2026-10-29-002 — Auditoría y evaluación del proyecto |
| [docs/Audit/audits/2026-10-29-documentacion/README.md](../Audit/audits/2026-10-29-documentacion/README.md) | Documentación granular propuesta — AUD-2026-10-29-002 |
| [docs/Audit/audits/2026-10-29-documentacion/backend/configuracion.md](../Audit/audits/2026-10-29-documentacion/backend/configuracion.md) | Backend · Configuración |
| [docs/Audit/audits/2026-10-29-documentacion/backend/integraciones.md](../Audit/audits/2026-10-29-documentacion/backend/integraciones.md) | Backend · Integraciones: bucket S3, Redis, lector de superficies, OIDC |
| [docs/Audit/audits/2026-10-29-documentacion/backend/persistencia.md](../Audit/audits/2026-10-29-documentacion/backend/persistencia.md) | Backend · Persistencia |
| [docs/Audit/audits/2026-10-29-documentacion/backend/servicios-y-flujos.md](../Audit/audits/2026-10-29-documentacion/backend/servicios-y-flujos.md) | Backend · Servicios, flujos y máquinas de estado |
| [docs/Audit/audits/2026-10-29-documentacion/calidad/pruebas-y-estandares.md](../Audit/audits/2026-10-29-documentacion/calidad/pruebas-y-estandares.md) | Calidad · Pruebas y estándares |
| [docs/Audit/audits/2026-10-29-documentacion/cobertura-fuentes.md](../Audit/audits/2026-10-29-documentacion/cobertura-fuentes.md) | Registro de cobertura fuente → documento |
| [docs/Audit/audits/2026-10-29-documentacion/faltantes.md](../Audit/audits/2026-10-29-documentacion/faltantes.md) | Aspectos que faltan o no coinciden con el código |
| [docs/Audit/audits/2026-10-29-documentacion/frontend/estado-paginas-visor.md](../Audit/audits/2026-10-29-documentacion/frontend/estado-paginas-visor.md) | Frontend · Estado, páginas y visor |
| [docs/Audit/audits/2026-10-29-documentacion/identidad/proyecto.md](../Audit/audits/2026-10-29-documentacion/identidad/proyecto.md) | Identidad del proyecto |
| [docs/Audit/audits/2026-10-29-documentacion/infraestructura/entorno-local.md](../Audit/audits/2026-10-29-documentacion/infraestructura/entorno-local.md) | Infraestructura · Entorno local, base de datos y operación |
| [docs/Audit/audits/2026-10-29-documentacion/nucleo-blender/modulos.md](../Audit/audits/2026-10-29-documentacion/nucleo-blender/modulos.md) | Núcleo geométrico y complemento Blender · Catálogo por módulo y función |
| [docs/Audit/audits/2026-10-29-evidencias.json](../Audit/audits/2026-10-29-evidencias.json) | Resultados observados en AUD-2026-10-29-002; no cierran hallazgos. |
| [docs/Audit/audits/2026-10-29-inventario.json](../Audit/audits/2026-10-29-inventario.json) | Inventario y huellas de los archivos de AUD-2026-10-29-002. |
| [docs/Audit/audits/README.md](../Audit/audits/README.md) | Auditorías |
| [docs/Audit/resolves/2026-10-13-firmas-base.json](../Audit/resolves/2026-10-13-firmas-base.json) | Instantánea AST de las 69 firmas públicas de los archivos auditados. |
| [docs/Audit/resolves/2026-10-13-resolve-organizar-pruebas.md](../Audit/resolves/2026-10-13-resolve-organizar-pruebas.md) | RES-2026-10-13-002 — Orden de pruebas y assets de prueba |
| [docs/Audit/resolves/2026-10-13-resolve-persistencia-postgres.md](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md) | RES-2026-10-13-001 — Persistencia PostgreSQL, bucket S3 y caché Redis |
| [docs/Audit/resolves/2026-11-12-issue-1-carga-presupuestos.md](../Audit/resolves/2026-11-12-issue-1-carga-presupuestos.md) | RES-2026-11-12-ISSUE-1 — Blindar carga y presupuestos (A-01, A-03, A-11) |
| [docs/Audit/resolves/2026-11-12-issue-2-riesgo-stl-anonimo.md](../Audit/resolves/2026-11-12-issue-2-riesgo-stl-anonimo.md) | RES-2026-11-12-ISSUE-2 — Lectura anónima del STL (A-02 / B-14 parcial) |
| [docs/Audit/resolves/2026-11-12-issue-3-normales-topologia.md](../Audit/resolves/2026-11-12-issue-3-normales-topologia.md) | RES-2026-11-12-ISSUE-3 — Normales, topología, unidades y resolución (A-04, A-05, A-06, A-14, A-16, A-22) |
| [docs/Audit/resolves/2026-11-12-issue-4-validacion-exportacion.md](../Audit/resolves/2026-11-12-issue-4-validacion-exportacion.md) | Issue #4 — Validación y exportación (A-07, A-08, A-15) |
| [docs/Audit/resolves/2026-11-12-issue-5-rollback-stl-json.md](../Audit/resolves/2026-11-12-issue-5-rollback-stl-json.md) | Issue #5 — Rollback y par STL/JSON (A-09, A-10) |
| [docs/Audit/resolves/2026-11-12-issue-6-cache-metricas.md](../Audit/resolves/2026-11-12-issue-6-cache-metricas.md) | Issue #6 — Caché y métricas (A-12, A-13) |
| [docs/Audit/resolves/2026-11-12-issue-7-contratos-wheel.md](../Audit/resolves/2026-11-12-issue-7-contratos-wheel.md) | Issue #7 — Contratos y consola (A-17, A-18) |
| [docs/Audit/resolves/2026-11-12-issue-8-tests-visor-a11y.md](../Audit/resolves/2026-11-12-issue-8-tests-visor-a11y.md) | Issue #8 — Tests, visor y accesibilidad (A-19, A-20, A-21, B-14) |
| [docs/Audit/resolves/2026-11-12-issue-9-seguimiento.md](../Audit/resolves/2026-11-12-issue-9-seguimiento.md) | RES-2026-11-12-ISSUE-9 — Seguimiento AUD-2026-10-13-001 |
| [docs/Audit/resolves/2026-11-12-issue-b-cierre-parcial-a.md](../Audit/resolves/2026-11-12-issue-b-cierre-parcial-a.md) | RES-2026-11-12-B-A — Cierre parcial hallazgos B (tramo A) |
| [docs/Audit/resolves/2026-11-12-issue-b-cierre-parcial-b.md](../Audit/resolves/2026-11-12-issue-b-cierre-parcial-b.md) | RES-2026-11-12-B-B — Cierre parcial hallazgos B (tramo B) |
| [docs/Audit/resolves/2026-11-12-issue-b-indice.md](../Audit/resolves/2026-11-12-issue-b-indice.md) | Índice de cierre — AUD-2026-10-29-002 (hallazgos B) |
| [docs/Audit/resolves/2026-11-12-resolve-ajustes-entorno.md](../Audit/resolves/2026-11-12-resolve-ajustes-entorno.md) | RES-2026-11-12-001 — Aviso de clave ausente dentro de `Variable.__get__` |
| [docs/Audit/resolves/2026-11-12-resolve-aud-2026-10-29.md](../Audit/resolves/2026-11-12-resolve-aud-2026-10-29.md) | RES-2026-11-12-002 — Cierre hallazgos AUD-2026-10-29-002 (B-01…B-22) |
| [docs/Audit/resolves/2026-11-12-resolve-cierre-issues-auditoria.md](../Audit/resolves/2026-11-12-resolve-cierre-issues-auditoria.md) | RES-2026-11-12-001 — Cierre de issues AUD-2026-10-13-001 (plan autorizado) |
| [docs/Audit/resolves/2026-11-12-resolve-conflictos-merge-login-lote.md](../Audit/resolves/2026-11-12-resolve-conflictos-merge-login-lote.md) | RES-2026-11-12-013 — Resolver el merge entre `/lote` y el login local |
| [docs/Audit/resolves/2026-11-12-resolve-dotenv-raiz.md](../Audit/resolves/2026-11-12-resolve-dotenv-raiz.md) | RES-2026-11-12-003 — Cargar el .env de la raíz con python-dotenv |
| [docs/Audit/resolves/2026-11-12-resolve-fase0-defectos.md](../Audit/resolves/2026-11-12-resolve-fase0-defectos.md) | RES-2026-11-12-014 — Fase 0: defectos que rompen límites, conciliación y purga |
| [docs/Audit/resolves/2026-11-12-resolve-fixture-stl.md](../Audit/resolves/2026-11-12-resolve-fixture-stl.md) | RES-2026-11-12-013 — Fixture STL de las pruebas |
| [docs/Audit/resolves/2026-11-12-resolve-login-local.md](../Audit/resolves/2026-11-12-resolve-login-local.md) | RES-2026-11-12-012 — Login y registro locales |
| [docs/Audit/resolves/2026-11-12-resolve-makefile.md](../Audit/resolves/2026-11-12-resolve-makefile.md) | RES-2026-11-12-006 — Objetivos de Make |
| [docs/Audit/resolves/2026-11-12-resolve-modulo-ortesislabapp.md](../Audit/resolves/2026-11-12-resolve-modulo-ortesislabapp.md) | RES-2026-11-12-010 — El módulo Reflex se llama `OrtesisLabApp` |
| [docs/Audit/resolves/2026-11-12-resolve-monorepo.md](../Audit/resolves/2026-11-12-resolve-monorepo.md) | RES-2026-11-12-001 — Reubicar el repositorio como monorepo |
| [docs/Audit/resolves/2026-11-12-resolve-normal-pliegue.md](../Audit/resolves/2026-11-12-resolve-normal-pliegue.md) | RES-2026-11-12-016 — Normal de un pliegue al refinar |
| [docs/Audit/resolves/2026-11-12-resolve-paquete-ortesislabplugin.md](../Audit/resolves/2026-11-12-resolve-paquete-ortesislabplugin.md) | RES-2026-11-12-008 — El núcleo se importa como `OrtesisLabPlugin` |
| [docs/Audit/resolves/2026-11-12-resolve-quitar-autoescala.md](../Audit/resolves/2026-11-12-resolve-quitar-autoescala.md) | RES-2026-11-12-004 — Quitar el autoescalado de coordenadas |
| [docs/Audit/resolves/2026-11-12-resolve-quitar-seeds-test.md](../Audit/resolves/2026-11-12-resolve-quitar-seeds-test.md) | RES-2026-11-12-005 — Quitar seeds y la base de pruebas |
| [docs/Audit/resolves/2026-11-12-resolve-quitar-src.md](../Audit/resolves/2026-11-12-resolve-quitar-src.md) | RES-2026-11-12-009 — Quitar la carpeta `src` |
| [docs/Audit/resolves/2026-11-12-resolve-quitar-validar-arranque.md](../Audit/resolves/2026-11-12-resolve-quitar-validar-arranque.md) | RES-2026-11-12-011 — Quitar `ValidarEnArranque` del arranque |
| [docs/Audit/resolves/2026-11-12-resolve-rediseno-interfaz-lotes.md](../Audit/resolves/2026-11-12-resolve-rediseno-interfaz-lotes.md) | RES-2026-11-12-011 — Rediseño de la interfaz web: parámetros, lotes y progreso |
| [docs/Audit/resolves/2026-11-12-resolve-revision-alembic.md](../Audit/resolves/2026-11-12-resolve-revision-alembic.md) | RES-2026-11-12-007 — Quitar la revisión de Alembic no generada por Alembic |
| [docs/Audit/resolves/2026-11-12-resolve-select-sesiones-trabajador.md](../Audit/resolves/2026-11-12-resolve-select-sesiones-trabajador.md) | RES-2026-11-12-015 — SELECT de sesiones para el trabajador |
| [docs/Audit/resolves/2026-11-12-resolve-simplificar-carga-yaml.md](../Audit/resolves/2026-11-12-resolve-simplificar-carga-yaml.md) | RES-2026-11-12-001 — Lectura directa del YAML en `Cargar` |
| [docs/Audit/resolves/README.md](../Audit/resolves/README.md) | Resoluciones |
| [docs/BlenderPlugin/ALGORITMOS.md](../BlenderPlugin/ALGORITMOS.md) | Algoritmos de generación y comprobación |
| [docs/BlenderPlugin/API_Y_DATOS.md](../BlenderPlugin/API_Y_DATOS.md) | API Python, contratos y datos de Blender |
| [docs/BlenderPlugin/ARQUITECTURA.md](../BlenderPlugin/ARQUITECTURA.md) | Arquitectura del complemento |
| [docs/BlenderPlugin/CONFIGURACION_GENERADA.md](../BlenderPlugin/CONFIGURACION_GENERADA.md) | Valores exactos de los cuatro JSON del núcleo, generados desde las fuentes. |
| [docs/BlenderPlugin/LEEME.md](../BlenderPlugin/LEEME.md) | OrtesisLab 1.3 — superficie sin espesor |
| [docs/BlenderPlugin/MODULOS.md](../BlenderPlugin/MODULOS.md) | Mapa completo del paquete Blender y del núcleo |
| [docs/BlenderPlugin/OPERACION_Y_PRUEBAS.md](../BlenderPlugin/OPERACION_Y_PRUEBAS.md) | Operación y pruebas del complemento |
| [docs/BlenderPlugin/PARAMETROS.md](../BlenderPlugin/PARAMETROS.md) | Parámetros: propósito, efecto y restricciones |
| [docs/BlenderPlugin/README.md](../BlenderPlugin/README.md) | BlenderPlugin |
| [docs/BlenderPlugin/SIMBOLOS.md](../BlenderPlugin/SIMBOLOS.md) | Índice de símbolos del paquete Blender y núcleo (instantánea). |
| [docs/README.md](../README.md) | Documentación de OrtesisLab |
| [docs/Simplificacion/INVESTIGACION_LIBRERIAS.md](../Simplificacion/INVESTIGACION_LIBRERIAS.md) | Investigación: librerías que pueden asumir código propio |
| [docs/Simplificacion/PLAN_SIMPLIFICACION.md](../Simplificacion/PLAN_SIMPLIFICACION.md) | Plan de simplificación con librerías |
| [docs/Simplificacion/README.md](../Simplificacion/README.md) | Simplificación |
| [infra/database/backups/prueba.dump](../../infra/database/backups/prueba.dump) | Volcado de PostgreSQL en formato personalizado de `pg_dump` (cabecera `PGDMP`), del 2026-10-13; copia local de pruebas, no versionada. |
| [infra/database/backups/verificacion-2026-10-13.dump](../../infra/database/backups/verificacion-2026-10-13.dump) | Volcado de PostgreSQL en formato personalizado de `pg_dump` (cabecera `PGDMP`) de la verificación del 2026-10-13; copia local, no versionada. |
| [pyproject.toml](../../pyproject.toml) | Metadata Python, dependencias, build y comando de consola. |
| [scripts/AsegurarReactRouter.py](../../scripts/AsegurarReactRouter.py) | En Windows, react-router.exe ignora --conditions=development. |
| [scripts/BaseLocal.py](../../scripts/BaseLocal.py) | Infraestructura local: arranque, parada, estado, respaldo y reinicio de la base. |
| [scripts/EjecutarOrtesisLab.py](../../scripts/EjecutarOrtesisLab.py) | Script para abrir el complemento dentro de Blender. |
| [scripts/EjecutarTrabajador.py](../../scripts/EjecutarTrabajador.py) | Proceso trabajador de OrtesisLab: cola de generación y conciliación. |
| [scripts/EmpaquetarBlender.py](../../scripts/EmpaquetarBlender.py) | Genera el ZIP instalable de Blender, sin Reflex, logs ni la base v5. |
| [scripts/IniciarConsola.py](../../scripts/IniciarConsola.py) | Script del comando de consola del proyecto. |
| [scripts/MigrarSubidas.py](../../scripts/MigrarSubidas.py) | Traslada una sola vez ``uploaded_files/`` al bucket y registra cada objeto. |
| [skills-lock.json](../../skills-lock.json) | Procedencia y huellas de las tres skills Reflex instaladas. |
| [tests/README.md](../../tests/README.md) | Pruebas |
| [tests/aplicacion_web/__init__.py](../../tests/aplicacion_web/__init__.py) | Pruebas del generador web y del lector de superficies. |
| [tests/aplicacion_web/test_contrasena.py](../../tests/aplicacion_web/test_contrasena.py) | Hash de contraseña: la misma clave coincide y otra no. |
| [tests/aplicacion_web/test_estado_lote.py](../../tests/aplicacion_web/test_estado_lote.py) | La página /lote recibe todas las variantes con su estado, no solo las terminadas. |
| [tests/aplicacion_web/test_generador_web.py](../../tests/aplicacion_web/test_generador_web.py) | Comprueba el lote y el STL sin abrir Blender ni la superficie real. |
| [tests/aplicacion_web/test_humo_import.py](../../tests/aplicacion_web/test_humo_import.py) | Humo: la web y el trabajador deben importar sin ImportError. |
| [tests/assets/OrtesisTest1model.stl](../../tests/assets/OrtesisTest1model.stl) | Superficie STL de entrada para la prueba de carga del lector. |
| [tests/assets/blender_ejecucion.log](../../tests/assets/blender_ejecucion.log) | Log histórico de una ejecución del complemento en Blender. |
| [tests/assets/nucleo_ejecucion.log](../../tests/assets/nucleo_ejecucion.log) | Log histórico de las pruebas del núcleo geométrico. |
| [tests/assets/resultado_blender.json](../../tests/assets/resultado_blender.json) | Resultado histórico de una ejecución en Blender; no valida la versión actual. |
| [tests/assets/zip_ejecucion.log](../../tests/assets/zip_ejecucion.log) | Log histórico del empaquetado del complemento. |
| [tests/blender/__init__.py](../../tests/blender/__init__.py) | Scripts de integración que ejecuta Blender; unittest no los recoge. |
| [tests/blender/blender_paquete_zip.py](../../tests/blender/blender_paquete_zip.py) | Comprueba el paquete distribuido en aislamiento, sin assets ni Reflex. |
| [tests/blender/blender_superficie_abierta.py](../../tests/blender/blender_superficie_abierta.py) | Ejecutar con Blender --background --factory-startup --python-exit-code 1 --python este_archivo. |
| [tests/blender/test_instantanea_exportacion.py](../../tests/blender/test_instantanea_exportacion.py) | Contrato de instantánea evaluada para exportación Blender. |
| [tests/blender/test_rollback_publicacion.py](../../tests/blender/test_rollback_publicacion.py) | Rollback de generación y publicación atómica de archivos. |
| [tests/e2e/__init__.py](../../tests/e2e/__init__.py) | Pruebas de contrato extremo a extremo (pueden omitirse sin infraestructura). |
| [tests/e2e/test_carga_generacion_descarga.py](../../tests/e2e/test_carga_generacion_descarga.py) | Contrato de lectura anónima solo para STL. |
| [tests/e2e/test_dos_sesiones.py](../../tests/e2e/test_dos_sesiones.py) | Aislamiento de claves por usuario en el bucket. |
| [tests/geometria/__init__.py](../../tests/geometria/__init__.py) | Pruebas de escala, refinamiento, suavizado de borde y espesor. |
| [tests/geometria/test_carga_presupuesto.py](../../tests/geometria/test_carga_presupuesto.py) | Presupuestos de carga NPZ y validación de límites (A-01, A-03, A-11). |
| [tests/geometria/test_exportacion_validada.py](../../tests/geometria/test_exportacion_validada.py) | Validación numérica previa a STL web. |
| [tests/geometria/test_normales_topologia.py](../../tests/geometria/test_normales_topologia.py) | Regresiones A-04, A-05, A-06, A-14, A-16 y A-22 (fixtures sintéticas). |
| [tests/geometria/test_refinador_malla.py](../../tests/geometria/test_refinador_malla.py) | Refinamiento de patrones web sin depender de Blender. |
| [tests/geometria/test_suavizado_borde.py](../../tests/geometria/test_suavizado_borde.py) | El contorno exterior pierde los dientes y conserva la forma general. |
| [tests/geometria/test_superficie_abierta.py](../../tests/geometria/test_superficie_abierta.py) | Regresiones del espesor: pared cerrada, canal superior abierto. |
| [tests/nucleo/__init__.py](../../tests/nucleo/__init__.py) | Pruebas del núcleo geométrico: validación, catálogo, volumen y material. |
| [tests/nucleo/test_cache_metricas.py](../../tests/nucleo/test_cache_metricas.py) | Caché refinada y métricas del modelo. |
| [tests/nucleo/test_compatibilidad_npz_json.py](../../tests/nucleo/test_compatibilidad_npz_json.py) | Contratos compartidos de superficie y sidecar. |
| [tests/nucleo/test_nucleo.py](../../tests/nucleo/test_nucleo.py) | Comprueba que el núcleo repartido conserva la geometría del script original. |
| [tests/nucleo/test_wheel.py](../../tests/nucleo/test_wheel.py) | Comprueba el punto de entrada declarado en pyproject. |
| [tests/persistencia/__init__.py](../../tests/persistencia/__init__.py) | Pruebas de PostgreSQL, bucket, Redis, lotes, trabajador y permisos. |
| [tests/persistencia/apoyo_persistencia.py](../../tests/persistencia/apoyo_persistencia.py) | Apoyo de pruebas contra la base desechable ``ortesislab_test``. |
| [tests/persistencia/test_almacen_import.py](../../tests/persistencia/test_almacen_import.py) | Import al bucket, caché Redis y migración de subidas locales. |
| [tests/persistencia/test_cuota_almacen.py](../../tests/persistencia/test_cuota_almacen.py) | Cuotas de almacenamiento en importación (B-05). |
| [tests/persistencia/test_import_fallo_publicar.py](../../tests/persistencia/test_import_fallo_publicar.py) | Import rechazado si falla la publicación al bucket (B-06). |
| [tests/persistencia/test_lotes_trabajador.py](../../tests/persistencia/test_lotes_trabajador.py) | Lotes idempotentes, trabajador con lease, aislamiento y conciliación. |
| [tests/persistencia/test_propiedad_datos.py](../../tests/persistencia/test_propiedad_datos.py) | Propiedad de los datos y permisos de rol sobre PostgreSQL real. |
| [tests/persistencia/test_superficie_no_estatica.py](../../tests/persistencia/test_superficie_no_estatica.py) | A-02: el import no escribe en uploaded_files/ servido por Reflex. |
| [uv.lock](../../uv.lock) | Resoluciones reproducibles de dependencias Python. |

## Carpetas y artefactos locales

| Carpeta | Propósito y mantenimiento |
|---|---|
| `apps/web/` | Aplicación Reflex: paquete `web`, `rxconfig.py` y assets del visor |
| `apps/db/` | PostgreSQL, Redis, MinIO y Alembic |
| `apps/ortesis-plugin/` | Complemento de Blender (`OrtesisLabPlugin`) y su ZIP |
| `core/config/` | YAML del backend, JSON de geometría y README de cada archivo |
| `apps/web/web/persistence/`, `services/`, `storage/`, `cache/`, `jobs/` | Persistencia, servicios, bucket, caché Redis y trabajador |
| `scripts/` | Lanzadores, empaquetado, trabajador y migración de subidas |
| `tests/` | Pruebas Python, integraciones Blender, fixture y evidencia histórica |
| `apps/web/assets/` | Visor, favicon y superficie incluida; external/ ignorado contiene assets externos generados |
| `docs/` | README de carpetas, AppBackend, AppFrontend, BlenderPlugin, Agents y registros de audit |
| `docs/Agents/` | Mantenimiento con agentes, estándar, inventario, referencia Reflex y cambios |
| `.agents/skills/` | Instrucciones Reflex versionadas; no lógica de producto |
| `.codegraph/` | Índice local de navegación; no reindexar sin decisión del usuario |
| `.vscode/` | Preferencias de editor |
| `apps/web/reflex.lock/` | Dependencias frontend reproducibles |
| `.venv/` | Intérprete/dependencias Python instaladas; regenerar con uv |
| `__pycache__/` | Bytecode Python regenerable; nunca fuente |
| `.states/` | Artefactos de estado Reflex; no historial de dominio |
| `uploaded_files/` | Subidas de la arquitectura anterior; `scripts/MigrarSubidas.py` las traslada al bucket y las borra |
| `apps/ortesis-plugin/OrtesisLabPlugin/logs/` | Logs de ejecución del dominio |
| `dist/` | Copias/ensayos de distribución; incluye ZIP anteriores y extracciones temporales de pruebas; no fuente vigente |

## `.web/`: árbol generado

No se inventarían los miles de archivos transitivos de node_modules ni builds: pertenecen al compilador/dependencias, no a código desarrollado en este repositorio. Los directorios cambian con la versión instalada.

| Elemento | Función |
|---|---|
| `app/`, `app_components/`, `components/` | Rutas React Router y componentes compilados |
| `backend/`, `utils/` | Integración generada de eventos/estado/utilidades cliente |
| `public/`, `styles/` | Assets publicados y estilos compilados |
| `build/`, `.react-router/` | Salidas de build y metadata de rutas |
| `node_modules/` | Dependencias transitivas instaladas |
| `package.json`, `bun.lock`, `bunfig.toml`, `.npmrc` | Resolución y configuración del gestor JS |
| `vite.config.js`, `react-router.config.js`, `jsconfig.json` | Configuración del frontend generado |
| `tailwind.config.js`, `postcss.config.js` | Compilación CSS |
| `env.json`, `reflex.json` | Parámetros generados de entorno/framework; no publicar secretos |
| `compress-static.js`, `vite-plugin-safari-cachebust.js` | Utilidades de build generadas |
| `.memo-manifest.json`, `reflex.install_frontend_packages.cached`, `.reflex_dev_backend_started` | Cachés y marcadores del compilador/proceso |
| `.gitignore` | Exclusiones de la compilación |
