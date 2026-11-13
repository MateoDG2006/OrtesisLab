# Índice de símbolos: BlenderPlugin

> Generado por `python docs/Agents/Scripts/GenerarIndices.py`. No editar a mano.

Incluye funciones anidadas y métodos privados para localizar todas las piezas. Las líneas son una ayuda de navegación; el nombre del símbolo es la referencia estable.

## `apps/ortesis-plugin/OrtesisLabPlugin/__init__.py`

Paquete del complemento de Blender y del núcleo de geometría.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `register` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/__init__.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `unregister` | Función/método | [25](../../apps/ortesis-plugin/OrtesisLabPlugin/__init__.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/ApiBlender.py`

API de Blender, separada del núcleo geométrico.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py`

Recorte de celdas y cascarón de espesor variable.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Cascaron` | Clase | [15](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L15) | Pasa de una superficie abierta a un sólido de espesor conocido. |
| `Cascaron.Smooth01` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Cascaron.Recortar` | Función/método | [25](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Cascaron.Recortar.verticeOriginal` | Función/método | [49](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L49) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Cascaron.Recortar.cruce` | Función/método | [57](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Cascaron.Engrosar` | Función/método | [103](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L103) | Añade espesor a las caras existentes; nunca rellena una abertura. |
| `Cascaron.VolumenMm3` | Función/método | [158](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/consola.py`

Punto de entrada de consola ``ortesislab``.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `main` | Función/método | [6](../../apps/ortesis-plugin/OrtesisLabPlugin/consola.py#L6) | Inicia el saludo de consola del proyecto. |

## `apps/ortesis-plugin/OrtesisLabPlugin/constants/__init__.py`

Constantes de OrtesisLab: nombres, patrones, materiales y límites.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py`

Materiales de impresión.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Material` | Clase | [16](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L16) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Material.__init__` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Material.Gramos` | Función/método | [47](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Material.Costo` | Función/método | [57](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PETG` | Clase | [62](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L62) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PETG.__init__` | Función/método | [63](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py#L63) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/constants/Nombres.py`

Nombres estables de objetos, atributos y archivos.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py`

Patrones de nervadura.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Patron` | Clase | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L19) | Distancia al eje de la nervadura, y si el patrón tiene celosía o semilla. |
| `Patron.__init__` | Función/método | [26](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L26) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.Distancia` | Función/método | [29](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.RotarXy` | Función/método | [34](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L34) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.DistanciaCuadricula` | Función/método | [41](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L41) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.DistanciaSemillas` | Función/método | [46](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L46) | Entrada: puntos XY y celda en mm. Proceso: evalúa semillas próximas |
| `Patron._DistanciaPlanos` | Función/método | [102](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L102) | Entrada: puntos y semillas XY. Proceso: calcula la bisectriz más |
| `Patron.Geometricos` | Función/método | [117](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L117) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.Obtener` | Función/método | [128](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L128) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.Celosia` | Función/método | [142](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L142) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Patron.PideSemilla` | Función/método | [149](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L149) | Sin docstring; consultar el catálogo de módulos y el código. |
| `HoneyComb` | Clase | [154](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L154) | Sin docstring; consultar el catálogo de módulos y el código. |
| `HoneyComb.__init__` | Función/método | [158](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |
| `HoneyComb.Distancia` | Función/método | [162](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L162) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Square` | Clase | [166](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L166) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Square.__init__` | Función/método | [169](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L169) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Square.Distancia` | Función/método | [173](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L173) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Diamond` | Clase | [177](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L177) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Diamond.__init__` | Función/método | [180](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L180) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Diamond.Distancia` | Función/método | [184](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L184) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Voronoi` | Clase | [192](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L192) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Voronoi.__init__` | Función/método | [196](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L196) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Voronoi.Distancia` | Función/método | [200](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L200) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Solid` | Clase | [204](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L204) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Solid.__init__` | Función/método | [208](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L208) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Solid.Distancia` | Función/método | [212](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py#L212) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/contratos.py`

Contratos compartidos entre núcleo, Blender y la web.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ValidarTuplaSuperficie` | Función/método | [12](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py#L12) | Entrada: (vértices, caras, normales, borde). |
| `ValidarOpciones` | Función/método | [28](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py#L28) | Opciones de generación: claves reconocidas y tipos básicos. |
| `ValidarFicha` | Función/método | [38](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py#L38) | Ficha visible en la página de comparación. |
| `ValidarInformeValidacion` | Función/método | [45](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py#L45) | Informe geométrico homogéneo entre web y Blender. |
| `ValidarSidecarStl` | Función/método | [60](../../apps/ortesis-plugin/OrtesisLabPlugin/contratos.py#L60) | JSON hermano de un STL exportado desde Blender. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py`

Errores de OrtesisLab.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `OrtesisLabError` | Clase | [10](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L10) | Base de los errores previstos del generador. |
| `OrtesisLabError.__init__` | Función/método | [13](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L13) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ConfiguracionInvalida` | Clase | [27](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L27) | Un archivo de ``config`` falta, no es JSON o no tiene las claves exigidas. |
| `EntornoBlenderRequerido` | Clase | [31](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L31) | El módulo usa la API de Blender y se importó fuera de Blender. |
| `ArchivoSuperficieNoEncontrado` | Clase | [35](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ArchivoSuperficieNoEncontrado.__init__` | Función/método | [36](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L36) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ArchivoSuperficieIlegible` | Clase | [43](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L43) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ArchivoSuperficieIlegible.__init__` | Función/método | [44](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieNoEsMalla` | Clase | [51](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieNoEsMalla.__init__` | Función/método | [52](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L52) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieInvalida` | Clase | [56](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L56) | La base no es una superficie conectada y orientada de una sola capa. |
| `ModificadoresSinAplicar` | Clase | [60](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L60) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModificadoresSinAplicar.__init__` | Función/método | [61](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L61) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EscalaSinAplicar` | Clase | [68](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L68) | Sin docstring; consultar el catálogo de módulos y el código. |
| `EscalaSinAplicar.__init__` | Función/método | [69](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L69) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieSinCaras` | Clase | [76](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L76) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieSinCaras.__init__` | Función/método | [77](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L77) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SolidoCerrado` | Clase | [81](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L81) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SolidoCerrado.__init__` | Función/método | [82](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L82) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AristasNoManifold` | Clase | [89](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L89) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AristasNoManifold.__init__` | Función/método | [90](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L90) | Sin docstring; consultar el catálogo de módulos y el código. |
| `VerticesSueltos` | Clase | [94](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L94) | Sin docstring; consultar el catálogo de módulos y el código. |
| `VerticesSueltos.__init__` | Función/método | [95](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L95) | Sin docstring; consultar el catálogo de módulos y el código. |
| `NormalesInvalidas` | Clase | [99](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L99) | Sin docstring; consultar el catálogo de módulos y el código. |
| `NormalesInvalidas.__init__` | Función/método | [100](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L100) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametrosNoReconocidos` | Clase | [104](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L104) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametrosNoReconocidos.__init__` | Función/método | [105](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L105) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametroNoPositivo` | Clase | [110](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L110) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametroNoPositivo.__init__` | Función/método | [111](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L111) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PatronNoReconocido` | Clase | [115](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L115) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PatronNoReconocido.__init__` | Función/método | [116](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L116) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PatronNoImplementado` | Clase | [120](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L120) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PatronNoImplementado.__init__` | Función/método | [121](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L121) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CeldaDemasiadoPequena` | Clase | [128](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L128) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CeldaDemasiadoPequena.__init__` | Función/método | [129](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L129) | Sin docstring; consultar el catálogo de módulos y el código. |
| `NervaduraDemasiadoAncha` | Clase | [135](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L135) | Sin docstring; consultar el catálogo de módulos y el código. |
| `NervaduraDemasiadoAncha.__init__` | Función/método | [136](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L136) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametroNoFinito` | Clase | [142](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L142) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ParametroNoFinito.__init__` | Función/método | [143](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L143) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResolucionNoPositiva` | Clase | [147](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L147) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResolucionNoPositiva.__init__` | Función/método | [148](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L148) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SemillaInvalida` | Clase | [152](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L152) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SemillaInvalida.__init__` | Función/método | [153](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L153) | Sin docstring; consultar el catálogo de módulos y el código. |
| `BordeNegativo` | Clase | [157](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L157) | Sin docstring; consultar el catálogo de módulos y el código. |
| `BordeNegativo.__init__` | Función/método | [158](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L158) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieEliminadaPorPatron` | Clase | [165](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L165) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieEliminadaPorPatron.__init__` | Función/método | [166](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L166) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResolucionDemasiadoFina` | Clase | [170](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L170) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ResolucionDemasiadoFina.__init__` | Función/método | [171](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L171) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeometriaFragmentada` | Clase | [178](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L178) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeometriaFragmentada.__init__` | Función/método | [179](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L179) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeometriaInconsistente` | Clase | [187](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L187) | Los arreglos internos no coinciden entre sí. Indica un fallo del generador. |
| `MallaNoConstruida` | Clase | [191](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L191) | Sin docstring; consultar el catálogo de módulos y el código. |
| `MallaNoConstruida.__init__` | Función/método | [192](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L192) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReconstruccionFallida` | Clase | [196](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L196) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReconstruccionFallida.__init__` | Función/método | [197](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L197) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModeloNoGenerado` | Clase | [204](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L204) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModeloNoGenerado.__init__` | Función/método | [205](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L205) | Sin docstring; consultar el catálogo de módulos y el código. |
| `MallaNoValida` | Clase | [209](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L209) | Sin docstring; consultar el catálogo de módulos y el código. |
| `MallaNoValida.__init__` | Función/método | [210](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L210) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ExportacionFallida` | Clase | [216](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L216) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ExportacionFallida.__init__` | Función/método | [217](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L217) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModeloSinGeometria` | Clase | [224](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L224) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ModeloSinGeometria.__init__` | Función/método | [225](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L225) | Sin docstring; consultar el catálogo de módulos y el código. |
| `MaterialInvalido` | Clase | [229](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L229) | Densidad, precio o volumen incompatibles con el cálculo de material. |
| `CalidadInsuficiente` | Clase | [233](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L233) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CalidadInsuficiente.__init__` | Función/método | [234](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L234) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PresupuestoExcedido` | Clase | [238](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L238) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PresupuestoExcedido.__init__` | Función/método | [239](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L239) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneracionCancelada` | Clase | [243](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L243) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneracionCancelada.__init__` | Función/método | [244](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L244) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CoordenadasFueraDeFloat32` | Clase | [248](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L248) | Sin docstring; consultar el catálogo de módulos y el código. |
| `CoordenadasFueraDeFloat32.__init__` | Función/método | [249](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py#L249) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py`

Exporta el STL en milímetros y un JSON con parámetros y comprobación.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ExportadorStl` | Clase | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py#L19) | Escribe el STL solo si la malla pasó la comprobación. |
| `ExportadorStl._ValidarMetadatos` | Función/método | [23](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py#L23) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ExportadorStl._EscribirStl` | Función/método | [38](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py#L38) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ExportadorStl.Exportar` | Función/método | [47](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py`

Inspección de cabeceras NPY dentro de un NPZ, sin materializar arrays grandes.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `InspeccionNpz` | Clase | [20](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py#L20) | Rechaza un NPZ cuya cabecera declare más bytes de los que el ZIP contiene. |
| `InspeccionNpz.CabeceraNpy` | Función/método | [24](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py#L24) | Entrada: bytes de un miembro ``.npy``. Proceso: lee solo la cabecera. |
| `InspeccionNpz.VerificarContenido` | Función/método | [63](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py#L63) | Entrada: bytes NPZ y tope descomprimido. Proceso: suma tamaños ZIP e |
| `InspeccionNpz.VerificarPresupuesto` | Función/método | [89](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py#L89) | Entrada: vértices y caras ya materializados. Proceso: compara conteos |
| `PathStem` | Función/método | [105](../../apps/ortesis-plugin/OrtesisLabPlugin/InspeccionNpz.py#L105) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py`

Instantánea evaluada de mallas Blender y publicación atómica de archivos.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `MallaEvaluada` | Clase | [11](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L11) | Instantánea de la malla con modificadores y transformación aplicados. |
| `MallaEvaluada.Extraer` | Función/método | [15](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L15) | Entrada: objeto Blender. Salida: vértices world-space y caras triangulares. |
| `PublicacionArchivos` | Clase | [42](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L42) | Publicación atómica del par STL + JSON desde archivos temporales. |
| `PublicacionArchivos.RutasTemporales` | Función/método | [46](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PublicacionArchivos.Confirmar` | Función/método | [51](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PublicacionArchivos.Descartar` | Función/método | [57](../../apps/ortesis-plugin/OrtesisLabPlugin/InstantaneaExportacion.py#L57) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py`

Panel N y operadores de OrtesisLab en la vista 3D.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `PanelAyuda` | Clase | [31](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L31) | Lee los controles del panel y muestra los errores en la interfaz. |
| `PanelAyuda.OpcionesDesdeAjustes` | Función/método | [35](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L35) | Sin docstring; consultar el catálogo de módulos y el código. |
| `PanelAyuda.Cancelar` | Función/método | [45](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L45) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_Settings` | Clase | [55](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L55) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_generate` | Clase | [101](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L101) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_generate.execute` | Función/método | [107](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L107) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_use_surface` | Clase | [123](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L123) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_use_surface.execute` | Función/método | [128](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L128) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_repair_surface` | Clase | [140](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L140) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_repair_surface.poll` | Función/método | [151](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L151) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_repair_surface.execute` | Función/método | [155](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L155) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_validate` | Clase | [172](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L172) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_validate.execute` | Función/método | [177](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L177) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_export` | Clase | [191](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L191) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_export.invoke` | Función/método | [198](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L198) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_OT_export.execute` | Función/método | [203](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L203) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_PT_panel` | Clase | [216](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L216) | Sin docstring; consultar el catálogo de módulos y el código. |
| `OL_PT_panel.draw` | Función/método | [224](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py#L224) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Malla.py`

Análisis de la superficie abierta, sin Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `AnalizadorMalla` | Clase | [24](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L24) | Comprueba que la base sea una superficie abierta y mide el borde. |
| `AnalizadorMalla.NormalesDeCaras` | Función/método | [28](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L28) | Entrada: vértices y triángulos orientados. Proceso: promedia normales |
| `AnalizadorMalla.Preparar` | Función/método | [47](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AnalizadorMalla.DistanciaAlContorno` | Función/método | [156](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L156) | Entrada: malla triangular abierta. Proceso: Dijkstra por aristas. |
| `AnalizadorMalla._VerticesNoManifold` | Función/método | [168](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L168) | True si algún vértice no tiene un único abanico de caras (A-05). |
| `AnalizadorMalla._Adyacencia` | Función/método | [205](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L205) | Sin docstring; consultar el catálogo de módulos y el código. |
| `AnalizadorMalla._Geodesica` | Función/método | [214](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py#L214) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py`

Modelo de impresión y construcción de la geometría.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Model3DForPrinting` | Clase | [48](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L48) | Pieza paramétrica: geometría, volumen, peso y precio de material. |
| `Model3DForPrinting.__init__` | Función/método | [51](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L51) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.vertices` | Función/método | [63](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L63) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.vertices` | Función/método | [67](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L67) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.faces` | Función/método | [72](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L72) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.faces` | Función/método | [76](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L76) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.ValidarOpciones` | Función/método | [81](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L81) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.ConstruirGeometria` | Función/método | [131](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L131) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.ChangePatern` | Función/método | [180](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L180) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.Construir` | Función/método | [197](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L197) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.CalculateVolume` | Función/método | [214](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L214) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.CalculateWeight` | Función/método | [231](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L231) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Model3DForPrinting.CalculatePrice` | Función/método | [239](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py#L239) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py`

Crea o actualiza el objeto OL_Ortesis en la escena de Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `GeneradorObjeto` | Clase | [40](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L40) | Escribe el cascarón en la escena y, si se pide, lo reconstruye con voxel. |
| `GeneradorObjeto._EspesorMinimo` | Función/método | [44](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L44) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorObjeto._Componentes` | Función/método | [53](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L53) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorObjeto._AplicarModificador` | Función/método | [76](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L76) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorObjeto._DescartarTrabajo` | Función/método | [83](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L83) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorObjeto._PromoverResultado` | Función/método | [92](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L92) | Sin docstring; consultar el catálogo de módulos y el código. |
| `GeneradorObjeto.Crear` | Función/método | [134](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py#L134) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py`

Complemento OrtesisLab dentro del paquete.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `Complemento` | Clase | [15](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L15) | Registra el panel y construye geometría sin escribirla todavía en escena. |
| `Complemento.BuildGeometry` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Complemento.Retirar` | Función/método | [31](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L31) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Complemento.Registrar` | Función/método | [46](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L46) | Sin docstring; consultar el catálogo de módulos y el código. |
| `register` | Función/método | [69](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L69) | Sin docstring; consultar el catálogo de módulos y el código. |
| `unregister` | Función/método | [74](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py#L74) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py`

Refinamiento triangular independiente de Blender para evaluar patrones.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `RefinadorMalla` | Clase | [13](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py#L13) | Divide únicamente las aristas largas y conserva una superficie conectada. |
| `RefinadorMalla.PasoPatron` | Función/método | [17](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py#L17) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RefinadorMalla.AristaMayor` | Función/método | [25](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py#L25) | Sin docstring; consultar el catálogo de módulos y el código. |
| `RefinadorMalla.Refinar` | Función/método | [32](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py#L32) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py`

Limpieza segura de la superficie base dentro de Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ReparadorMalla` | Clase | [23](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L23) | Limpia una superficie abierta sin convertirla en un volumen. |
| `ReparadorMalla._ComponentesCaras` | Función/método | [29](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L29) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReparadorMalla._EliminarCarasDuplicadas` | Función/método | [50](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L50) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReparadorMalla._EliminarSinCaras` | Función/método | [66](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L66) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReparadorMalla._ArreglarBmesh` | Función/método | [75](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L75) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReparadorMalla._ValidarBmesh` | Función/método | [132](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L132) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ReparadorMalla.Arreglar` | Función/método | [148](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py#L148) | Repara la malla activa y devuelve un resumen de lo retirado. |

## `apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py`

STL binario del cascarón, en milímetros, sin Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `StlBinario` | Clase | [21](../../apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py#L21) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StlBinario.Triangulos` | Función/método | [23](../../apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py#L23) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StlBinario.Bytes` | Función/método | [34](../../apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py#L34) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StlBinario.Contar` | Función/método | [54](../../apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py#L54) | Sin docstring; consultar el catálogo de módulos y el código. |
| `StlBinario.VerticesSiBinario` | Función/método | [58](../../apps/ortesis-plugin/OrtesisLabPlugin/StlBinario.py#L58) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py`

Suavizado del contorno exterior antes de dar espesor.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `SuavizadoBorde` | Clase | [15](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L15) | Aplana los dientes del contorno sin mover el interior de la superficie. |
| `SuavizadoBorde.Aplicar` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuavizadoBorde._Bucles` | Función/método | [103](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L103) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuavizadoBorde._Perimetro` | Función/método | [139](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L139) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuavizadoBorde._Pasabajos` | Función/método | [148](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L148) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuavizadoBorde._PasabajosCampo` | Función/método | [153](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L153) | Filtra ``campo`` con el perímetro físico de ``geometria`` (mm). |
| `SuavizadoBorde._MascaraRota` | Función/método | [183](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L183) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuavizadoBorde._CarasRotas` | Función/método | [193](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py#L193) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py`

Carga y lectura de la superficie interior dentro de Blender.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `SuperficieInterior` | Clase | [38](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py#L38) | Prepara una copia de la superficie elegida, sin cerrar sus aberturas. |
| `SuperficieInterior.VaciarCache` | Función/método | [43](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py#L43) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieInterior._Candidatos` | Función/método | [47](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py#L47) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieInterior.Cargar` | Función/método | [60](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py#L60) | Sin docstring; consultar el catálogo de módulos y el código. |
| `SuperficieInterior.Leer` | Función/método | [104](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py#L104) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/util/__init__.py`

Utilidades compartidas: registro de ejecución y lectura de JSON.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| — | Sin clases/funciones | — | Declaraciones o marcador de paquete |

## `apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py`

Registro de mensajes y lectura de la carpeta config.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `CarpetaConfig` | Función/método | [18](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L18) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Registro` | Clase | [25](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L25) | Escribe en consola y en logs/ortesislab.log. |
| `Registro._Preferencias` | Función/método | [39](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L39) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Registro._Nivel` | Función/método | [58](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L58) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Registro.Configurar` | Función/método | [66](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L66) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Registro.Obtener` | Función/método | [100](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L100) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion` | Clase | [106](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L106) | Carga los JSON de config y comprueba que traigan las claves esperadas. |
| `Configuracion._Error` | Función/método | [205](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L205) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.Recargar` | Función/método | [212](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L212) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.CargarJson` | Función/método | [225](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L225) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion._ExigirClaves` | Función/método | [250](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L250) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.ParametrosDefecto` | Función/método | [260](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L260) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.Limites` | Función/método | [267](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L267) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion._ValidarLimites` | Función/método | [275](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L275) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.ValorLimite` | Función/método | [297](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L297) | Sin docstring; consultar el catálogo de módulos y el código. |
| `Configuracion.ComprobacionDeReferencia` | Función/método | [304](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py#L304) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py`

Comprobación geométrica de la malla ya generada.

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ValidadorMalla` | Clase | [20](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py#L20) | Informa si OL_Ortesis es una sola pieza cerrada. |
| `ValidadorMalla.GuardarInforme` | Función/método | [24](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py#L24) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorMalla._Cruces` | Función/método | [28](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py#L28) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorMalla.Comprobar` | Función/método | [56](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py#L56) | Sin docstring; consultar el catálogo de módulos y el código. |

## `apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py`

Validación de mallas sólidas solo con NumPy (sin Blender).

| Símbolo | Tipo | Línea | Descripción declarada |
|---|---|---:|---|
| `ValidadorSolido` | Clase | [15](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L15) | Comprueba topología de un sólido triangular antes de publicar. |
| `ValidadorSolido._ContarComponentes` | Función/método | [19](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L19) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido._ContarComponentes.buscar` | Función/método | [24](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L24) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido._ContarComponentes.unir` | Función/método | [30](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L30) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido._ContarAristas` | Función/método | [42](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L42) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido._CarasDegeneradas` | Función/método | [53](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L53) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido._CrucesHeuristica` | Función/método | [64](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L64) | Heurística ligera: solo en mallas pequeñas; no sustituye BVH de Blender. |
| `ValidadorSolido._TrianguloContiene` | Función/método | [91](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L91) | Sin docstring; consultar el catálogo de módulos y el código. |
| `ValidadorSolido.Comprobar` | Función/método | [108](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionSolido.py#L108) | Salida: informe compatible con ``ValidadorMalla``. |
