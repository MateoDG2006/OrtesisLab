# Índice de símbolos: AppBackend

> Generado por `python docs/Agents/Scripts/GenerarIndices.py`. No editar a mano.

Incluye funciones anidadas y métodos privados para localizar todas las piezas. Las líneas son una ayuda de navegación; el nombre del símbolo es la referencia estable.

## `apps/web/rxconfig.py`

Marcador de paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/__init__.py`

Aplicación Reflex.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/Ajustes.py`

Variables de entorno de OrtesisLab: el único lugar que las declara y las lee.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Variable` | Clase | [22](../../apps/web/web/Ajustes.py#L22) | Una clave del entorno; sin ``defecto`` es obligatoria y no admite vacío. |
| `Variable.__init__` | Función/método | [25](../../apps/web/web/Ajustes.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Variable.__get__` | Función/método | [30](../../apps/web/web/Ajustes.py#L30) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Ajustes` | Clase | [43](../../apps/web/web/Ajustes.py#L43) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Ajustes.__init__` | Función/método | [71](../../apps/web/web/Ajustes.py#L71) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Ajustes.cookie_secure` | Función/método | [75](../../apps/web/web/Ajustes.py#L75) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Ajustes.Cargar` | Función/método | [80](../../apps/web/web/Ajustes.py#L80) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/cache/__init__.py`

Marcador de paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/cache/CacheRedis.py`

Caché compartida de superficies preparadas.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `CacheRedis` | Clase | [26](../../apps/web/web/cache/CacheRedis.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis.ClaveCruda` | Función/método | [31](../../apps/web/web/cache/CacheRedis.py#L31) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis.ClaveRefinada` | Función/método | [35](../../apps/web/web/cache/CacheRedis.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis.Usar` | Función/método | [39](../../apps/web/web/cache/CacheRedis.py#L39) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis._Cliente` | Función/método | [44](../../apps/web/web/cache/CacheRedis.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis._Fallo` | Función/método | [56](../../apps/web/web/cache/CacheRedis.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis.LeerTupla` | Función/método | [62](../../apps/web/web/cache/CacheRedis.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CacheRedis.GuardarTupla` | Función/método | [82](../../apps/web/web/cache/CacheRedis.py#L82) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/ConfiguracionBackend.py`

Valores ajustables del backend, leídos de ``core/config/<area>.yaml``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ConfiguracionBackend` | Clase | [17](../../apps/web/web/ConfiguracionBackend.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConfiguracionBackend.Cargar` | Función/método | [20](../../apps/web/web/ConfiguracionBackend.py#L20) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/__init__.py`

Valores cerrados del dominio. Deben coincidir con los ``CHECK`` del esquema.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/enums/Archivos.py`

Tipos y estados de los objetos del bucket registrados en ``file_assets``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `TipoAsset` | Clase | [6](../../apps/web/web/enums/Archivos.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoAsset` | Clase | [13](../../apps/web/web/enums/Archivos.py#L13) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ExtensionSuperficie` | Clase | [22](../../apps/web/web/enums/Archivos.py#L22) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/Historial.py`

Tipos de evento de ``history_events``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `TipoEvento` | Clase | [6](../../apps/web/web/enums/Historial.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/Imports.py`

Origen, estado y formato de una superficie importada (``imports``).

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `OrigenImport` | Clase | [6](../../apps/web/web/enums/Imports.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoImport` | Clase | [11](../../apps/web/web/enums/Imports.py#L11) | Sin docstring; consultar el catálogo de módulos y el código. |
| `FormatoImport` | Clase | [18](../../apps/web/web/enums/Imports.py#L18) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/Lotes.py`

Backend de versión, modos de lote y estados de lotes, ítems e intentos.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `BackendGeneracion` | Clase | [6](../../apps/web/web/enums/Lotes.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModoLote` | Clase | [10](../../apps/web/web/enums/Lotes.py#L10) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoLote` | Clase | [16](../../apps/web/web/enums/Lotes.py#L16) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoItem` | Clase | [25](../../apps/web/web/enums/Lotes.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoIntento` | Clase | [33](../../apps/web/web/enums/Lotes.py#L33) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/Resultados.py`

Validación y alcance de ``generation_results`` y formato, unidad y estado de ``exports``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `EstadoValidacion` | Clase | [6](../../apps/web/web/enums/Resultados.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlcanceGeometria` | Clase | [12](../../apps/web/web/enums/Resultados.py#L12) | Sin docstring; consultar el catálogo de módulos y el código. |
| `FormatoExport` | Clase | [16](../../apps/web/web/enums/Resultados.py#L16) | Sin docstring; consultar el catálogo de módulos y el código. |
| `UnidadExport` | Clase | [21](../../apps/web/web/enums/Resultados.py#L21) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoExport` | Clase | [25](../../apps/web/web/enums/Resultados.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/enums/Usuarios.py`

Estados de una cuenta de ``app_users``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `EstadoUsuario` | Clase | [6](../../apps/web/web/enums/Usuarios.py#L6) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/EstadoApp.py`

Estado de la página de comparación.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `EstadoApp` | Clase | [45](../../apps/web/web/EstadoApp.py#L45) | Parámetros del complemento, lote en curso y fichas ya generadas. |
| `EstadoApp.set_pattern` | Función/método | [106](../../apps/web/web/EstadoApp.py#L106) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_cell_mm` | Función/método | [110](../../apps/web/web/EstadoApp.py#L110) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_rib_width_mm` | Función/método | [114](../../apps/web/web/EstadoApp.py#L114) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_rib_height_mm` | Función/método | [118](../../apps/web/web/EstadoApp.py#L118) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_liner` | Función/método | [122](../../apps/web/web/EstadoApp.py#L122) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_skin_mm` | Función/método | [126](../../apps/web/web/EstadoApp.py#L126) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_solid_mm` | Función/método | [130](../../apps/web/web/EstadoApp.py#L130) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_border_mm` | Función/método | [134](../../apps/web/web/EstadoApp.py#L134) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_rounding_mm` | Función/método | [138](../../apps/web/web/EstadoApp.py#L138) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_angle_deg` | Función/método | [142](../../apps/web/web/EstadoApp.py#L142) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_seed` | Función/método | [146](../../apps/web/web/EstadoApp.py#L146) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_reinforce_y_mm` | Función/método | [150](../../apps/web/web/EstadoApp.py#L150) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_reinforce_width_mm` | Función/método | [154](../../apps/web/web/EstadoApp.py#L154) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_flip_normals` | Función/método | [158](../../apps/web/web/EstadoApp.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_surface_step_mm` | Función/método | [162](../../apps/web/web/EstadoApp.py#L162) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_usar_voronoi` | Función/método | [166](../../apps/web/web/EstadoApp.py#L166) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_usar_hex` | Función/método | [170](../../apps/web/web/EstadoApp.py#L170) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_usar_diamond` | Función/método | [174](../../apps/web/web/EstadoApp.py#L174) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_usar_square` | Función/método | [178](../../apps/web/web/EstadoApp.py#L178) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_usar_solid` | Función/método | [182](../../apps/web/web/EstadoApp.py#L182) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_eje` | Función/método | [186](../../apps/web/web/EstadoApp.py#L186) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_desde` | Función/método | [190](../../apps/web/web/EstadoApp.py#L190) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_hasta` | Función/método | [194](../../apps/web/web/EstadoApp.py#L194) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_paso` | Función/método | [198](../../apps/web/web/EstadoApp.py#L198) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.set_ambos_revestimientos` | Función/método | [202](../../apps/web/web/EstadoApp.py#L202) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.CargarSuperficie` | Función/método | [206](../../apps/web/web/EstadoApp.py#L206) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.UsarSuperficieIncluida` | Función/método | [252](../../apps/web/web/EstadoApp.py#L252) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.CargarPredeterminados` | Función/método | [263](../../apps/web/web/EstadoApp.py#L263) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.Previsualizar` | Función/método | [307](../../apps/web/web/EstadoApp.py#L307) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.PedirLote` | Función/método | [313](../../apps/web/web/EstadoApp.py#L313) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.Generar` | Función/método | [319](../../apps/web/web/EstadoApp.py#L319) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.SeguirLote` | Función/método | [391](../../apps/web/web/EstadoApp.py#L391) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.CancelarLote` | Función/método | [411](../../apps/web/web/EstadoApp.py#L411) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.Ver` | Función/método | [423](../../apps/web/web/EstadoApp.py#L423) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.Comparar` | Función/método | [430](../../apps/web/web/EstadoApp.py#L430) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.Descargar` | Función/método | [445](../../apps/web/web/EstadoApp.py#L445) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.espesor_total` | Función/método | [465](../../apps/web/web/EstadoApp.py#L465) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp.porcentaje` | Función/método | [474](../../apps/web/web/EstadoApp.py#L474) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Usuario` | Función/método | [479](../../apps/web/web/EstadoApp.py#L479) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Seguir` | Función/método | [494](../../apps/web/web/EstadoApp.py#L494) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Publicar` | Función/método | [515](../../apps/web/web/EstadoApp.py#L515) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._OlvidarTrabajo` | Función/método | [538](../../apps/web/web/EstadoApp.py#L538) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Mostrar` | Función/método | [550](../../apps/web/web/EstadoApp.py#L550) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Variantes` | Función/método | [558](../../apps/web/web/EstadoApp.py#L558) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Opciones` | Función/método | [588](../../apps/web/web/EstadoApp.py#L588) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoApp._Numero` | Función/método | [613](../../apps/web/web/EstadoApp.py#L613) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/EstadoHistorial.py`

Estado de /historial: filtros, cursor y comparación de hasta tres versiones.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `EstadoHistorial` | Clase | [35](../../apps/web/web/EstadoHistorial.py#L35) | Listado paginado del trabajo del usuario y comparación de versiones. |
| `EstadoHistorial.set_filtro_patron` | Función/método | [55](../../apps/web/web/EstadoHistorial.py#L55) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.set_filtro_estado` | Función/método | [59](../../apps/web/web/EstadoHistorial.py#L59) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.set_filtro_desde` | Función/método | [63](../../apps/web/web/EstadoHistorial.py#L63) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.set_filtro_hasta` | Función/método | [67](../../apps/web/web/EstadoHistorial.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Cargar` | Función/método | [71](../../apps/web/web/EstadoHistorial.py#L71) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Siguiente` | Función/método | [79](../../apps/web/web/EstadoHistorial.py#L79) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Anterior` | Función/método | [87](../../apps/web/web/EstadoHistorial.py#L87) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Seleccionar` | Función/método | [95](../../apps/web/web/EstadoHistorial.py#L95) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Restaurar` | Función/método | [107](../../apps/web/web/EstadoHistorial.py#L107) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Reintentar` | Función/método | [119](../../apps/web/web/EstadoHistorial.py#L119) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial.Descargar` | Función/método | [131](../../apps/web/web/EstadoHistorial.py#L131) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Usuario` | Función/método | [145](../../apps/web/web/EstadoHistorial.py#L145) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Leer` | Función/método | [164](../../apps/web/web/EstadoHistorial.py#L164) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Comparar` | Función/método | [192](../../apps/web/web/EstadoHistorial.py#L192) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Filtros` | Función/método | [209](../../apps/web/web/EstadoHistorial.py#L209) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Fecha` | Función/método | [218](../../apps/web/web/EstadoHistorial.py#L218) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Fila` | Función/método | [227](../../apps/web/web/EstadoHistorial.py#L227) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EstadoHistorial._Tarjeta` | Función/método | [251](../../apps/web/web/EstadoHistorial.py#L251) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/GeneradorWeb.py`

Genera cascarones para la aplicación web.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `_HuellaPlantilla` | Función/método | [44](../../apps/web/web/GeneradorWeb.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb` | Clase | [50](../../apps/web/web/GeneradorWeb.py#L50) | Prepara la superficie y traduce resultados persistidos a fichas de la página. |
| `GeneradorWeb._Origen` | Función/método | [54](../../apps/web/web/GeneradorWeb.py#L54) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Cruda` | Función/método | [68](../../apps/web/web/GeneradorWeb.py#L68) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Superficie` | Función/método | [80](../../apps/web/web/GeneradorWeb.py#L80) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb._Superficie` | Función/método | [84](../../apps/web/web/GeneradorWeb.py#L84) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.SuperficieRefinada` | Función/método | [95](../../apps/web/web/GeneradorWeb.py#L95) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb._SuperficieRefinada` | Función/método | [99](../../apps/web/web/GeneradorWeb.py#L99) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.GuardarSuperficie` | Función/método | [116](../../apps/web/web/GeneradorWeb.py#L116) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Crear` | Función/método | [122](../../apps/web/web/GeneradorWeb.py#L122) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb._FichaDeItem` | Función/método | [144](../../apps/web/web/GeneradorWeb.py#L144) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.FichaError` | Función/método | [173](../../apps/web/web/GeneradorWeb.py#L173) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Ficha` | Función/método | [181](../../apps/web/web/GeneradorWeb.py#L181) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Detalle` | Función/método | [204](../../apps/web/web/GeneradorWeb.py#L204) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Combinaciones` | Función/método | [236](../../apps/web/web/GeneradorWeb.py#L236) | Entrada: patrones, rango y paso. Proceso: acota el barrido antes de |
| `GeneradorWeb.Numero` | Función/método | [311](../../apps/web/web/GeneradorWeb.py#L311) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Stl` | Función/método | [317](../../apps/web/web/GeneradorWeb.py#L317) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Triangulos` | Función/método | [336](../../apps/web/web/GeneradorWeb.py#L336) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Escribir` | Función/método | [348](../../apps/web/web/GeneradorWeb.py#L348) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Leer` | Función/método | [359](../../apps/web/web/GeneradorWeb.py#L359) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.Ruta` | Función/método | [366](../../apps/web/web/GeneradorWeb.py#L366) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorWeb.RutaSuperficie` | Función/método | [377](../../apps/web/web/GeneradorWeb.py#L377) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/GenerateModelsApp.py`

Aplicación Reflex de comparación de ortesis.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `PoolPostgres` | Función/método | [26](../../apps/web/web/GenerateModelsApp.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/jobs/__init__.py`

Marcador de paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/jobs/ConciliadorArchivos.py`

Conciliación entre filas de ``file_assets`` y objetos del bucket.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ConciliadorArchivos` | Clase | [31](../../apps/web/web/jobs/ConciliadorArchivos.py#L31) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConciliadorArchivos.__init__` | Función/método | [32](../../apps/web/web/jobs/ConciliadorArchivos.py#L32) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConciliadorArchivos.Ejecutar` | Función/método | [35](../../apps/web/web/jobs/ConciliadorArchivos.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConciliadorArchivos._PurgarRetencion` | Función/método | [113](../../apps/web/web/jobs/ConciliadorArchivos.py#L113) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConciliadorArchivos._PurgarRetencion.purgar` | Función/método | [116](../../apps/web/web/jobs/ConciliadorArchivos.py#L116) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConciliadorArchivos._BorrarHuerfanos` | Función/método | [126](../../apps/web/web/jobs/ConciliadorArchivos.py#L126) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/jobs/TrabajadorGeneracion.py`

Trabajador de generación: un ítem a la vez, con lease y latido.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `_Revision` | Función/método | [40](../../apps/web/web/jobs/TrabajadorGeneracion.py#L40) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion` | Clase | [51](../../apps/web/web/jobs/TrabajadorGeneracion.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion.__init__` | Función/método | [52](../../apps/web/web/jobs/TrabajadorGeneracion.py#L52) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion.Ciclo` | Función/método | [58](../../apps/web/web/jobs/TrabajadorGeneracion.py#L58) | Procesa un ítem si hay alguno disponible. Devuelve si procesó. |
| `TrabajadorGeneracion.Procesar` | Función/método | [66](../../apps/web/web/jobs/TrabajadorGeneracion.py#L66) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion.Procesar.latir` | Función/método | [71](../../apps/web/web/jobs/TrabajadorGeneracion.py#L71) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion._FallarSinPerder` | Función/método | [125](../../apps/web/web/jobs/TrabajadorGeneracion.py#L125) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajadorGeneracion.Ejecutar` | Función/método | [132](../../apps/web/web/jobs/TrabajadorGeneracion.py#L132) | Bucle principal: supervisa leases, concilia archivos y procesa la cola. |

## `apps/web/web/LectorSuperficie.py`

Lectura de superficies subidas a la aplicación web.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `LectorSuperficie` | Clase | [20](../../apps/web/web/LectorSuperficie.py#L20) | Convierte STL o NPZ en los arreglos que consume el núcleo geométrico. |
| `LectorSuperficie.Preparar` | Función/método | [28](../../apps/web/web/LectorSuperficie.py#L28) | Sin docstring; consultar el catálogo de módulos y el código. |
| `LectorSuperficie._Npz` | Función/método | [72](../../apps/web/web/LectorSuperficie.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `LectorSuperficie._Stl` | Función/método | [89](../../apps/web/web/LectorSuperficie.py#L89) | Sin docstring; consultar el catálogo de módulos y el código. |
| `LectorSuperficie._StlBinario` | Función/método | [111](../../apps/web/web/LectorSuperficie.py#L111) | Sin docstring; consultar el catálogo de módulos y el código. |
| `LectorSuperficie._StlAscii` | Función/método | [128](../../apps/web/web/LectorSuperficie.py#L128) | Sin docstring; consultar el catálogo de módulos y el código. |
| `LectorSuperficie._Normales` | Función/método | [142](../../apps/web/web/LectorSuperficie.py#L142) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/PaginaComparacion.py`

Pantalla para previsualizar una ortesis o un lote de variantes.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `PaginaComparacion` | Clase | [19](../../apps/web/web/PaginaComparacion.py#L19) | Formulario con los parámetros del panel y los visores del lote. |
| `PaginaComparacion.Index` | Función/método | [23](../../apps/web/web/PaginaComparacion.py#L23) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Formulario` | Función/método | [55](../../apps/web/web/PaginaComparacion.py#L55) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Superficie` | Función/método | [134](../../apps/web/web/PaginaComparacion.py#L134) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Vista` | Función/método | [197](../../apps/web/web/PaginaComparacion.py#L197) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Lote` | Función/método | [241](../../apps/web/web/PaginaComparacion.py#L241) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Fila` | Función/método | [333](../../apps/web/web/PaginaComparacion.py#L333) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Marco` | Función/método | [364](../../apps/web/web/PaginaComparacion.py#L364) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Visor` | Función/método | [368](../../apps/web/web/PaginaComparacion.py#L368) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Enlace` | Función/método | [380](../../apps/web/web/PaginaComparacion.py#L380) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Campo` | Función/método | [387](../../apps/web/web/PaginaComparacion.py#L387) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Interruptor` | Función/método | [396](../../apps/web/web/PaginaComparacion.py#L396) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Selector` | Función/método | [405](../../apps/web/web/PaginaComparacion.py#L405) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaComparacion.Medida` | Función/método | [422](../../apps/web/web/PaginaComparacion.py#L422) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/PaginaHistorial.py`

Pantalla /historial: generaciones del usuario, comparación y restauración.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `PaginaHistorial` | Clase | [13](../../apps/web/web/PaginaHistorial.py#L13) | Filtros, tabla paginada por cursor y visores de las versiones elegidas. |
| `PaginaHistorial.Index` | Función/método | [17](../../apps/web/web/PaginaHistorial.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Filtros` | Función/método | [42](../../apps/web/web/PaginaHistorial.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Fecha` | Función/método | [75](../../apps/web/web/PaginaHistorial.py#L75) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Tabla` | Función/método | [83](../../apps/web/web/PaginaHistorial.py#L83) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Fila` | Función/método | [133](../../apps/web/web/PaginaHistorial.py#L133) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Comparacion` | Función/método | [177](../../apps/web/web/PaginaHistorial.py#L177) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial.Tarjeta` | Función/método | [196](../../apps/web/web/PaginaHistorial.py#L196) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/__init__.py`

Acceso a PostgreSQL con SQLAlchemy 2.0; el esquema se versiona con Alembic.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/persistence/ConexionPostgres.py`

Motor SQLAlchemy y sesiones por proceso.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ConexionPostgres` | Clase | [29](../../apps/web/web/persistence/ConexionPostgres.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConexionPostgres.Abrir` | Función/método | [36](../../apps/web/web/persistence/ConexionPostgres.py#L36) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConexionPostgres.Cerrar` | Función/método | [60](../../apps/web/web/persistence/ConexionPostgres.py#L60) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConexionPostgres.Abierta` | Función/método | [67](../../apps/web/web/persistence/ConexionPostgres.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConexionPostgres.Transaccion` | Función/método | [72](../../apps/web/web/persistence/ConexionPostgres.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConexionPostgres.Ejecutar` | Función/método | [88](../../apps/web/web/persistence/ConexionPostgres.py#L88) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/Contratos.py`

DTO y errores de la persistencia. No son entidades ORM.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ErrorPersistencia` | Clase | [29](../../apps/web/web/persistence/Contratos.py#L29) | Error previsto con un mensaje que se puede mostrar. |
| `PersistenciaNoDisponible` | Clase | [33](../../apps/web/web/persistence/Contratos.py#L33) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SesionInvalida` | Clase | [37](../../apps/web/web/persistence/Contratos.py#L37) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SesionInvalida.__init__` | Función/método | [38](../../apps/web/web/persistence/Contratos.py#L38) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AccesoDenegado` | Clase | [42](../../apps/web/web/persistence/Contratos.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AccesoDenegado.__init__` | Función/método | [43](../../apps/web/web/persistence/Contratos.py#L43) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SolicitudIdempotenteEnConflicto` | Clase | [47](../../apps/web/web/persistence/Contratos.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SolicitudIdempotenteEnConflicto.__init__` | Función/método | [48](../../apps/web/web/persistence/Contratos.py#L48) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConflictoRevision` | Clase | [52](../../apps/web/web/persistence/Contratos.py#L52) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConflictoRevision.__init__` | Función/método | [53](../../apps/web/web/persistence/Contratos.py#L53) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CuotaExcedida` | Clase | [57](../../apps/web/web/persistence/Contratos.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |
| `UsuarioAutenticado` | Clase | [62](../../apps/web/web/persistence/Contratos.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Asset` | Clase | [70](../../apps/web/web/persistence/Contratos.py#L70) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ImportDTO` | Clase | [84](../../apps/web/web/persistence/Contratos.py#L84) | Sin docstring; consultar el catálogo de módulos y el código. |
| `VersionDTO` | Clase | [101](../../apps/web/web/persistence/Contratos.py#L101) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SolicitudLote` | Clase | [116](../../apps/web/web/persistence/Contratos.py#L116) | Variantes ya expandidas y validadas por ``GeneradorWeb.Combinaciones``. |
| `LoteDTO` | Clase | [130](../../apps/web/web/persistence/Contratos.py#L130) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResultadoDTO` | Clase | [143](../../apps/web/web/persistence/Contratos.py#L143) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ItemLote` | Clase | [162](../../apps/web/web/persistence/Contratos.py#L162) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ProgresoLote` | Clase | [176](../../apps/web/web/persistence/Contratos.py#L176) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ProgresoLote.terminados` | Función/método | [181](../../apps/web/web/persistence/Contratos.py#L181) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ProgresoLote.abierto` | Función/método | [185](../../apps/web/web/persistence/Contratos.py#L185) | Sin docstring; consultar el catálogo de módulos y el código. |
| `TrabajoReservado` | Clase | [190](../../apps/web/web/persistence/Contratos.py#L190) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResultadoGeometrico` | Clase | [206](../../apps/web/web/persistence/Contratos.py#L206) | Sin docstring; consultar el catálogo de módulos y el código. |
| `FilaHistorial` | Clase | [224](../../apps/web/web/persistence/Contratos.py#L224) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PaginaHistorial` | Clase | [246](../../apps/web/web/persistence/Contratos.py#L246) | Sin docstring; consultar el catálogo de módulos y el código. |
| `IntentoDTO` | Clase | [252](../../apps/web/web/persistence/Contratos.py#L252) | Sin docstring; consultar el catálogo de módulos y el código. |
| `DetalleVersion` | Clase | [269](../../apps/web/web/persistence/Contratos.py#L269) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Preferencias` | Clase | [279](../../apps/web/web/persistence/Contratos.py#L279) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/Modelos.py`

Modelos declarativos de SQLAlchemy del esquema ``ortesislab``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Base` | Clase | [65](../../apps/web/web/persistence/Modelos.py#L65) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_Sha` | Función/método | [85](../../apps/web/web/persistence/Modelos.py#L85) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_Valores` | Función/método | [89](../../apps/web/web/persistence/Modelos.py#L89) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_Defecto` | Función/método | [95](../../apps/web/web/persistence/Modelos.py#L95) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_Objeto` | Función/método | [99](../../apps/web/web/persistence/Modelos.py#L99) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_Check` | Función/método | [103](../../apps/web/web/persistence/Modelos.py#L103) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Usuario` | Clase | [107](../../apps/web/web/persistence/Modelos.py#L107) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SesionAutenticacion` | Clase | [125](../../apps/web/web/persistence/Modelos.py#L125) | Sesión de servidor tras el login OIDC; la cookie solo lleva el token. |
| `PreferenciaUsuario` | Clase | [143](../../apps/web/web/persistence/Modelos.py#L143) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ArchivoAlmacenado` | Clase | [161](../../apps/web/web/persistence/Modelos.py#L161) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Proyecto` | Clase | [196](../../apps/web/web/persistence/Modelos.py#L196) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Importacion` | Clase | [224](../../apps/web/web/persistence/Modelos.py#L224) | Sin docstring; consultar el catálogo de módulos y el código. |
| `VersionModelo` | Clase | [289](../../apps/web/web/persistence/Modelos.py#L289) | Versión inmutable; el trigger ``model_versions_comprobar`` valida import y padre. |
| `LoteGeneracion` | Clase | [350](../../apps/web/web/persistence/Modelos.py#L350) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ItemLoteGeneracion` | Clase | [399](../../apps/web/web/persistence/Modelos.py#L399) | Sin docstring; consultar el catálogo de módulos y el código. |
| `IntentoGeneracion` | Clase | [468](../../apps/web/web/persistence/Modelos.py#L468) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResultadoGeneracion` | Clase | [528](../../apps/web/web/persistence/Modelos.py#L528) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Exportacion` | Clase | [576](../../apps/web/web/persistence/Modelos.py#L576) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EventoHistorial` | Clase | [606](../../apps/web/web/persistence/Modelos.py#L606) | Historial append-only: los roles de aplicación no tienen UPDATE ni DELETE. |

## `apps/web/web/persistence/repositorios/__init__.py`

Repositorios SQLAlchemy, uno por archivo. Reciben una ``Session`` ya abierta y no hacen commit.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/persistence/repositorios/Consultas.py`

Tablas y fragmentos de consulta que comparten varios repositorios.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Segundos` | Función/método | [45](../../apps/web/web/persistence/repositorios/Consultas.py#L45) | Sin docstring; consultar el catálogo de módulos y el código. |
| `UltimoError` | Función/método | [49](../../apps/web/web/persistence/repositorios/Consultas.py#L49) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConStlGanador` | Función/método | [62](../../apps/web/web/persistence/repositorios/Consultas.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ColumnasResultado` | Función/método | [81](../../apps/web/web/persistence/repositorios/Consultas.py#L81) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioAssets.py`

Filas de ``file_assets``: el contenido vive en el bucket.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioAssets` | Clase | [18](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L18) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets._Seleccion` | Función/método | [27](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L27) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.CrearStaged` | Función/método | [31](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L31) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.MarcarListo` | Función/método | [57](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.MarcarEstado` | Función/método | [67](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.Obtener` | Función/método | [75](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L75) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.ListoPorSha` | Función/método | [79](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L79) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.StagedVencidos` | Función/método | [94](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L94) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.RechazadosVencidos` | Función/método | [104](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L104) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.ListosParaComprobar` | Función/método | [123](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L123) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.PorClave` | Función/método | [130](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L130) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.ClavesRegistradas` | Función/método | [134](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L134) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.BytesUsuarioReady` | Función/método | [139](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L139) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioAssets.MarcarExportsFaltantes` | Función/método | [150](../../apps/web/web/persistence/repositorios/RepositorioAssets.py#L150) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioBase.py`

Clase padre de los repositorios: lectura de filas y conversión a DTO.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioBase` | Clase | [19](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Uno` | Función/método | [24](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L24) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Todos` | Función/método | [29](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Construir` | Función/método | [33](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L33) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Dto` | Función/método | [38](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L38) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Seleccion` | Función/método | [42](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Opcional` | Función/método | [46](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._Lista` | Función/método | [51](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioBase._DelUsuario` | Función/método | [55](../../apps/web/web/persistence/repositorios/RepositorioBase.py#L55) | Fila del usuario que cumple ``condiciones``; un recurso ajeno o inexistente lanza ``AccesoDenegado``. |

## `apps/web/web/persistence/repositorios/RepositorioHistorial.py`

Eventos de historial y listado de ejecuciones por versión.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioHistorial` | Clase | [26](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioHistorial.PurgarAntiguos` | Función/método | [30](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py#L30) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioHistorial.Evento` | Función/método | [36](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py#L36) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioHistorial.Listar` | Función/método | [62](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioHistorial.EventosDeVersion` | Función/método | [140](../../apps/web/web/persistence/repositorios/RepositorioHistorial.py#L140) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioImports.py`

Importaciones de superficies: original recibido y NPZ normalizado.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioImports` | Clase | [17](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.Crear` | Función/método | [22](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L22) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.MarcarListo` | Función/método | [47](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.MarcarRechazado` | Función/método | [70](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L70) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.Obtener` | Función/método | [78](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L78) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.ListoPorNormalizado` | Función/método | [82](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L82) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.ListoPorOriginal` | Función/método | [96](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L96) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.ContarReady` | Función/método | [126](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L126) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioImports.ContarSubidasRecientes` | Función/método | [136](../../apps/web/web/persistence/repositorios/RepositorioImports.py#L136) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioLotes.py`

Lotes, ítems y cola del trabajador: admisión, reserva, lease y cierre.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioLotes` | Clase | [32](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L32) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes._ClaveBloqueo` | Función/método | [37](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L37) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.BloquearUsuario` | Función/método | [41](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.IntentarBloquearUsuario` | Función/método | [46](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.PorRequest` | Función/método | [52](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L52) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.ContarPendientes` | Función/método | [56](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.InsertarLote` | Función/método | [66](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L66) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.InsertarItem` | Función/método | [91](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L91) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Obtener` | Función/método | [109](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L109) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Ultimo` | Función/método | [113](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L113) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Items` | Función/método | [123](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L123) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.SolicitarCancelacion` | Función/método | [150](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L150) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Recalcular` | Función/método | [171](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L171) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes._Candidato` | Función/método | [220](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L220) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.ReservarPendiente` | Función/método | [246](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L246) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes._ItemVigente` | Función/método | [343](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L343) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.RenovarLease` | Función/método | [352](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L352) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.BloquearVigente` | Función/método | [368](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L368) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.CancelacionPedida` | Función/método | [375](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L375) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.CerrarIntento` | Función/método | [382](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L382) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Exito` | Función/método | [410](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L410) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Liberar` | Función/método | [441](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L441) | Saca el ítem de ``running``: a la cola, cancelado o fallido. |
| `RepositorioLotes.AbandonarIntento` | Función/método | [467](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L467) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes.Vencidos` | Función/método | [486](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L486) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioLotes._Item` | Función/método | [506](../../apps/web/web/persistence/repositorios/RepositorioLotes.py#L506) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioPreferencias.py`

Preferencias por usuario con control optimista de revisión.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioPreferencias` | Clase | [15](../../apps/web/web/persistence/repositorios/RepositorioPreferencias.py#L15) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioPreferencias.Obtener` | Función/método | [20](../../apps/web/web/persistence/repositorios/RepositorioPreferencias.py#L20) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioPreferencias.Guardar` | Función/método | [29](../../apps/web/web/persistence/repositorios/RepositorioPreferencias.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioProyectos.py`

Proyectos del usuario; cada cuenta tiene uno predeterminado.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioProyectos` | Clase | [15](../../apps/web/web/persistence/repositorios/RepositorioProyectos.py#L15) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioProyectos.Predeterminado` | Función/método | [17](../../apps/web/web/persistence/repositorios/RepositorioProyectos.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioProyectos.Crear` | Función/método | [33](../../apps/web/web/persistence/repositorios/RepositorioProyectos.py#L33) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioProyectos.PorNombre` | Función/método | [41](../../apps/web/web/persistence/repositorios/RepositorioProyectos.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioResultados.py`

Resultados geométricos, intentos de una versión y exports STL.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioResultados` | Clase | [18](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L18) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.Insertar` | Función/método | [22](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L22) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.InsertarExport` | Función/método | [46](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.Dto` | Función/método | [62](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados._Dto` | Función/método | [83](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L83) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.Intentos` | Función/método | [87](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L87) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.DeVersion` | Función/método | [102](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L102) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioResultados.ExportStl` | Función/método | [127](../../apps/web/web/persistence/repositorios/RepositorioResultados.py#L127) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioUsuarios.py`

Cuentas creadas desde OIDC y sus sesiones de servidor.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioUsuarios` | Clase | [18](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L18) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.Upsert` | Función/método | [22](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L22) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.Estado` | Función/método | [41](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.CrearSesion` | Función/método | [45](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L45) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.ResolverSesion` | Función/método | [51](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.PurgarSesionesVencidas` | Función/método | [65](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L65) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioUsuarios.RevocarSesion` | Función/método | [78](../../apps/web/web/persistence/repositorios/RepositorioUsuarios.py#L78) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/persistence/repositorios/RepositorioVersiones.py`

Versiones inmutables numeradas por proyecto.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RepositorioVersiones` | Clase | [16](../../apps/web/web/persistence/repositorios/RepositorioVersiones.py#L16) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioVersiones.ReservarNumeros` | Función/método | [21](../../apps/web/web/persistence/repositorios/RepositorioVersiones.py#L21) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioVersiones.Insertar` | Función/método | [35](../../apps/web/web/persistence/repositorios/RepositorioVersiones.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RepositorioVersiones.Obtener` | Función/método | [68](../../apps/web/web/persistence/repositorios/RepositorioVersiones.py#L68) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/__init__.py`

Marcador de paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/services/AutenticacionOidc.py`

Rutas OIDC del backend: /auth/login, /auth/callback y /auth/logout.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `AutenticacionOidc` | Clase | [27](../../apps/web/web/services/AutenticacionOidc.py#L27) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AutenticacionOidc.Aplicacion` | Función/método | [29](../../apps/web/web/services/AutenticacionOidc.py#L29) | Aplicación raíz que Reflex usa como transformador; monta /auth. |
| `AutenticacionOidc.Aplicacion.login` | Función/método | [41](../../apps/web/web/services/AutenticacionOidc.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AutenticacionOidc.Aplicacion.callback` | Función/método | [44](../../apps/web/web/services/AutenticacionOidc.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AutenticacionOidc.Aplicacion.logout` | Función/método | [72](../../apps/web/web/services/AutenticacionOidc.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AutenticacionOidc.Aplicacion.logout_get` | Función/método | [81](../../apps/web/web/services/AutenticacionOidc.py#L81) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/ContextoUsuario.py`

Principal autenticado de cada operación.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ContextoUsuario` | Clase | [30](../../apps/web/web/services/ContextoUsuario.py#L30) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.Hash` | Función/método | [32](../../apps/web/web/services/ContextoUsuario.py#L32) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.TokenDeCookie` | Función/método | [36](../../apps/web/web/services/ContextoUsuario.py#L36) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.Requerir` | Función/método | [48](../../apps/web/web/services/ContextoUsuario.py#L48) | Entrada: cabecera Cookie. Proceso: resuelve la sesión vigente y el |
| `ContextoUsuario.Requerir.resolver` | Función/método | [57](../../apps/web/web/services/ContextoUsuario.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.IniciarSesion` | Función/método | [67](../../apps/web/web/services/ContextoUsuario.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.IniciarSesion.crear` | Función/método | [72](../../apps/web/web/services/ContextoUsuario.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.CerrarSesion` | Función/método | [84](../../apps/web/web/services/ContextoUsuario.py#L84) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.Activar` | Función/método | [92](../../apps/web/web/services/ContextoUsuario.py#L92) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ContextoUsuario.Actual` | Función/método | [101](../../apps/web/web/services/ContextoUsuario.py#L101) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/GeneradorGeometrico.py`

Construcción numérica de una versión: métricas, STL y JSON de parámetros.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `GeneradorGeometrico` | Clase | [26](../../apps/web/web/services/GeneradorGeometrico.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorGeometrico.MaterialDe` | Función/método | [28](../../apps/web/web/services/GeneradorGeometrico.py#L28) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorGeometrico.Construir` | Función/método | [39](../../apps/web/web/services/GeneradorGeometrico.py#L39) | Salida: resultado numérico, STL binario y JSON canónico de parámetros. |

## `apps/web/web/services/ServicioHistorial.py`

Historial por usuario: listado paginado, detalle, restauración y reintento.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ServicioHistorial` | Clase | [40](../../apps/web/web/services/ServicioHistorial.py#L40) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.CodificarCursor` | Función/método | [42](../../apps/web/web/services/ServicioHistorial.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.DecodificarCursor` | Función/método | [47](../../apps/web/web/services/ServicioHistorial.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.Listar` | Función/método | [55](../../apps/web/web/services/ServicioHistorial.py#L55) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.Detalle` | Función/método | [79](../../apps/web/web/services/ServicioHistorial.py#L79) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.Detalle.leer` | Función/método | [80](../../apps/web/web/services/ServicioHistorial.py#L80) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.Comparar` | Función/método | [98](../../apps/web/web/services/ServicioHistorial.py#L98) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioHistorial.Restaurar` | Función/método | [104](../../apps/web/web/services/ServicioHistorial.py#L104) | Crea una versión nueva con los parámetros de otra; no modifica la original. |
| `ServicioHistorial.Reintentar` | Función/método | [123](../../apps/web/web/services/ServicioHistorial.py#L123) | Nuevo lote ``retry`` sobre versiones existentes: nuevos intentos, mismas versiones. |
| `ServicioHistorial.RegistrarDescarga` | Función/método | [144](../../apps/web/web/services/ServicioHistorial.py#L144) | Devuelve la object_url del STL del usuario y registra la descarga. |
| `ServicioHistorial.RegistrarDescarga.registrar` | Función/método | [147](../../apps/web/web/services/ServicioHistorial.py#L147) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/ServicioImports.py`

Importación de superficies: original y NPZ normalizado en el bucket.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ServicioImports` | Clase | [47](../../apps/web/web/services/ServicioImports.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.NombreSuperficie` | Función/método | [49](../../apps/web/web/services/ServicioImports.py#L49) | Identificador que la página guarda en ``superficie_archivo``. |
| `ServicioImports.AssetDeNombre` | Función/método | [54](../../apps/web/web/services/ServicioImports.py#L54) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.TuplaANpz` | Función/método | [66](../../apps/web/web/services/ServicioImports.py#L66) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.NpzATupla` | Función/método | [73](../../apps/web/web/services/ServicioImports.py#L73) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.PrepararPlantilla` | Función/método | [86](../../apps/web/web/services/ServicioImports.py#L86) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.Importar` | Función/método | [96](../../apps/web/web/services/ServicioImports.py#L96) | Entrada: archivo subido. Proceso: lo guarda y normaliza. Salida: import |
| `ServicioImports.Importar.normalizar` | Función/método | [118](../../apps/web/web/services/ServicioImports.py#L118) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports.AsegurarPlantilla` | Función/método | [126](../../apps/web/web/services/ServicioImports.py#L126) | La plantilla incluida pasa a ser un import del proyecto del usuario. |
| `ServicioImports.Resolver` | Función/método | [135](../../apps/web/web/services/ServicioImports.py#L135) | ``""`` es la plantilla; otro valor es el NPZ de un import del usuario. |
| `ServicioImports.Info` | Función/método | [148](../../apps/web/web/services/ServicioImports.py#L148) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports._Registrar` | Función/método | [158](../../apps/web/web/services/ServicioImports.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports._Registrar.admitir` | Función/método | [174](../../apps/web/web/services/ServicioImports.py#L174) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioImports._Registrar.rechazar_fallo` | Función/método | [206](../../apps/web/web/services/ServicioImports.py#L206) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/ServicioLotes.py`

Admisión de lotes, progreso y transiciones del trabajador.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ServicioLotes` | Clase | [46](../../apps/web/web/services/ServicioLotes.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.HuellaSolicitud` | Función/método | [48](../../apps/web/web/services/ServicioLotes.py#L48) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Solicitar` | Función/método | [61](../../apps/web/web/services/ServicioLotes.py#L61) | Entrada: variantes ya validadas. Proceso: crea versiones, lote e ítems |
| `ServicioLotes.Solicitar.admitir` | Función/método | [72](../../apps/web/web/services/ServicioLotes.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Progreso` | Función/método | [113](../../apps/web/web/services/ServicioLotes.py#L113) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Progreso.leer` | Función/método | [114](../../apps/web/web/services/ServicioLotes.py#L114) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Ultimo` | Función/método | [121](../../apps/web/web/services/ServicioLotes.py#L121) | Último lote del usuario: la página lo recupera al recargar o reiniciar. |
| `ServicioLotes.Ultimo.leer` | Función/método | [124](../../apps/web/web/services/ServicioLotes.py#L124) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Esperar` | Función/método | [133](../../apps/web/web/services/ServicioLotes.py#L133) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Cancelar` | Función/método | [144](../../apps/web/web/services/ServicioLotes.py#L144) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Cancelar.cancelar` | Función/método | [145](../../apps/web/web/services/ServicioLotes.py#L145) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Reservar` | Función/método | [158](../../apps/web/web/services/ServicioLotes.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Renovar` | Función/método | [164](../../apps/web/web/services/ServicioLotes.py#L164) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.CancelacionPedida` | Función/método | [168](../../apps/web/web/services/ServicioLotes.py#L168) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.RegistrarSalidas` | Función/método | [172](../../apps/web/web/services/ServicioLotes.py#L172) | Filas ``staged`` de los objetos que el trabajador va a subir: |
| `ServicioLotes.RegistrarSalidas.registrar` | Función/método | [176](../../apps/web/web/services/ServicioLotes.py#L176) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Confirmar` | Función/método | [183](../../apps/web/web/services/ServicioLotes.py#L183) | Publica resultado y exports si el lease sigue vigente. Devuelve False |
| `ServicioLotes.Confirmar.confirmar` | Función/método | [193](../../apps/web/web/services/ServicioLotes.py#L193) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Fallar` | Función/método | [222](../../apps/web/web/services/ServicioLotes.py#L222) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.Fallar.fallar` | Función/método | [223](../../apps/web/web/services/ServicioLotes.py#L223) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.CerrarCancelado` | Función/método | [240](../../apps/web/web/services/ServicioLotes.py#L240) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.CerrarCancelado.cerrar` | Función/método | [241](../../apps/web/web/services/ServicioLotes.py#L241) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioLotes.AbandonarVencidos` | Función/método | [251](../../apps/web/web/services/ServicioLotes.py#L251) | Devuelve a la cola los ítems cuyo trabajador dejó de renovar el lease. |
| `ServicioLotes.AbandonarVencidos.abandonar` | Función/método | [254](../../apps/web/web/services/ServicioLotes.py#L254) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/ServicioPreferencias.py`

Preferencias por usuario con control optimista de revisión.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ServicioPreferencias` | Clase | [10](../../apps/web/web/services/ServicioPreferencias.py#L10) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioPreferencias.Obtener` | Función/método | [12](../../apps/web/web/services/ServicioPreferencias.py#L12) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/services/ServicioVersiones.py`

Versiones inmutables: snapshot de parámetros, material y escala.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ServicioVersiones` | Clase | [22](../../apps/web/web/services/ServicioVersiones.py#L22) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioVersiones.Canonico` | Función/método | [24](../../apps/web/web/services/ServicioVersiones.py#L24) | JSON estable para hashes: claves ordenadas, sin espacios, sin NaN. |
| `ServicioVersiones.Sha` | Función/método | [29](../../apps/web/web/services/ServicioVersiones.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioVersiones.Material` | Función/método | [33](../../apps/web/web/services/ServicioVersiones.py#L33) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioVersiones.Parametros` | Función/método | [46](../../apps/web/web/services/ServicioVersiones.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ServicioVersiones.Insertar` | Función/método | [56](../../apps/web/web/services/ServicioVersiones.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/Sesion.py`

Barra de sesión común a la comparación y al historial.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Sesion` | Clase | [8](../../apps/web/web/Sesion.py#L8) | Enlaces a las rutas OIDC del backend y navegación entre páginas. |
| `Sesion.Ruta` | Función/método | [12](../../apps/web/web/Sesion.py#L12) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Sesion.Boton` | Función/método | [17](../../apps/web/web/Sesion.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Sesion.FormularioPost` | Función/método | [23](../../apps/web/web/Sesion.py#L23) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Sesion.Barra` | Función/método | [32](../../apps/web/web/Sesion.py#L32) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/storage/__init__.py`

Marcador de paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/web/web/storage/AlmacenamientoPrivado.py`

Contrato del almacén de bytes y claves de objeto.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `AlmacenamientoNoDisponible` | Clase | [25](../../apps/web/web/storage/AlmacenamientoPrivado.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoNoDisponible.__init__` | Función/método | [26](../../apps/web/web/storage/AlmacenamientoPrivado.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ObjetoAusente` | Clase | [30](../../apps/web/web/storage/AlmacenamientoPrivado.py#L30) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ObjetoAusente.__init__` | Función/método | [31](../../apps/web/web/storage/AlmacenamientoPrivado.py#L31) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado` | Clase | [35](../../apps/web/web/storage/AlmacenamientoPrivado.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado.Url` | Función/método | [36](../../apps/web/web/storage/AlmacenamientoPrivado.py#L36) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado.Publicar` | Función/método | [38](../../apps/web/web/storage/AlmacenamientoPrivado.py#L38) | Sube el objeto completo, comprueba tamaño y hash, y devuelve su URL. |
| `AlmacenamientoPrivado.Leer` | Función/método | [42](../../apps/web/web/storage/AlmacenamientoPrivado.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado.Existe` | Función/método | [44](../../apps/web/web/storage/AlmacenamientoPrivado.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado.Borrar` | Función/método | [46](../../apps/web/web/storage/AlmacenamientoPrivado.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AlmacenamientoPrivado.Claves` | Función/método | [48](../../apps/web/web/storage/AlmacenamientoPrivado.py#L48) | Clave y fecha de última modificación de cada objeto bajo el prefijo. |
| `Almacen` | Clase | [53](../../apps/web/web/storage/AlmacenamientoPrivado.py#L53) | Instancia de proceso. Las pruebas la sustituyen con ``Usar``. |
| `Almacen.Actual` | Función/método | [59](../../apps/web/web/storage/AlmacenamientoPrivado.py#L59) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Almacen.Usar` | Función/método | [67](../../apps/web/web/storage/AlmacenamientoPrivado.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Almacen.Clave` | Función/método | [71](../../apps/web/web/storage/AlmacenamientoPrivado.py#L71) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Almacen.Sha256` | Función/método | [76](../../apps/web/web/storage/AlmacenamientoPrivado.py#L76) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Almacen.LeerVerificado` | Función/método | [80](../../apps/web/web/storage/AlmacenamientoPrivado.py#L80) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/web/web/storage/StorageS3.py`

Almacén de bytes en un bucket S3 (MinIO en desarrollo).

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `StorageS3` | Clase | [25](../../apps/web/web/storage/StorageS3.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.__init__` | Función/método | [26](../../apps/web/web/storage/StorageS3.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.DesdeAjustes` | Función/método | [45](../../apps/web/web/storage/StorageS3.py#L45) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Url` | Función/método | [56](../../apps/web/web/storage/StorageS3.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Publicar` | Función/método | [59](../../apps/web/web/storage/StorageS3.py#L59) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Leer` | Función/método | [72](../../apps/web/web/storage/StorageS3.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Existe` | Función/método | [83](../../apps/web/web/storage/StorageS3.py#L83) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Borrar` | Función/método | [94](../../apps/web/web/storage/StorageS3.py#L94) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StorageS3.Claves` | Función/método | [100](../../apps/web/web/storage/StorageS3.py#L100) | Sin docstring; consultar el catálogo de módulos y el código. |

## `scripts/BaseLocal.py`

Infraestructura local: arranque, parada, estado, respaldo y reinicio de la base.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `_variable` | Función/método | [24](../../scripts/BaseLocal.py#L24) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_compose` | Función/método | [29](../../scripts/BaseLocal.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_correr` | Función/método | [41](../../scripts/BaseLocal.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_accion` | Función/método | [47](../../scripts/BaseLocal.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_archivo` | Función/método | [54](../../scripts/BaseLocal.py#L54) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_exigir_desarrollo` | Función/método | [63](../../scripts/BaseLocal.py#L63) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_confirmar` | Función/método | [70](../../scripts/BaseLocal.py#L70) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_base` | Función/método | [75](../../scripts/BaseLocal.py#L75) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_bucket` | Función/método | [79](../../scripts/BaseLocal.py#L79) | Sin docstring; consultar el catálogo de módulos y el código. |
| `_salud` | Función/método | [83](../../scripts/BaseLocal.py#L83) | Sin docstring; consultar el catálogo de módulos y el código. |
| `up` | Función/método | [97](../../scripts/BaseLocal.py#L97) | Sin docstring; consultar el catálogo de módulos y el código. |
| `down` | Función/método | [105](../../scripts/BaseLocal.py#L105) | Sin docstring; consultar el catálogo de módulos y el código. |
| `estado` | Función/método | [118](../../scripts/BaseLocal.py#L118) | Sin docstring; consultar el catálogo de módulos y el código. |
| `respaldo` | Función/método | [129](../../scripts/BaseLocal.py#L129) | Sin docstring; consultar el catálogo de módulos y el código. |
| `reset` | Función/método | [161](../../scripts/BaseLocal.py#L161) | Sin docstring; consultar el catálogo de módulos y el código. |
| `comprobar` | Función/método | [176](../../scripts/BaseLocal.py#L176) | Sin docstring; consultar el catálogo de módulos y el código. |
| `main` | Función/método | [222](../../scripts/BaseLocal.py#L222) | Sin docstring; consultar el catálogo de módulos y el código. |

## `scripts/EjecutarOrtesisLab.py`

Script para abrir el complemento dentro de Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `scripts/EjecutarTrabajador.py`

Proceso trabajador de OrtesisLab: cola de generación y conciliación.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `main` | Función/método | [27](../../scripts/EjecutarTrabajador.py#L27) | Sin docstring; consultar el catálogo de módulos y el código. |

## `scripts/EmpaquetarBlender.py`

Genera el ZIP instalable de Blender, sin Reflex, logs ni la base v5.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `empaquetar` | Función/método | [11](../../scripts/EmpaquetarBlender.py#L11) | Sin docstring; consultar el catálogo de módulos y el código. |

## `scripts/IniciarConsola.py`

Script del comando de consola del proyecto.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `IniciarConsola` | Clase | [15](../../scripts/IniciarConsola.py#L15) | Sin docstring; consultar el catálogo de módulos y el código. |
| `IniciarConsola.Ejecutar` | Función/método | [17](../../scripts/IniciarConsola.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |

## `scripts/MigrarSubidas.py`

Traslada una sola vez ``uploaded_files/`` al bucket y registra cada objeto.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Propietario` | Función/método | [45](../../scripts/MigrarSubidas.py#L45) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Propietario.asegurar` | Función/método | [46](../../scripts/MigrarSubidas.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Migrar` | Función/método | [56](../../scripts/MigrarSubidas.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Migrar.registrar` | Función/método | [85](../../scripts/MigrarSubidas.py#L85) | Sin docstring; consultar el catálogo de módulos y el código. |
| `main` | Función/método | [103](../../scripts/MigrarSubidas.py#L103) | Sin docstring; consultar el catálogo de módulos y el código. |
