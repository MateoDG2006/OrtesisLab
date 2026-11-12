# Registro de cobertura fuente → documento

**Estado:** propuesta. **Inventario:** completo para el alcance de
AUD-2026-10-29-002, con 181 archivos versionados en `e56df68`, salvo
`docs/Audit/**` y `.agents/**`. Lo genera un script a partir del
[inventario](../2026-10-29-inventario.json); la responsabilidad sale de la
primera línea del docstring del módulo, o de una descripción fija en el caso
de los no Python.

Valores de la columna «Estado»:

- **documentado:** tiene una sección en esta propuesta.
- **canónico:** es documentación del proyecto, revisada frente al código.
- **excluido:** archivo generado o histórico.
- **hallazgos:** IDs de AUD-2026-10-29-002 que afectan al archivo.

La relación entre consumidores y contratos de cada archivo está en el documento
de destino.

| Archivo | Área de auditoría | Documento de destino | Responsabilidad | Estado |
|---|---|---|---|---|
| `.codegraph/.gitignore` | proyecto | [faltantes.md](faltantes.md) | Exclusiones del índice CodeGraph | documentado |
| `.env.example` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Plantilla de variables de la app | documentado |
| `.github/scripts/README.md` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Guía del script de sincronización Notion | documentado |
| `.github/scripts/notion_sync_issues.py` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Sincroniza tareas de Notion (base Tasksk, proyecto OrtesisLab) -> issues de GitHub | documentado; hallazgos B-21 |
| `.github/workflows/notion-to-issues.yml` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Workflow Notion → Issues (manual y diario) | documentado; hallazgos B-03, B-21 |
| `.gitignore` | proyecto | [faltantes.md](faltantes.md) | Exclusiones de Git | documentado |
| `.python-version` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Intérprete 3.14 | documentado |
| `.vscode/settings.json` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Vacío | documentado; hallazgos B-18 |
| `AGENTS.md` | proyecto | [faltantes.md](faltantes.md) | Reglas de agentes, documentación y bloqueo | canónico; deriva en B-17 |
| `CLAUDE.md` | proyecto | [faltantes.md](faltantes.md) | Redirige a AGENTS.md | canónico |
| `GenerateModelsApp.zip` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Distribución del complemento (artefacto) | artefacto; B-16 |
| `GenerateModelsApp/ApiBlender.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | API de Blender, separada del núcleo geométrico | documentado |
| `GenerateModelsApp/Cascaron.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Recorte de celdas y cascarón de espesor variable | documentado |
| `GenerateModelsApp/EscalaMalla.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Diagnóstico de unidades para una superficie de ortesis | documentado |
| `GenerateModelsApp/Excepciones.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Errores de OrtesisLab | documentado |
| `GenerateModelsApp/Exportacion.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Exporta el STL en milímetros y un JSON con parámetros y comprobación | documentado |
| `GenerateModelsApp/Interfaz.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Panel N y operadores de OrtesisLab en la vista 3D | documentado |
| `GenerateModelsApp/Malla.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Análisis de la superficie abierta, sin Blender | documentado |
| `GenerateModelsApp/Modeling.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Modelo de impresión y construcción de la geometría | documentado; hallazgos B-19 |
| `GenerateModelsApp/Objeto.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Crea o actualiza el objeto OL_Ortesis en la escena de Blender | documentado |
| `GenerateModelsApp/OrtesisLab.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Complemento OrtesisLab dentro del paquete | documentado |
| `GenerateModelsApp/RefinadorMalla.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Refinamiento triangular independiente de Blender para evaluar patrones | documentado |
| `GenerateModelsApp/ReparacionMalla.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Limpieza segura de la superficie base dentro de Blender | documentado |
| `GenerateModelsApp/SuavizadoBorde.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Suavizado del contorno exterior antes de dar espesor | documentado |
| `GenerateModelsApp/Superficie.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Carga y lectura de la superficie interior dentro de Blender | documentado |
| `GenerateModelsApp/ValidacionMalla.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Comprobación geométrica de la malla ya generada | documentado |
| `GenerateModelsApp/__init__.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Paquete del complemento de Blender y del núcleo de geometría | documentado |
| `GenerateModelsApp/config/comprobacion_geometrica.json` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Configuración JSON del núcleo | documentado |
| `GenerateModelsApp/config/limites.json` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Configuración JSON del núcleo | documentado |
| `GenerateModelsApp/config/parametros_defecto.json` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Configuración JSON del núcleo | documentado |
| `GenerateModelsApp/config/registro.json` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Configuración JSON del núcleo | documentado |
| `GenerateModelsApp/constants/Materials.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Materiales de impresión | documentado |
| `GenerateModelsApp/constants/Nombres.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Nombres estables de objetos, atributos y archivos | documentado |
| `GenerateModelsApp/constants/Paterns.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Patrones de nervadura | documentado |
| `GenerateModelsApp/constants/__init__.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Constantes de OrtesisLab: nombres, patrones, materiales y límites | documentado |
| `GenerateModelsApp/util/Utilidades.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Registro de mensajes y lectura de la carpeta config | documentado |
| `GenerateModelsApp/util/__init__.py` | nucleo-blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Utilidades compartidas: registro de ejecución y lectura de JSON | documentado |
| `Makefile` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Operación local de Compose | documentado |
| `README.md` | proyecto | [faltantes.md](faltantes.md) | Entrada del repositorio | canónico; deriva en B-17 |
| `alembic.ini` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Configuración Alembic | documentado; hallazgos B-02 |
| `assets/README.md` | proyecto | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Guía de assets | documentado |
| `assets/favicon.ico` | proyecto | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Icono web | documentado |
| `assets/superficie_interior_mm.npz` | proyecto | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Plantilla de superficie incluida | documentado |
| `assets/visor.html` | proyecto | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Visor Three.js del STL por object_url | documentado; hallazgos B-14 |
| `config/almacen.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-09 |
| `config/cache.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-09 |
| `config/persistencia.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-05, B-08, B-09 |
| `config/sesion.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-09 |
| `config/trabajador.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-09 |
| `config/web.yaml` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend | documentado; hallazgos B-05, B-08, B-09 |
| `db/alembic/env.py` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Entorno de Alembic: migra el esquema ortesislab con el rol migrador | documentado; hallazgos B-02 |
| `db/alembic/script.py.mako` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Plantilla de revisiones Alembic | documentado |
| `db/alembic/versions/.gitkeep` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Mantiene carpeta vacía | documentado; hallazgos B-02 |
| `db/seeds/development.sql` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Fixture de desarrollo | documentado |
| `db/test/preparar_base.sql` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Esquema y permisos en base vacía | documentado; hallazgos B-02 |
| `docs/Agents/ESTANDAR_DOCUMENTACION.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/Agents/GUIA_REFLEX.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/Agents/INVENTARIO.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-17 |
| `docs/Agents/MANTENIMIENTO.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/Agents/README.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/Agents/REGISTRO_CAMBIOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-01 |
| `docs/Agents/Scripts/GenerarIndices.py` | documentacion | [faltantes.md](faltantes.md) | Regenera los catálogos de hechos de la documentación y comprueba enlaces | canónico; deriva en B-17 |
| `docs/AppBackend/ARQUITECTURA.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppBackend/CONTRATOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-17 |
| `docs/AppBackend/DATABASE.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-02 |
| `docs/AppBackend/MODULOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-17 |
| `docs/AppBackend/OPERACION_Y_PRUEBAS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-02, B-17 |
| `docs/AppBackend/README.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppBackend/SIMBOLOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-17 |
| `docs/AppFrontend/ARQUITECTURA.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppFrontend/COMPONENTES_Y_FLUJOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppFrontend/OPERACION_Y_PRUEBAS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppFrontend/README.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppFrontend/SIMBOLOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/AppFrontend/VISOR_3D.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/ALGORITMOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/API_Y_DATOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/ARQUITECTURA.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/CONFIGURACION_GENERADA.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/LEEME.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-16 |
| `docs/BlenderPlugin/MODULOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/OPERACION_Y_PRUEBAS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/PARAMETROS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/README.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/BlenderPlugin/SIMBOLOS.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico |
| `docs/README.md` | documentacion | [faltantes.md](faltantes.md) | Documentación canónica | canónico; deriva en B-17 |
| `infra/database/.env.example` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Plantilla de secretos de Compose | documentado |
| `infra/database/.gitattributes` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Fin de línea de scripts de infraestructura | documentado |
| `infra/database/.gitignore` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Excluye .env y backups | documentado |
| `infra/database/backups/.gitkeep` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Mantiene carpeta vacía | documentado |
| `infra/database/compose.yaml` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Servicios locales | documentado |
| `infra/database/init/01_roles.sh` | infraestructura-configuracion | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Roles y esquema al crear el volumen | documentado |
| `infra/database/minio/inicializar.sh` | infraestructura-configuracion | [backend/integraciones.md](backend/integraciones.md) | Bucket, políticas y cuenta de servicio | documentado |
| `infra/database/minio/politica-aplicacion.json` | infraestructura-configuracion | [backend/integraciones.md](backend/integraciones.md) | Política de la cuenta de servicio | documentado |
| `infra/database/minio/politica-lectura-stl.json` | infraestructura-configuracion | [backend/integraciones.md](backend/integraciones.md) | Lectura anónima de STL de resultado | documentado; hallazgos B-14 |
| `pyproject.toml` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Manifiesto y dependencias | documentado; hallazgos B-18 |
| `reflex.lock/bun.lock` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Lock del frontend | excluido: generado |
| `reflex.lock/package.json` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Lock del frontend | excluido: generado |
| `rxconfig.py` | infraestructura-configuracion | [backend/configuracion.md](backend/configuracion.md) | Configuración Reflex (módulo, plugins, tema); sin docstring | documentado; hallazgos B-15 |
| `scripts/EjecutarOrtesisLab.py` | herramientas | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Script para abrir el complemento dentro de Blender | documentado |
| `scripts/EjecutarTrabajador.py` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Proceso trabajador de OrtesisLab: cola de generación y conciliación | documentado |
| `scripts/EmpaquetarBlender.py` | herramientas | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) | Genera el ZIP instalable de Blender, sin Reflex, logs ni la base v5 | documentado; hallazgos B-16 |
| `scripts/IniciarConsola.py` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Script del comando de consola del proyecto | documentado; hallazgos B-18 |
| `scripts/MigrarSubidas.py` | herramientas | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) | Traslada una sola vez ``uploaded_files/`` al bucket y registra cada objeto | documentado; hallazgos B-01 |
| `skills-lock.json` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Versión fijada de skills Reflex | documentado |
| `src/generatemodelsapp/__init__.py` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Marcador de paquete | documentado; hallazgos B-18 |
| `tests/README.md` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Guía de pruebas por carpeta | documentado; hallazgos B-17 |
| `tests/aplicacion_web/__init__.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Pruebas del generador web y del lector de superficies | documentado |
| `tests/aplicacion_web/test_generador_web.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Comprueba el lote y el STL sin abrir Blender ni la superficie real | documentado |
| `tests/assets/Test.stl` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Fixture de superficie | documentado |
| `tests/assets/blender_ejecucion.log` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Log histórico (no evidencia actual) | excluido: histórico |
| `tests/assets/nucleo_ejecucion.log` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Log histórico (no evidencia actual) | excluido: histórico |
| `tests/assets/resultado_blender.json` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Resultado histórico (no evidencia actual) | excluido: histórico |
| `tests/assets/zip_ejecucion.log` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Log histórico (no evidencia actual) | excluido: histórico |
| `tests/blender/__init__.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Scripts de integración que ejecuta Blender; unittest no los recoge | documentado |
| `tests/blender/blender_paquete_zip.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Comprueba el paquete distribuido en aislamiento, sin assets ni Reflex | documentado |
| `tests/blender/blender_superficie_abierta.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Ejecutar con Blender --background --factory-startup --python-exit-code 1 --python este_archivo | documentado |
| `tests/geometria/__init__.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Pruebas de escala, refinamiento, suavizado de borde y espesor | documentado |
| `tests/geometria/test_escala_malla.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Diagnóstico de unidades de una superficie antes de usar Blender | documentado |
| `tests/geometria/test_refinador_malla.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Refinamiento de patrones web sin depender de Blender | documentado |
| `tests/geometria/test_suavizado_borde.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | El contorno exterior pierde los dientes y conserva la forma general | documentado |
| `tests/geometria/test_superficie_abierta.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Regresiones del espesor: pared cerrada, canal superior abierto | documentado |
| `tests/nucleo/__init__.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Pruebas del núcleo geométrico: validación, catálogo, volumen y material | documentado |
| `tests/nucleo/test_nucleo.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Comprueba que el núcleo repartido conserva la geometría del script original | documentado |
| `tests/persistencia/__init__.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Pruebas de PostgreSQL, bucket, Redis, lotes, trabajador y permisos | documentado |
| `tests/persistencia/apoyo_persistencia.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Apoyo de pruebas contra la base desechable ``ortesislab_test`` | documentado |
| `tests/persistencia/test_almacen_import.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Import al bucket, caché Redis y migración de subidas locales | documentado |
| `tests/persistencia/test_lotes_trabajador.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Lotes idempotentes, trabajador con lease, aislamiento y conciliación | documentado |
| `tests/persistencia/test_propiedad_datos.py` | pruebas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Propiedad de los datos y permisos de rol sobre PostgreSQL real | documentado |
| `uv.lock` | proyecto | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) | Resolución Python bloqueada | excluido: generado |
| `web/Ajustes.py` | backend-web | [backend/configuracion.md](backend/configuracion.md) | Variables de entorno de OrtesisLab: el único lugar que las declara y las lee | documentado |
| `web/ConfiguracionBackend.py` | backend-web | [backend/configuracion.md](backend/configuracion.md) | Valores ajustables del backend, leídos de ``config/<area>.yaml`` en la raíz | documentado; hallazgos B-09 |
| `web/EstadoApp.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Estado de la página de comparación | documentado; hallazgos B-04, B-08, B-10, B-22 |
| `web/EstadoHistorial.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Estado de /historial: filtros, cursor y comparación de hasta tres versiones | documentado; hallazgos B-19 |
| `web/GeneradorWeb.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Genera cascarones para la aplicación web | documentado; hallazgos B-04, B-10 |
| `web/GenerateModelsApp.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Aplicación Reflex de comparación de ortesis | documentado |
| `web/LectorSuperficie.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Lectura de superficies subidas a la aplicación web | documentado; hallazgos B-04 |
| `web/PaginaComparacion.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Pantalla para previsualizar una ortesis o un lote de variantes | documentado; hallazgos B-14, B-22 |
| `web/PaginaHistorial.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Pantalla /historial: generaciones del usuario, comparación y restauración | documentado |
| `web/Sesion.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Barra de sesión común a la comparación y al historial | documentado |
| `web/__init__.py` | backend-web | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) | Aplicación Reflex | documentado |
| `web/cache/CacheRedis.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Caché compartida de superficies preparadas | documentado |
| `web/cache/__init__.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Marcador de paquete | documentado |
| `web/enums/Archivos.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Tipos y estados de los objetos del bucket registrados en ``file_assets`` | documentado |
| `web/enums/Historial.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Tipos de evento de ``history_events`` | documentado; hallazgos B-13 |
| `web/enums/Imports.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Origen, estado y formato de una superficie importada (``imports``) | documentado |
| `web/enums/Lotes.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Backend de versión, modos de lote y estados de lotes, ítems e intentos | documentado |
| `web/enums/Resultados.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Validación y alcance de ``generation_results`` y formato, unidad y estado de ``exports`` | documentado |
| `web/enums/Usuarios.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Estados de una cuenta de ``app_users`` | documentado; hallazgos B-13 |
| `web/enums/__init__.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Valores cerrados del dominio. Deben coincidir con los ``CHECK`` del esquema | documentado |
| `web/jobs/ConciliadorArchivos.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Conciliación entre filas de ``file_assets`` y objetos del bucket | documentado; hallazgos B-05, B-06, B-12 |
| `web/jobs/TrabajadorGeneracion.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Trabajador de generación: un ítem a la vez, con lease y latido | documentado; hallazgos B-11, B-20 |
| `web/jobs/__init__.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Marcador de paquete | documentado |
| `web/persistence/ConexionPostgres.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Motor SQLAlchemy y sesiones por proceso | documentado |
| `web/persistence/Contratos.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | DTO y errores de la persistencia. No son entidades ORM | documentado; hallazgos B-01 |
| `web/persistence/Modelos.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Modelos declarativos de SQLAlchemy del esquema ``ortesislab`` | documentado; hallazgos B-02, B-07, B-08 |
| `web/persistence/__init__.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Acceso a PostgreSQL con SQLAlchemy 2.0; el esquema se versiona con Alembic | documentado |
| `web/persistence/repositorios/Consultas.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Tablas y fragmentos de consulta que comparten varios repositorios | documentado; hallazgos B-10 |
| `web/persistence/repositorios/RepositorioAssets.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Filas de ``file_assets``: el contenido vive en el bucket | documentado; hallazgos B-12 |
| `web/persistence/repositorios/RepositorioBase.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Clase padre de los repositorios: lectura de filas y conversión a DTO | documentado |
| `web/persistence/repositorios/RepositorioHistorial.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Eventos de historial y listado de ejecuciones por versión | documentado |
| `web/persistence/repositorios/RepositorioImports.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Importaciones de superficies: original recibido y NPZ normalizado | documentado; hallazgos B-07 |
| `web/persistence/repositorios/RepositorioLotes.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Lotes, ítems y cola del trabajador: admisión, reserva, lease y cierre | documentado; hallazgos B-10, B-11 |
| `web/persistence/repositorios/RepositorioPreferencias.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Preferencias por usuario con control optimista de revisión | documentado |
| `web/persistence/repositorios/RepositorioProyectos.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Proyectos del usuario; cada cuenta tiene uno predeterminado | documentado |
| `web/persistence/repositorios/RepositorioResultados.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Resultados geométricos, intentos de una versión y exports STL | documentado |
| `web/persistence/repositorios/RepositorioUsuarios.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Cuentas creadas desde OIDC y sus sesiones de servidor | documentado; hallazgos B-13 |
| `web/persistence/repositorios/RepositorioVersiones.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Versiones inmutables numeradas por proyecto | documentado |
| `web/persistence/repositorios/__init__.py` | backend-web | [backend/persistencia.md](backend/persistencia.md) | Repositorios SQLAlchemy, uno por archivo. Reciben una ``Session`` ya abierta y no hacen commit | documentado |
| `web/services/AutenticacionOidc.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Rutas OIDC del backend: /auth/login, /auth/callback y /auth/logout | documentado; hallazgos B-15 |
| `web/services/ContextoUsuario.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Principal autenticado de cada operación | documentado |
| `web/services/GeneradorGeometrico.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Construcción numérica de una versión: métricas, STL y JSON de parámetros | documentado |
| `web/services/ServicioHistorial.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Historial por usuario: listado paginado, detalle, restauración y reintento | documentado |
| `web/services/ServicioImports.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Importación de superficies: original y NPZ normalizado en el bucket | documentado; hallazgos B-01, B-04, B-05, B-06, B-07 |
| `web/services/ServicioLotes.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Admisión de lotes, progreso y transiciones del trabajador | documentado; hallazgos B-01, B-10, B-20 |
| `web/services/ServicioPreferencias.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Preferencias por usuario con control optimista de revisión | documentado |
| `web/services/ServicioVersiones.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Versiones inmutables: snapshot de parámetros, material y escala | documentado; hallazgos B-01, B-19 |
| `web/services/__init__.py` | backend-web | [backend/servicios-y-flujos.md](backend/servicios-y-flujos.md) | Marcador de paquete | documentado |
| `web/storage/AlmacenamientoPrivado.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Contrato del almacén de bytes y claves de objeto | documentado |
| `web/storage/StorageS3.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Almacén de bytes en un bucket S3 (MinIO en desarrollo) | documentado |
| `web/storage/__init__.py` | backend-web | [backend/integraciones.md](backend/integraciones.md) | Marcador de paquete | documentado |
