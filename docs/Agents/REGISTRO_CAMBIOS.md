# Registro de cambios documentales

## 2026-11-12 — Límites, imports colgados y purga del trabajador

`Configuracion.Limites` exigía dos claves de autoescala que `limites.json` ya no tiene, así que cualquier límite lanzaba `KeyError`. Esas claves salen de `LIMITES_POSITIVOS`. `RepositorioImports.ColgadosVencidos` cierra imports `received` o `validating` vencidos, e `ImportDTO` incluye `user_id` porque el conciliador lo usa. `ServicioVersiones.CLAVES_SOLO_VOXEL` es `repair` y `resolution_mm`. La revisión Alembic `b7c1d4e9a2f0` concede `DELETE` de `history_events` y `auth_sessions` solo a `ortesislab_worker`; la aplicación sigue sin borrar historial. `ValidarEnArranque` ya no se llama desde el merge del login. Autorización en [RES-2026-11-12-014](../Audit/resolves/2026-11-12-resolve-fase0-defectos.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `uv run python -m unittest tests.geometria.test_carga_presupuesto -v`: 5 pruebas, OK. `Limites()` carga `limites.json` sin las claves de escala.
- Importación de `ServicioVersiones.CLAVES_SOLO_VOXEL` y `RepositorioImports.ColgadosVencidos`: imprimió `simbolos-ok`.

No se aplicó `alembic upgrade head` ni se ejecutó la purga contra PostgreSQL. No se arrancó la web ni el trabajador.

## 2026-11-12 — Rediseño de la interfaz: parámetros, lotes y página de progreso

Pedido del usuario ([RES-2026-11-12-011](../Audit/resolves/2026-11-12-resolve-rediseno-interfaz-lotes.md)). La página `/` separa parámetros genéricos y avanzados (casilla «Mostrar parámetros avanzados»), muestra una ayuda por parámetro (`ayudas` en `core/config/web.yaml`) y agrupa las acciones en pestañas «Una ortesis» y «Lote de variantes». El lote se arma en tres pasos con un resumen en vivo (cantidad y minutos, o el motivo por el que no es válido) y, al generarlo, redirige a la nueva página `/lote` (`web/PaginaLote.py`): cabecera con avance, conteo por estado y Cancelar lote, comparación 3D y una tarjeta por variante con miniatura. `assets/visor.html` acepta `miniatura=1`: dibuja un fotograma, lo deja como imagen y libera el contexto WebGL. `EstadoApp._Publicar` publica también las variantes en cola o en curso con su `estado`; los valores por defecto se aplican una sola vez por pestaña (botón Restaurar); Restaurar/Reintentar del historial redirigen a `/lote`.

Documentación: AppFrontend README, ARQUITECTURA, COMPONENTES_Y_FLUJOS, VISOR_3D y OPERACION_Y_PRUEBAS; AppBackend OPERACION_Y_PRUEBAS; `core/config/README.md`.

Pruebas ejecutadas:
- `.venv/Scripts/python.exe -m unittest tests.aplicacion_web.test_estado_lote -v`: 2 OK (nueva: `_Publicar` con variantes en cola, en curso y fallidas).
- `.venv/Scripts/python.exe -m unittest tests.aplicacion_web.test_generador_web tests.aplicacion_web.test_humo_import`: 14 pruebas, 3 errores en `LectorSuperficie.Preparar` que también aparecen sin estos cambios (comprobado con `git stash`).
- `reflex compile --dry` en `apps/web`: compiló sin errores.
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`.

No se arrancó Reflex en el navegador ni se probó el flujo con PostgreSQL, trabajador y bucket; tampoco el render real de las miniaturas.

## 2026-11-12 — El acceso es usuario y contraseña

Se quita el proveedor OIDC, el callback y el alta por emisor y sujeto. `/auth/registro` y `/auth/login` guardan `username` y el hash scrypt de la contraseña en `app_users`, y abren la misma cookie `ortesislab_sesion`. La revisión Alembic `0ea8eb9c0ca2` crea el esquema vacío, concede a la aplicación y al trabajador los permisos de [DATABASE.md](../AppBackend/DATABASE.md) y deja el trigger que exige un import `ready` al crear una versión. `make web` seguía fallando el `postinstall` del frontend porque la ruta del ajuste de React Router se resolvía desde `apps/web/.web`; queda en `../../../scripts/AsegurarReactRouter.py`. Autorización en [RES-2026-11-12-012](../Audit/resolves/2026-11-12-resolve-login-local.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `uv run python -m unittest tests.aplicacion_web.test_contrasena tests.aplicacion_web.test_humo_import`: 4 pruebas, OK.
- `uv run alembic upgrade head`: aplicó `0ea8eb9c0ca2`.
- Alta, entrada, clave incorrecta y usuario repetido contra PostgreSQL de desarrollo, y borrado de esa cuenta: imprimió `login-ok`.

No se recorrió el formulario en el navegador: `make web` seguía reiniciando el worker por el `postinstall` con la ruta anterior.

## 2026-11-12 — El frontend de Windows no se reinicia dos veces

`make web` ejecuta `scripts/AsegurarReactRouter.py` antes de Reflex. En Windows, `bun install` regenera `react-router.exe` y ese binario no aplica `--conditions=development`, así que el servidor de desarrollo se relanza y choca con su propio seguro. `bin.cjs` vuelve a arrancar con el bun de Reflex y esa condición. `reflex.lock/package.json` repite el ajuste en `postinstall` por si el paquete se reinstala durante la compilación. Los hallazgos siguen abiertos.

## 2026-11-12 — El arranque ya no llama a `ValidarEnArranque`

`PoolPostgres` llamaba `ConfiguracionBackend.ValidarEnArranque`, que no existe: `Cargar` solo lee el YAML. El ciclo de vida abre PostgreSQL y, si no responde, deja el mensaje de persistencia no disponible. Los hallazgos siguen abiertos.

## 2026-11-12 — El módulo Reflex es `web.OrtesisLabApp`

`rxconfig.py` declara `app_name="OrtesisLabApp"` y `app_module_import="web.OrtesisLabApp"`. El archivo seguía en `apps/web/web/GenerateModelsApp.py`, así que Reflex no encontraba el módulo. Pasa a `OrtesisLabApp.py`. El complemento sigue siendo `OrtesisLabPlugin` y el ZIP conserva el nombre `GenerateModelsApp.zip`. Autorización en [RES-2026-11-12-010](../Audit/resolves/2026-11-12-resolve-modulo-ortesislabapp.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `uv run --directory apps/web python -c "import rxconfig; import web.OrtesisLabApp"`: terminó en 0 e imprimió `import-ok`.
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`: catálogos al día y enlaces correctos.

No se arrancó Reflex en el navegador.

## 2026-11-12 — Sin carpeta `src`

Se elimina `src/generatemodelsapp/`. Solo añadía el complemento a `sys.path` y llamaba `OrtesisLabPlugin.consola.main`. El saludo sigue en `consola.py` y se lanza con `scripts/IniciarConsola.py`. Desaparece el script `generatemodelsapp` de `pyproject.toml`. `tool.uv.package` queda en `false`: el repositorio no instala un paquete propio y `uv run` sigue trayendo las dependencias. Autorización en [RES-2026-11-12-009](../Audit/resolves/2026-11-12-resolve-quitar-src.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `uv run python -c "print('uv-ok')"`: terminó en 0.
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`: catálogos al día y enlaces correctos.

No se ejecutó unittest ni Reflex.

## 2026-11-12 — El núcleo se importa como `OrtesisLabPlugin`

La carpeta del complemento ya era `apps/ortesis-plugin/OrtesisLabPlugin`. La web, las pruebas, los lanzadores y `pyproject.toml` seguían importando `GenerateModelsApp`, y `rxconfig.py` metía en `sys.path` la ruta `apps/apps/ortesis-plugin`. Los imports pasan a `OrtesisLabPlugin`. `rxconfig.py` añade `apps/ortesis-plugin`, que es el padre real del paquete. El ZIP sigue llamándose `GenerateModelsApp.zip`; el directorio raíz de dentro pasa a `OrtesisLabPlugin`, igual que el módulo que carga Blender. `web/GenerateModelsApp.py` no cambia de nombre: es el módulo Reflex. Autorización en [RES-2026-11-12-008](../Audit/resolves/2026-11-12-resolve-paquete-ortesislabplugin.md). Los hallazgos siguen abiertos.

Documentación: README, `core/config/README.md`, AppBackend MODULOS y OPERACION_Y_PRUEBAS, BlenderPlugin ARQUITECTURA, API_Y_DATOS, LEEME, MODULOS y OPERACION_Y_PRUEBAS, Agents MANTENIMIENTO e INVENTARIO (tabla de carpetas).

Pruebas ejecutadas:
- `uv run --directory apps/web python -c "import rxconfig; import web.GenerateModelsApp"`: terminó en 0 e imprimió `import-ok`.
- `uv run python -m unittest discover -s tests -p "test_wheel.py"`: 2 pruebas, OK.
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`: catálogos al día y enlaces correctos. Se completaron las descripciones pendientes de `apps/web/.gitignore` y `apps/web/requirements.txt`.

No se arrancó `make web` hasta el navegador, ni Blender, ni el empaquetado del ZIP.

## 2026-11-12 — La revisión de Alembic no la había emitido Alembic

Se elimina `apps/db/alembic/versions/20261112_1200_esquema_inicial.py`. No coincide con `apps/db/alembic/script.py.mako`: no tiene `Revision ID`, `Revises` ni `Create Date`, ni `import sqlalchemy as sa`. `upgrade` crea las tablas con `Base.metadata.create_all`, no con los `op.create_table` de `alembic revision --autogenerate`. El humo `tests/persistencia/test_alembic_revision.py` solo importaba ese archivo y también se elimina. `versions/` queda con `.gitkeep`. `make migrar` sigue siendo `alembic upgrade head` y, sin revisiones, no crea tablas. La autorización está en [RES-2026-11-12-007](../Audit/resolves/2026-11-12-resolve-revision-alembic.md). El cierre histórico de B-02 no se reescribe. Los hallazgos siguen abiertos.

No se ejecutó `alembic revision` ni `alembic upgrade`: no hay `.env` ni base en esta sesión, y una revisión nueva tiene que salir de Alembic.

## 2026-11-12 — Objetivos de Make

El `Makefile` instala el entorno, levanta la web y el trabajador, ejecuta unittest y ruff, y empaqueta el complemento. La infraestructura local queda en cinco objetivos (`db-up`, `db-down`, `db-estado`, `db-respaldo`, `db-reset`); el comportamiento está en `scripts/BaseLocal.py`. `db-up` arranca PostgreSQL, MinIO, Redis, el bucket y el OIDC de pruebas. `db-respaldo` copia y restaura metadatos y objetos juntos. `db-reset` sigue recreando `ortesislab_dev` vacía. La autorización está en [RES-2026-11-12-006](../Audit/resolves/2026-11-12-resolve-makefile.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `python scripts/BaseLocal.py --comprobar`.
- `python scripts/BaseLocal.py up` sin `apps/db/.env`: termina avisando que falta el archivo.
- `python scripts/BaseLocal.py respaldo` sin `FILE`: pide `FILE=nombre.dump`.
- `make help` dentro de `alpine:3.20`: la primera pasada falló porque un `;` del texto de ayuda lo partía el shell. Con las líneas entre comillas, la siguiente pasada terminó en 0.

No están `make`, `uv` ni `ruff` en el PATH del host. No se arrancó Docker Compose ni Reflex. No se ejecutó unittest.

## 2026-11-12 — README de core/config

`core/config/README.md` explica para qué sirve cada YAML del backend y cada JSON de geometría. [OPERACION_Y_PRUEBAS.md](../AppBackend/OPERACION_Y_PRUEBAS.md) enlaza ese archivo. El catálogo de claves deja de citar `maximo_variantes`: el tope de variantes es `lotes.maximo_items`. Los enlaces de BlenderPlugin que apuntaban a `apps/ortesis-plugin/GenerateModelsApp/` pasan a `OrtesisLabPlugin/`, que es la carpeta que está en disco.

Pruebas ejecutadas: `py -3 docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`. Catálogos al día y enlaces correctos.

## 2026-11-12 — Sin fixture ni base de pruebas

Se eliminan `apps/db/seeds/development.sql`, `make db-seed` y `make db-test-reset`. El repositorio ya no crea `ortesislab_test` ni carga un usuario demo. Los datos de desarrollo salen del uso de la aplicación. `make db-reset` sigue recreando `ortesislab_dev` vacía y reaplicando esquema y permisos con `apps/db/preparar_base.sql`. La autorización está en [RES-2026-11-12-005](../Audit/resolves/2026-11-12-resolve-quitar-seeds-test.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `py -3 docs/Agents/Scripts/GenerarIndices.py --comprobar`.

No se ejecutó `make` ni PostgreSQL.

## 2026-11-12 — Un commit con el monorepo y lo que traía master

Los dos commits de `origin/master` quedan dentro del árbol del monorepo. Si tocaban lo mismo que la refactorización, se conserva esta: no vuelve `EscalaMalla` ni el parámetro `autoescalar`, y las rutas siguen en `apps/` y `core/`. Sí entran la revisión inicial de Alembic en `apps/db/alembic/versions/`, el flujo de cuotas de importación, los módulos nuevos del complemento, el visor con Three.js en `apps/web/assets/vendor/` y el workflow de pruebas, con `preparar_base.sql` en `apps/db/test/`.

Pruebas ejecutadas:
- `py -3 docs/Agents/Scripts/GenerarIndices.py --comprobar`.

No se ejecutó `uv sync`, Reflex, PostgreSQL ni `alembic upgrade`.

## 2026-11-12 — Las coordenadas de entrada no se autoescalan

Se elimina la corrección decimal de unidades. Web, núcleo y complemento usan las coordenadas del archivo. Desaparecen la casilla, `EscalaMalla`, el aviso y los límites `min_plausible_surface_extent_mm` y `max_plausible_surface_extent_mm`. Arreglar sigue horneando la escala del objeto de Blender. Las columnas `user_preferences.auto_scale` y `model_versions.auto_scale` permanecen: una preferencia nueva y cada versión nueva se insertan con `false`, y la generación no las lee. El hash de versión y el de la solicitud ya no incluyen esa bandera. Autorización en [RES-2026-11-12-004](../Audit/resolves/2026-11-12-resolve-quitar-autoescala.md). Documentación: BlenderPlugin ALGORITMOS, MODULOS, ARQUITECTURA, API_Y_DATOS, PARAMETROS, LEEME y OPERACION_Y_PRUEBAS; AppBackend ARQUITECTURA, MODULOS, CONTRATOS, DATABASE y OPERACION_Y_PRUEBAS; AppFrontend ARQUITECTURA; `tests/README.md`.

Pruebas ejecutadas:
- `py -3` analizó la sintaxis de los `.py` de `apps`, `tests` y `scripts`: sin errores.
- `py -3 docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`: catálogos al día y enlaces correctos.
- `py -3 scripts/EmpaquetarBlender.py`: el ZIP ya no contiene `EscalaMalla.py` ni las claves de rango plausible.

No hay `.venv` ni NumPy en el Python de esta sesión, así que no se ejecutó unittest. No se abrió Blender ni el navegador. No se aplicó una migración: las columnas `auto_scale` siguen en el esquema.

## 2026-11-12 — El `.env` de la raíz lo lee python-dotenv

`Ajustes.Cargar()` deja de parsear el archivo. La ruta ya es fija (`RAIZ / ".env"`, la raíz del monorepo). `load_dotenv` vuelca ese archivo al entorno del proceso sin pisar variables ya definidas, y `Cargar` guarda una copia. Siguen el UTF-8 con o sin BOM y la prioridad del entorno del proceso. Las referencias `$` del archivo ahora se sustituyen. Autorización en [RES-2026-11-12-003](../Audit/resolves/2026-11-12-resolve-dotenv-raiz.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- python-dotenv 1.2.4 en un directorio temporal: con BOM, la variable del proceso gana, una clave nueva entra, `${NUEVA}` se sustituye y el BOM no forma parte del nombre.
- No había `.env` en la raíz. Se creó uno de prueba, `Cargar()` leyó la clave del archivo y conservó la del proceso, y se borró el archivo.
- `py -3 docs/Agents/Scripts/GenerarIndices.py`. Una comprobación posterior volvió a marcar `docs/AppBackend/SIMBOLOS.md`: cambiaron las líneas de otros módulos mientras se medía. La ficha de `Ajustes` ya no incluye `_LeerArchivo`.

No hay `.venv` ni `uv` en esta sesión. No se arrancó Reflex, el trabajador ni PostgreSQL.

## 2026-11-12 — `Cargar` lee el YAML con `Path.read_text`

`ConfiguracionBackend.Cargar` sigue devolviendo el `dict` de `yaml.safe_load` sobre `core/config/<area>.yaml`, con la misma caché por proceso. Desaparece el `with`/`open`: `Path.read_text` ya entrega ese texto. No cambia la firma, los llamadores ni el contrato. El archivo sigue auditado; la autorización está en [RES-2026-11-12-002](../Audit/resolves/2026-11-12-resolve-simplificar-carga-yaml.md) y B-09 queda abierto.

Pruebas ejecutadas:
- `read_text` y `open` devolvieron el mismo texto en los seis YAML de `core/config/`. Un nombre ausente lanza `FileNotFoundError`.

No se importó `Cargar`: en esta máquina no hay `.venv`, `uv` ni PyYAML para Python 3.15. No se regeneraron los índices: la línea del método no cambia y el contrato tampoco.

## 2026-11-12 — Monorepo `apps` y `core`

La web Reflex queda en `apps/web/` (el paquete Python sigue llamándose `web`). PostgreSQL, Redis y el Compose que ya incluía MinIO y el OIDC de pruebas quedan en `apps/db/`, junto con Alembic y el seed. El complemento queda entero en `apps/ortesis-plugin/GenerateModelsApp/`: Blender lo instala como una carpeta y la web importa ese mismo núcleo. Los YAML del backend y los JSON de geometría pasan a `core/config/`; el empaquetado copia los JSON dentro del ZIP. La autorización de mover archivos auditados está en [RES-2026-11-12-001](../Audit/resolves/2026-11-12-resolve-monorepo.md). Los hallazgos siguen abiertos.

Pruebas ejecutadas:
- `py -3 docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`.

No se ejecutó `uv lock` ni `uv sync`: `uv` no está en el PATH de esta sesión. No se arrancó Reflex ni PostgreSQL. `uv.lock` no cambia.

## 2026-11-12 — La clave ausente se avisa dentro de `Variable.__get__`

`VariableFaltante`, `VariableInvalida` y `Ajustes.Faltante` salen de `apps/web/web/Ajustes.py`. Leer una variable obligatoria ausente o vacía lanza `RuntimeError` con «Falta la variable de entorno …»; un prefijo incorrecto lanza `RuntimeError` con el prefijo exigido. `cookie_secure` sigue convirtiendo `ORTESISLAB_COOKIE_SECURE` en bool. Las pruebas de persistencia capturan solo el mensaje de clave ausente para omitirse. Documentación: AppBackend MODULOS, OPERACION_Y_PRUEBAS y ARQUITECTURA. Autorización: [RES-2026-11-12-003](../Audit/resolves/2026-11-12-resolve-ajustes-entorno.md).

Pruebas ejecutadas:
- Script sobre `Ajustes({})`: clave ausente y URL ausente lanzan `RuntimeError` con «Falta la variable de entorno …»; una URL `postgresql://` lanza el mensaje del prefijo; el defecto de bucket, Redis vacío, `app_url` y `cookie_secure` (`TRUE` y ausente) salen como se declaran. No se imprimieron valores reales.
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`.

No se ejecutaron las pruebas de persistencia contra PostgreSQL ni el arranque de la web.

## 2026-11-12 — Base de datos: quitar el diseño obsoleto y dos métodos sin uso

`docs/AppBackend/DATABASE.md` deja de conservar la propuesta de dbmate, el catálogo de objetivos que el Makefile no tiene y el plan de una implementación ya hecha. Conserva la arquitectura y el modelo entidad-relación, alineados con el código: repositorios SQLAlchemy, Alembic, bucket S3, Redis prescindible, `auth_sessions` y `file_assets.object_url`. El grafo muestra solo las relaciones; las columnas van en tablas Markdown, porque las cajas de Mermaid con todos los atributos no cabían en la vista. También quedan los roles y el SQL que Alembic no genera. `OPERACION_Y_PRUEBAS.md` sustituye el recetario de PowerShell por `make db-reset CONFIRM=ELIMINAR`, que recrea `ortesislab_dev` vacía igual que `db-test-reset` recrea la base de pruebas. Se eliminan `RepositorioImports.NombreOriginal` y `RepositorioProyectos.Listar`, que no tenían llamadores; `RepositorioProyectos` deja de heredar `RepositorioBase`.

El generador de índices señaló seis archivos sin descripción previa (workflow de Notion, dos JSON de la auditoría del 2026-10-29 y tres logs de `tests/assets/`); se completaron en `INVENTARIO.md`.

Pruebas ejecutadas:
- `python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`.

GNU Make no está en el PATH de esta sesión, así que `db-reset` no se ejecutó. No se ejecutaron pruebas contra PostgreSQL ni el recorrido en navegador: no cambia el esquema ni un flujo de pantalla.

## 2026-10-13 — Estados y tipos como `StrEnum` en `web/enums/`

Los valores cerrados del dominio (estados de usuario, asset, import, lote, ítem, intento y export; tipos de asset y de evento; formatos, modos, unidades, alcance y extensiones de superficie) pasan a `StrEnum` en `web/enums/`, agrupados por dominio. `Modelos.py` construye desde ellos los `CHECK ... IN`, los `server_default` y los índices parciales por estado; desaparece `TIPOS_EVENTO`. `Contratos.ALCANCE_GEOMETRIA` se sustituye por `AlcanceGeometria.PRE_VOXEL_SHELL` y `ServicioHistorial.ESTADOS` por `EstadoItem`. Repositorios, servicios, jobs, `scripts/MigrarSubidas.py` y `EstadoHistorial` usan los miembros en lugar de literales. Las etiquetas de estado de `/historial` (`ESTADOS_VISIBLES`) pasan a `config/web.yaml`, clave `estados_visibles`.

En los archivos auditados solo cambian `EstadoApp.TERMINALES` y `LectorSuperficie.EXTENSIONES`, con autorización explícita registrada en [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md); `GeneradorWeb.py`, `PaginaComparacion.py` y el resto de `EstadoApp.py` conservan sus literales. Las claves de `payload` y de contadores que coinciden con un estado (`"succeeded"` en `batch_finished`, `"staged"` en el conciliador) no son valores de columna y se mantienen. Documentación: AppBackend MODULOS y OPERACION_Y_PRUEBAS.

Pruebas ejecutadas:
- DDL PostgreSQL de las 13 tablas e índices (31 sentencias) compilado desde `Modelos.py` antes y después: idéntico.
- Repositorios antes y después con sesión falsa: 132 ejecuciones, mismo SQL, parámetros (comparando cada enum por su valor) y resultados.
- psycopg y SQLAlchemy envían un `StrEnum` por su valor; el JSON canónico del hash de versión es el mismo.
- `TERMINALES`, `EXTENSIONES` y `ESTADOS_VISIBLES` conservan valores y orden; el filtro de estado de historial acepta y rechaza los mismos valores; `NombreSuperficie`/`AssetDeNombre` siguen siendo inversas.
- unittest: 73 pruebas, 50 aprobadas y 23 omitidas.
- Firmas AST: 69 sin cambios.
- `import web.GenerateModelsApp` sin error.

No se ejecutaron pruebas contra PostgreSQL.

## 2026-10-13 — Patrones y ejes en `config/web.yaml`

Los diccionarios `PATRONES` (patrón de relleno → etiqueta) y `EJES` (parámetro variable → etiqueta) pasan de `web/GeneradorWeb.py` a las claves `patrones` y `ejes` de `config/web.yaml`. `GeneradorWeb` los sigue exportando con el mismo nombre, por lo que `EstadoApp`, `EstadoHistorial`, `PaginaComparacion` y `PaginaHistorial` no cambian. El archivo auditado se edita con autorización explícita del usuario, registrada en [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md). Documentación: AppBackend MODULOS y OPERACION_Y_PRUEBAS.

Pruebas ejecutadas:
- Comparación de `PATRONES` y `EJES` con una copia tomada antes del cambio: mismas claves, etiquetas y orden.
- unittest: 73 pruebas, 50 aprobadas y 23 omitidas.
- Firmas AST: 69 sin cambios.
- `import web.GenerateModelsApp` sin error.

## 2026-10-13 — Comprobación de variables faltantes en `Ajustes`

`Ajustes.Faltante(*atributos)` devuelve el mensaje de la primera variable obligatoria sin definir, o una cadena vacía. `tests/persistencia/apoyo_persistencia.py` ya no captura `VariableFaltante`: pregunta a `Ajustes` por las dos URL de prueba y, si falta alguna, omite las pruebas con ese mensaje. Documentación: AppBackend MODULOS.

Pruebas ejecutadas:
- Script temporal sobre `Faltante`: sin variables, con una URL y con ambas. Devuelve el mensaje de la que falta o una cadena vacía. No se imprimieron valores reales.
- unittest: 73 pruebas, 50 aprobadas y 23 omitidas.
- Firmas AST: 69 sin cambios.

## 2026-10-13 — Repositorios en un paquete

`web/persistence/Repositorios.py` se divide en el paquete `web/persistence/repositorios/`, con un archivo por repositorio. `RepositorioBase` agrupa lo que se repetía: leer una fila o todas, construir el DTO, la consulta opcional y la consulta filtrada por dueño con `AccesoDenegado`. `Consultas.py` reúne los alias de tablas y los fragmentos compartidos. Las firmas públicas, el SQL y los DTO no cambian. Los once módulos que importaban `web.persistence.Repositorios` pasan a `web.persistence.repositorios`. En el archivo auditado `web/GeneradorWeb.py` solo cambia esa línea de importación, con la autorización registrada en [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md).

Documentos actualizados: AppBackend MODULOS y DATABASE (fila de acceso a datos).

Pruebas ejecutadas:
- Comparación entre el módulo previo y el paquete nuevo con una sesión falsa: 61 métodos públicos y 122 ejecuciones. El SQL compilado para PostgreSQL, los parámetros y las firmas coinciden. Las seis diferencias de resultado de `RepositorioAssets` se deben a columnas extra en la fila falsa. Se verificó que `COLUMNAS` coincide con `Asset`.
- unittest: 73 pruebas, 50 aprobadas y 23 omitidas.
- Firmas AST: 69 sin cambios.
- `import web.GenerateModelsApp` sin error.

Los repositorios no se probaron contra PostgreSQL.

## 2026-10-13 — Valores ajustables del backend en `config/*.yaml`

Los límites, tiempos y tamaños del backend salen del código y pasan a seis archivos YAML en `config/`: `persistencia`, `trabajador`, `cache`, `almacen`, `sesion` y `web`. Los lee `web/ConfiguracionBackend.py` (`ConfiguracionBackend.Cargar(area)`, `yaml.safe_load` en caché). Las constantes conservan sus nombres en cada módulo, así que los demás módulos y las pruebas no cambian. Los valores son los mismos.

También pasan a YAML valores que estaban escritos como literales:
- el timeout de conexión y la pausa entre reintentos de PostgreSQL;
- los timeouts de Redis y de S3, y los intentos de S3;
- la vigencia de la cookie del intercambio OIDC.

Quedan en código las constantes de contrato: versiones, estados, prefijos de claves, nombre de cookie y esquema. La configuración JSON del complemento Blender no cambia. Se añade `pyyaml` como dependencia directa.

Los archivos auditados `web/EstadoApp.py`, `web/GeneradorWeb.py` y `web/LectorSuperficie.py` se editan con autorización explícita del usuario, registrada en [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md).

Documentos actualizados: AppBackend OPERACION_Y_PRUEBAS (catálogo de claves y relaciones entre ellas), ARQUITECTURA y MODULOS.

Pruebas ejecutadas:
- unittest: 73 pruebas, 50 aprobadas y 23 omitidas.
- Firmas AST: 69 sin cambios.
- Comparación de las 24 constantes leídas de YAML con sus valores anteriores: iguales.
- `import web.GenerateModelsApp` sin error.

No se ejecutaron Reflex ni el trabajador.

## 2026-10-13 — URL de PostgreSQL sin conversión

Se elimina `ConexionPostgres.UrlSqlAlchemy`. Las seis URL de base de datos deben venir del entorno como `postgresql+psycopg://`. `Variable` acepta un `prefijo`, y si el valor no empieza por él, `Ajustes` lanza `VariableInvalida`. `ConexionPostgres.Abrir`, `db/alembic/env.py` y `apoyo_persistencia.py` usan la URL tal como la entrega `Ajustes`. Las URL de `.env.example` y del `.env` local se reescriben al nuevo prefijo. Documentación: AppBackend OPERACION_Y_PRUEBAS (formato y diagnóstico) y MODULOS.

Pruebas ejecutadas: unittest, firmas AST, comprobación de `Ajustes` con URL válidas e inválidas y `GenerarIndices.py --comprobar`.

## 2026-10-13 — `db/alembic/env.py` con un solo flujo

Las funciones `EjecutarOffline` y `EjecutarOnline` se sustituyen por `Ejecutar`. Ese único flujo abre siempre una conexión con el rol migrador, fija `search_path` y ejecuta las migraciones. Desaparece el modo `--sql` de Alembic. `AppBackend/OPERACION_Y_PRUEBAS.md` retira esa fila de la tabla de comandos e indica la limitación; `DATABASE.md` §12 la menciona.

Pruebas ejecutadas: compilación del archivo con `py_compile`, unittest y `GenerarIndices.py --comprobar`. No se ejecutó Alembic, por instrucción del usuario.

## 2026-10-13 — Variables de entorno centralizadas en `Ajustes`

`web/Ajustes.py` es ahora el único archivo que declara y lee variables `ORTESISLAB_*`.

Cómo funciona:
- Cada clave es un atributo `Variable(clave, defecto)`. Las que no tienen defecto son obligatorias: leerlas ausentes o vacías lanza `VariableFaltante`.
- `Cargar()` combina el `.env` raíz con el entorno real, que tiene prioridad, sin modificar `os.environ`.
- Se añaden las URL del migrador y de las bases de prueba.
- Se elimina `ORTESISLAB_STORAGE_SCHEME`, que nada leía.

Comprobaciones propias retiradas:
- `db/alembic/env.py` deja de leer `.env` y `os.environ`.
- `apoyo_persistencia.py` toma las URL de prueba de `Ajustes` y omite las pruebas con el mensaje de `VariableFaltante`.
- Se eliminan las comprobaciones «Falta …» de `EjecutarTrabajador.py`, `ConexionPostgres.Abrir` y `StorageS3`.
- Se elimina el modo 503 de `AutenticacionOidc`. Sin OIDC la web no arranca.

Además, el trabajador crea el almacén S3 al arrancar. `tests/blender/blender_paquete_zip.py` sigue leyendo `ORTESISLAB_ZIP` con `os.environ` porque se ejecuta dentro de Blender y es un archivo auditado sin autorización para este cambio.

Documentos actualizados: AppBackend OPERACION_Y_PRUEBAS (tabla de variables y diagnóstico), MODULOS, ARQUITECTURA, DATABASE; `.env.example`.

Pruebas ejecutadas:
- `.venv\Scripts\python.exe -B -m unittest discover -s tests`: 73 pruebas, 50 aprobadas y 23 omitidas por no poder conectar con la base de pruebas.
- Firmas AST: 69 sin cambios.
- Script temporal sobre `Ajustes`: las variables obligatorias ausentes o vacías lanzan `VariableFaltante`, se aplican los defectos y el `.env` local define las URL de base, migrador, pruebas y OIDC. No se imprimieron valores.

No se ejecutaron Reflex, el trabajador ni Alembic.

## 2026-10-13 — Persistencia con SQLAlchemy 2.0 y Alembic

El acceso a PostgreSQL pasa de SQL con Psycopg a SQLAlchemy 2.0 sobre psycopg 3:
- `web/persistence/Modelos.py` declara las 13 tablas.
- `ConexionPostgres` abre un motor y entrega una `Session`, con la misma API (`Abrir`, `Transaccion`, `Ejecutar`, `Cerrar`).
- `Repositorios.py` reescribe cada consulta como sentencia SQLAlchemy, con las mismas firmas y DTO.
- Se eliminan `web/persistence/sql/` y `Consulta`.

En el resto del repositorio:
- Las pruebas de persistencia usan `Session` y `ErrorDeBase`.
- El Makefile y el Compose dejan dbmate y los objetivos de migración; `db-test-reset` solo crea la base vacía con `db/test/preparar_base.sql`, que recibe `base`.
- Alembic queda configurado (`alembic.ini`, `db/alembic/env.py`, rol migrador en `.env.example`).

Por instrucción del usuario, las migraciones las hace él. Se eliminaron las migraciones dbmate, `db/schema.sql`, la revisión Alembic generada y las bases previas, y `db/alembic/versions/` queda sin revisiones. La documentación explica cómo inicializar una base y cómo crear, aplicar y revertir migraciones (`AppBackend/OPERACION_Y_PRUEBAS.md`). Explica también qué debe añadirse a mano a la revisión porque Alembic no lo genera: la FK circular, el trigger de versiones y los `GRANT` (`AppBackend/DATABASE.md` §12). Los archivos auditados editados (`pyproject.toml`, `uv.lock`, `README.md`) constan en [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md).

Documentos actualizados: AppBackend (DATABASE, OPERACION_Y_PRUEBAS, ARQUITECTURA con diagrama de capas de persistencia, MODULOS, README), README raíz y `tests/README.md`.

Pruebas ejecutadas sobre la versión actual:
- `.venv\Scripts\python.exe -B -m unittest discover -s tests`: 73 pruebas, 50 aprobadas y 23 omitidas. Las 23 de persistencia se omiten porque no existe una base `ortesislab_test` migrada.
- Comparación AST de firmas: 69 sin cambios.
- Compilación de las sentencias de los 59 métodos de repositorio con sesiones simuladas, para el dialecto PostgreSQL.

Antes de la instrucción del usuario se ejecutaron `alembic upgrade head`, `alembic check` y una comparación de `pg_dump` con el esquema dbmate sobre bases que después se eliminaron. Esas ejecuciones no validan la versión actual. Los repositorios no se han probado contra PostgreSQL con SQLAlchemy y el recorrido en navegador no se repitió.

## 2026-10-13 — Orden de las pruebas por área

Las pruebas dejan de estar sueltas en `tests/` y quedan agrupadas por el código que cubren: `nucleo`, `geometria`, `aplicacion_web`, `persistencia` y `blender`. El mapa está en `tests/README.md`. Los fixtures y la evidencia histórica pasan a `tests/assets/`. El visor, el icono y la superficie incluida siguen en la raíz de `assets/`, con `assets/README.md`, porque Reflex y el núcleo los buscan ahí.

El traslado está autorizado en [RES-2026-10-13-002](../Audit/resolves/2026-10-13-resolve-organizar-pruebas.md). No cierra hallazgos de `AUD-2026-10-13-001`. En los archivos auditados solo cambian la profundidad de `parents` y las rutas del fixture, del JSON de Blender y del comando documentado.

Pruebas ejecutadas: `.venv\Scripts\python.exe -B -m unittest discover -s tests` — 73 aprobadas, ninguna omitida, contra PostgreSQL 17 en Docker. No se ejecutaron las integraciones de Blender.

Al regenerar el inventario, el árbol ya no tenía `db/migrations/` ni `db/schema.sql` y sí tenía Alembic (`alembic.ini`, `db/alembic/`, `web/persistence/Modelos.py`). El catálogo y la fila de módulos apuntan a esos archivos presentes. No forma parte del orden de las pruebas.

## 2026-10-13 — Persistencia PostgreSQL, bucket S3, Redis y `/historial`

Base de código: `64bb48e` más cambios locales. Se implementa `AppBackend/DATABASE.md` con desviaciones documentadas en ese archivo: bucket S3 (MinIO en Compose) en lugar de almacenamiento local, `object_url` en `file_assets`, lectura anónima solo de STL, Redis como caché por contenido, retención de 30 días para imports rechazados y servidor de producción en un único puerto.

Fuentes y contratos afectados: infraestructura (`infra/database/`, `db/`, `Makefile`, `.env.example`), `web/persistence/`, `web/services/`, `web/storage/`, `web/cache/`, `web/jobs/`, `web/Ajustes.py`, `web/Sesion.py`, `web/EstadoHistorial.py`, `web/PaginaHistorial.py`, `scripts/EjecutarTrabajador.py`, `scripts/MigrarSubidas.py` y archivos auditados editados con firmas intactas según [RES-2026-10-13-001](../Audit/resolves/2026-10-13-resolve-persistencia-postgres.md). Se eliminan cachés de clase de `GeneradorWeb`, escritura en `uploaded_files/` y la generación dentro del proceso Reflex.

Documentos actualizados: AppBackend (ARQUITECTURA con diagramas de componentes y secuencia de la cola, MODULOS, CONTRATOS, OPERACION_Y_PRUEBAS, README, DATABASE) y AppFrontend (ARQUITECTURA con árbol y UML de `/historial` y sesión, COMPONENTES_Y_FLUJOS, VISOR_3D, OPERACION_Y_PRUEBAS, README), y README raíz.

Pruebas y validaciones ejecutadas:
- `.venv\Scripts\python.exe -B -m unittest discover -s tests`: 73 aprobadas, ninguna omitida, contra PostgreSQL 17 en Docker.
- Comparación AST de firmas: 69 sin cambios.
- `make db-backup` y restauración del volcado en una base desechable: 4 filas en `model_versions`.
- Navegador con Reflex `--env prod`, PostgreSQL, Redis y OIDC de pruebas en Docker y `moto_server` en lugar de MinIO: rechazo sin sesión, login con cookie HttpOnly, previsualización y visor, recuperación tras recarga, descarga con evento, lote de 2 con comparación, `/historial` con filtro, comparación y restauración, cierre de sesión y aislamiento de un segundo usuario.
- `scripts/MigrarSubidas.py --simular`: 32 archivos listados.

No ejecutado: MinIO real, `make db-init-s3`, `make s3-backup`, la migración real de `uploaded_files/`, proveedor OIDC distinto del de pruebas, vista móvil, integración Blender.

Retirada del verificador documental: `scripts/VerificarDocumentacion.py` no estaba en disco ni en `64bb48e`, y por instrucción del usuario se elimina de la documentación. Se borra `docs/Agents/linea_base_documental.json`, que solo usaba ese script. A petición posterior del usuario se añade [`docs/Agents/Scripts/GenerarIndices.py`](Scripts/GenerarIndices.py), que regenera `INVENTARIO.md`, los tres `SIMBOLOS.md` y `CONFIGURACION_GENERADA.md` conservando las descripciones escritas a mano, y comprueba enlaces; `--comprobar` no escribe. `MANTENIMIENTO.md`, `Agents/README.md`, `AGENTS.md` y el README raíz indican ejecutarlo. Ejecutado: la generación dejó `CONFIGURACION_GENERADA.md` y el índice Blender iguales salvo la línea de cabecera, y `--comprobar` a continuación informó «Catálogos al día y enlaces correctos» con código 0. Todos los enlaces relativos de `docs/` y del README raíz resuelven, salvo dos enlaces de `docs/Audit/` (informe de auditoría y `resolves/README.md`) a `resolves/2026-10-13-reorganizacion-documental.md`, que tampoco está en disco ni en `64bb48e`; no se modifican esos registros de auditoría.
## 2026-10-13 — Constantes de versión sin uso en Contratos

Se eliminan `ESQUEMA_PARAMETROS`, `ESQUEMA_NORMALIZACION`, `VERSION_LECTOR` y `VERSION_EXPORTADOR` de `web/persistence/Contratos.py`. No tenían consumidores. Las columnas `parameter_schema_version`, `normalization_schema_version`, `reader_version` y `exporter_version` siguen en el modelo y en `DATABASE.md`.

**Evidencia ejecutada:** búsqueda en el repositorio sin otras referencias. `scripts/VerificarDocumentacion.py` no está en el árbol, así que no se regeneró la línea base.

## 2026-10-13 — Atributos en el diagrama entidad-relación

Se completa el ER de `AppBackend/DATABASE.md` con todos los atributos de las doce entidades, tipos, PK/FK/UK y nulabilidad. Las claves únicas compuestas se identifican con comentarios de agrupación; la sección de integridad conserva el detalle de FK compuestas e índices parciales. Se contrasta la cobertura de atributos con el diccionario de tablas y se ejecuta la verificación documental. El cambio es únicamente documental; no implementa PostgreSQL ni modifica el esquema propuesto.

## 2026-10-13 — Propuesta de PostgreSQL sin ORM

Se incorpora `AppBackend/DATABASE.md` como propuesta expresamente no implementada: doce tablas de dominio, ER/UML/secuencia, contratos de repositorios SQL/Psycopg, archivos privados, versiones inmutables, lotes durables, intentos y leases, historial y futura vista Reflex. Se especifican Docker, migraciones SQL/dbmate, seed y targets Makefile únicamente como trabajo posterior.

Decisiones confirmadas por el usuario: no usar ORM y conservar binarios en almacenamiento privado con referencias, hashes, parámetros y resultados en PostgreSQL. Al aclararse que el alcance era solo documental, se retiraron todos los archivos nuevos de infraestructura que se habían empezado a crear; no quedan Makefile, Compose, migraciones ni seed de esa propuesta. No se cambia código de aplicación ni se ejecutan SQL o contenedores.

Se añade `erDiagram` a los tipos aceptados por el verificador documental. La verificación de enlaces, índices, parámetros y huellas se ejecuta tras regenerar hechos. No se presentan pruebas PostgreSQL/Docker como ejecutadas ni se cierran hallazgos de la auditoría independiente.

## 2026-10-13 — Reorganización inicial

Base de código revisada: `2b74669`. Árbol inicialmente sin cambios locales. Proyecto Python 0.1.0; Blender `bl_info` 1.3.0, mínimo 5.0; entorno local Reflex 0.9.12 / NumPy 2.5.3.

Se crean AppBackend, AppFrontend y BlenderPlugin con arquitectura, módulos, contratos, algoritmos, parámetros, operación e índices de símbolos. Se separan núcleo común, UI web y adaptadores Blender. La documentación previa aporta contexto, pero las afirmaciones técnicas se contrastan con la fuente actual y las skills/referencias oficiales Reflex.

Se aclaran diferencias observadas: macizo web sin refinamiento, voxel/validación final solo Blender, cachés web de proceso, NPZ internos en directorio de subidas, límites de UI frente a API, sidecar `*.stl.json`, parámetros ocultos aún validados y base conservada con borde de trabajo suavizado. El encabezado histórico de Cascaron tiene sentido de normal contrario a la expresión actual; se documenta `p+n*t` sin modificar el algoritmo.

Se añaden instrucciones persistentes y verificador local para regenerar índices/configuración/inventario y detectar deriva. No se modifica lógica de generación, interfaz de producto, dependencias, ZIP ni infraestructura de despliegue.

**Evidencia ejecutada:** suite Python existente, 51 pruebas aprobadas; verificación documental e índices; validación sintáctica Python del verificador; comprobaciones de que el verificador detecta deriva y enlaces rotos mediante fixtures temporales. Los resultados específicos finales se informan al entregar.

**Fuera de la ejecución de esta revisión:** integración Blender, recompilación Reflex, pruebas end-to-end de navegador y renderizado completo Mermaid. Los diagramas son fuente Mermaid editable; se comprueban bloques y tipos. Los logs/JSON históricos no se presentan como nuevas pruebas.

## Plantilla para futuras entradas

```text
AAAA-MM-DD — Cambio y motivo
Base de código / versión:
Fuentes y contratos afectados:
Documentos y diagramas actualizados:
Pruebas y validaciones ejecutadas (comando y resultado):
Comprobaciones no ejecutadas y limitación:
```

## 2026-10-13 — Organización final solicitada

Se concentra la mantenibilidad con agentes en `docs/Agents/`, junto con estándar, inventario, referencias Reflex, historial y manifiesto. La guía breve se traslada a `docs/BlenderPlugin/LEEME.md`. En la raíz de `docs/` queda solo el README que explica las carpetas.

Se actualizan enlaces, rutas de instrucciones y destinos del verificador. El empaquetador cambia exclusivamente la ruta fuente de la guía; conserva su ubicación `GenerateModelsApp/LEEME.md` dentro del ZIP. Se registra el alcance de esta reorganización en Audit/resolves sin cerrar hallazgos de la auditoría independiente.

## 2026-10-13 — Auditoría de código y bloqueo de archivos

Se incorpora [AUD-2026-10-13-001](../Audit/audits/2026-10-13-auditoria-base-codigo.md)
con alcance de partida en `2b74669`, inventario SHA-256, 22 hallazgos y evidencias.
Se crean `Audit/audits` y `Audit/resolves` y se añade la regla de bloqueo en
`AGENTS.md`. No se corrige lógica de producto ni se cierran hallazgos. El
protocolo y las plantillas de `resolves` no constituyen un cierre.

Evidencia de esta auditoría: 51 pruebas Python aprobadas; integración
`tests/blender_superficie_abierta.py` aprobada en Blender 5.2.2 con escritura del
JSON histórico redirigida a un temporal; reproducciones adicionales de entrada
NPZ, normales, topología, refinamiento, caché y exportación. Se contrastó el ZIP
con las fuentes antes de los traslados documentales concurrentes. No se ejecutó
`blender_paquete_zip.py`, navegador, escaneo CVE/licencias o build de wheel.
El informe conserva los detalles, criterios de cierre y límites del alcance.

Comprobación final: verificador documental aprobado (64 fuentes, 29 documentos,
13 diagramas), y validación propia de JSON, enlaces y bloques de `docs/Audit`.
Se verificó el nombre físico `Audit`, con A mayúscula, y se preservó el registro
de reorganización concurrente sin cerrar los hallazgos de código.
