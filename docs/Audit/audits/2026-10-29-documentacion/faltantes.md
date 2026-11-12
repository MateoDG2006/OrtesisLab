# Aspectos que faltan o no coinciden con el código

**Estado:** propuesta, AUD-2026-10-29-002. Cada fila indica dónde corregir, qué
falta y con qué evidencia. Las filas **D** son discrepancias con el código
vigente. Las filas **F** son contenido ausente; algunas solo pueden resolverse
con una decisión del responsable. La columna «Propuesta» enlaza la sección de
esta carpeta que ya lo cubre, cuando existe.

## D · Discrepancias entre la documentación canónica y el código

| ID | Documento canónico | Dice | Código vigente | Propuesta |
|---|---|---|---|---|
| D-01 | `docs/AppBackend/CONTRATOS.md` («Variantes, lotes y fichas») | `mode` (`single`, `batch`, `retry`) | `ModoLote.SWEEP = "sweep"`; `EstadoApp.py:393` usa `sweep` | [persistencia](backend/persistencia.md#enums-webenums) |
| D-02 | `docs/AppBackend/MODULOS.md` (`Contratos.py`) | «constantes de versión/cuota» | Solo hay constantes de cuota; las de versión no existen (B-01) | [configuración](backend/configuracion.md#constantes-que-no-son-configuración) |
| D-03 | `docs/AppBackend/OPERACION_Y_PRUEBAS.md` («Valores ajustables») | «Las constantes de contrato no están aquí: versiones de lector y exportador…» | No están en ningún sitio | ídem |
| D-04 | `docs/AppBackend/OPERACION_Y_PRUEBAS.md` («Pruebas existentes») y `tests/README.md` | 73 pruebas: 50 aprobadas y 23 omitidas | 46 cargadas: 38 aprobadas y 8 omitidas; 27 no cargan | [calidad](calidad/pruebas-y-estandares.md#línea-base-actual) |
| D-05 | `docs/Agents/REGISTRO_CAMBIOS.md` (2026-10-13, «Constantes de versión sin uso») | «No tenían consumidores» | Cuatro archivos las importan | [informe B-01](../2026-10-29-auditoria-evaluacion.md#b-01--p0--master-no-importa-se-eliminaron-constantes-que-siguen-en-uso) |
| D-06 | `docs/README.md:9` | Enlace `audit/README.md` | La carpeta es `docs/Audit` | — |
| D-07 | `docs/AppBackend/SIMBOLOS.md`, `docs/Agents/INVENTARIO.md` | Índices generados | `GenerarIndices --comprobar` los da por desactualizados; 4 archivos sin descripción | — |
| D-08 | `docs/AppBackend/CONTRATOS.md` (eventos de `/`) | `CancelarLote` es un evento público | Ningún componente lo invoca (B-22) | [frontend](frontend/estado-paginas-visor.md#estadoapp-eventos) |
| D-09 | `docs/AppBackend/CONTRATOS.md` («Opciones y escala») | «`_Numero` admite coma decimal» | Cierto en el servidor, pero `rx.input(type="number")` puede impedir escribir la coma | [frontend](frontend/estado-paginas-visor.md#estadoapp-eventos) |
| D-10 | `GenerateModelsApp.zip` | Contiene `LEEME.md` | No coincide con `docs/BlenderPlugin/LEEME.md` (B-16) | [núcleo](nucleo-blender/modulos.md#empaquetado) |
| D-11 | `README.md` («Setup») | Secuencia de arranque | No completa: falta la revisión Alembic (B-02) y el import falla (B-01) | [infraestructura](infraestructura/entorno-local.md#arranque-desde-cero-procedimiento-actual-y-dónde-se-rompe) |
| D-12 | `docs/AppBackend/CONTRATOS.md` («Opciones y escala») | Las 17 claves se describen como geometría compartida | `repair` y `resolution_mm` no influyen en la geometría web, pero entran en el hash de la versión (B-19) | [núcleo](nucleo-blender/modulos.md#modelingpy--model3dforprinting) |

## F · Contenido que falta

### Identidad y producto

| ID | Falta | Por qué importa | Quién decide |
|---|---|---|---|
| F-01 | Tipo de proyecto (comercial, investigación, clínico, interno) y su objetivo medible | Determina requisitos de regulación, privacidad y SLA | Responsable del producto |
| F-02 | Requisitos aprobados con identificador y criterio de aceptación | Hoy solo hay requisitos inferidos ([identidad](identidad/proyecto.md#requisitos-observados)) | Responsable del producto |
| F-03 | Clasificación de los datos (superficies de pacientes) y base legal | Necesaria para B-13 y B-14 | Responsable / legal |
| F-04 | Capacidad objetivo: usuarios simultáneos, lotes por hora, tiempo máximo por variante | Sin ella no se puede validar la escalabilidad | Responsable del producto |

### Backend

| ID | Falta | Propuesta |
|---|---|---|
| F-05 | Ficha de cada método público (E/P/S/Err/Ef) de servicios y repositorios | [persistencia](backend/persistencia.md), [servicios](backend/servicios-y-flujos.md) |
| F-06 | Máquinas de estado completas, incluidos los estados sin productor (`quarantined`, `deleting`, `validating`, `deletion_pending`) | [servicios](backend/servicios-y-flujos.md#máquinas-de-estado) |
| F-07 | Matriz de excepciones del trabajador y si cada una se reintenta | [servicios](backend/servicios-y-flujos.md#ciclo-del-trabajador-trabajadorgeneracion) |
| F-08 | Catálogo de eventos de historial con emisor, transacción y `payload` | [servicios](backend/servicios-y-flujos.md#eventos-de-historial) |
| F-09 | Formato exacto de las claves Redis y su contenido | [integraciones](backend/integraciones.md#caché-redis-webcachecacheredispy) |
| F-10 | Momento de lectura de cada variable y de cada clave YAML (arranque, primera operación, import) | [configuración](backend/configuracion.md) |
| F-11 | Efecto de `statement_timeout` de 15 s en historial y progreso | [infraestructura](infraestructura/entorno-local.md#roles-postgresql-infradatabaseinit01_rolessh-solo-con-volumen-nuevo) |
| F-12 | Política de retención y borrado (sesiones, eventos, imports `ready`, STL) | Requiere F-03 (B-13) |
| F-13 | Modelo de amenazas: CSRF, origen de WebSocket, URL pública de STL, dependencias CDN | Parcial en [integraciones](backend/integraciones.md#oidc-y-sesión); falta un documento dedicado |
| F-14 | Observabilidad: qué se registra, dónde, rotación, métricas y alertas | No existe; no hay métricas implementadas |
| F-15 | Recuperación ante desastre: RPO/RTO y respaldo consistente de base y bucket | Parcial en [infraestructura](infraestructura/entorno-local.md#objetivos-del-makefile) |
| F-16 | Revisión inicial de Alembic y su SQL manual | Es código, no documentación (B-02) |

### Frontend

| ID | Falta | Propuesta |
|---|---|---|
| F-17 | Lista de variables de estado con tipo e inicial, y de mensajes visibles por evento | [frontend](frontend/estado-paginas-visor.md) |
| F-18 | Zona horaria: los filtros son UTC y la columna «Fecha» usa la hora del servidor | [frontend](frontend/estado-paginas-visor.md#estadohistorial) |
| F-19 | Dependencia de la API interna `reflex_base` | [calidad](calidad/pruebas-y-estandares.md#herramientas-y-estándares) |
| F-20 | Criterios de accesibilidad (WCAG) y prueba del árbol de accesibilidad | No existe (A-20) |

### Núcleo y Blender

| ID | Falta | Propuesta |
|---|---|---|
| F-21 | Secuencia exacta de `ConstruirGeometria` y orden de validación de opciones con su excepción | [núcleo](nucleo-blender/modulos.md#modelingpy--model3dforprinting) |
| F-22 | Contrato numérico de `EscalaMalla` (rangos, orden de candidatos, presupuesto) | [núcleo](nucleo-blender/modulos.md#escalamallapy) |
| F-23 | Fichas con cuerpo leído de `Recortar`, `Refinar` (completo), `AnalizadorMalla.Preparar` y los adaptadores | Pendiente: esta propuesta solo usa su firma |
| F-24 | Docstrings EPS en las funciones que no los tienen (A-18) | Requiere editar código bloqueado |

### Calidad y operación

| ID | Falta | Propuesta |
|---|---|---|
| F-25 | Línea base de pruebas fechada y reproducible por revisión | [calidad](calidad/pruebas-y-estandares.md#línea-base-actual) |
| F-26 | Estándar de código ejecutable (lint, formato, tipos) | [calidad](calidad/pruebas-y-estandares.md#propuesta-mínima-de-estándar-ejecutable) |
| F-27 | CI de pruebas y documentación | B-03 |
| F-28 | Registro de cobertura fuente → documento de todos los archivos | [cobertura](cobertura-fuentes.md) |
| F-29 | Cómo conciliar la regla de mantenimiento de `AGENTS.md` con el bloqueo de auditorías | Decisión del usuario (B-17) |

## Cómo incorporar esta propuesta a la documentación canónica

1. El usuario autoriza de forma explícita editar los documentos canónicos
   afectados. Se registra en `docs/Audit/resolves/` con el alcance, enumerando
   archivos y hallazgos.
2. Se corrigen las discrepancias D-01 a D-12 en los documentos canónicos.
3. Se integran las fichas granulares en `AppBackend/MODULOS.md`,
   `CONTRATOS.md`, `AppFrontend/COMPONENTES_Y_FLUJOS.md` y
   `BlenderPlugin/MODULOS.md`, o se enlazan como anexos.
4. Se ejecutan `GenerarIndices.py` y `--comprobar`, y se actualiza
   `REGISTRO_CAMBIOS.md` con pruebas realmente ejecutadas.
5. Se cierra en el resolve el alcance documental. Los hallazgos de código siguen
   abiertos hasta que se corrijan.
