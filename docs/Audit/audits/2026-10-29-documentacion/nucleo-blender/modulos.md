# Núcleo geométrico y complemento Blender · Catálogo por módulo y función

**Estado:** propuesta. El código no cambia desde `2b74669`. Los hallazgos A-01 a
A-22 de `AUD-2026-10-13-001` siguen abiertos.
**Archivos:** `GenerateModelsApp/**` (26 archivos), `scripts/EmpaquetarBlender.py`,
`scripts/EjecutarOrtesisLab.py`.

Fuentes de esta ficha:

- `Modeling.py`, `Materials.py`, `EscalaMalla.py`, `RefinadorMalla.PasoPatron` y
  `RefinadorMalla.Refinar` (inicio), y los JSON de `config/`: lectura directa.
- El resto: catálogo `ast` de firmas y docstrings, contrastado con
  `docs/BlenderPlugin/ALGORITMOS.md` y la auditoría anterior.

Las celdas que se basan solo en el catálogo dicen **(firma)**.

## Capas

| Capa | Módulos | Dependencia de Blender |
|---|---|---|
| Configuración y registro | `util/Utilidades.py`, `config/*.json` | No |
| Dominio puro | `Modeling`, `Malla`, `EscalaMalla`, `RefinadorMalla`, `SuavizadoBorde`, `Cascaron`, `constants/*`, `Excepciones` | No; lo usan la web y el trabajador |
| Adaptadores | `ApiBlender`, `Superficie`, `ReparacionMalla`, `Objeto`, `ValidacionMalla`, `Exportacion`, `Interfaz`, `OrtesisLab`, `__init__` | Sí (`bpy`, `bmesh`, `mathutils`). Importarlos fuera de Blender lanza `EntornoBlenderRequerido` |

## `Modeling.py` · `Model3DForPrinting`

| Miembro | E → S | Proceso | Err |
|---|---|---|---|
| `__init__(material=None)` | → instancia | Material PETG por defecto, patrón VORONOI y opciones del JSON | `MaterialInvalido` |
| `ValidarOpciones(options)` | dict → cfg completo | 1) `options` es dict y sus claves están en la plantilla. 2) `flip_normals`, `repair` y `liner` son `bool`. 3) Positivos y finitos: `cell_mm`, `rib_width_mm`, `rib_height_mm`, `skin_mm`, `solid_mm`, `surface_step_mm`. 4) `pattern` en `Patron.Geometricos()`. 5) `cell_mm ≥ min_cell_mm` (5). 6) Patrón distinto de SOLID: `rib_width_mm < cell_mm × 0.75`. 7) Finitos: `border_mm`, `rounding_mm`, `angle_deg`, `reinforce_*`, `resolution_mm`. 8) `resolution_mm > 0`. 9) `seed`: `int ≥ 0`, no `bool`. 10) `border_mm`, `rounding_mm` y `reinforce_width_mm ≥ 0` | `ParametrosNoReconocidos`, `GeometriaInconsistente`, `ParametroNoPositivo`, `PatronNoReconocido`, `CeldaDemasiadoPequena`, `NervaduraDemasiadoAncha`, `ParametroNoFinito`, `ResolucionNoPositiva`, `SemillaInvalida`, `BordeNegativo` |
| `ConstruirGeometria(v, f, n, borde, **opts)` | → `(vértices, caras, cfg, n_puntos, n_caras)` | Ver la secuencia siguiente | Las de validación y de `Cascaron` |
| `ChangePatern(p)` / `ChangePattern(p)` | Código, nombre o `Patron` → instancia | Cambia el patrón e invalida el volumen | `PatronNoImplementado` |
| `Construir(...)` | Igual que `ConstruirGeometria` | Guarda el resultado en la instancia y sincroniza opciones y patrón | — |
| `CalculateVolume()` | → mm³ | `Cascaron.VolumenMm3`, con caché | `ModeloSinGeometria` |
| `CalculateWeight()` | → g | `material.Gramos(volumen)` | — |
| `CalculatePrice()` | → número sin moneda | `peso × material.price` | — |

Secuencia de `ConstruirGeometria`:

1. Valida las opciones.
2. Si `flip_normals`, invierte normales y el orden de las caras.
3. `SuavizadoBorde.Aplicar`; si hubo desplazamiento, recalcula
   `DistanciaAlContorno`.
4. `distancia = patron.Distancia(puntos, cell, angle, seed)`.
5. Calcula el campo `nervadura`:
   - base: `rib_width/2 − distancia`;
   - con `border > 0`: `max(…, border − borde)`;
   - con banda: `max(…, reinforce_width/2 − |y − reinforce_y|)`.
6. Calcula el espesor:
   - `SOLID`: `solid_mm`;
   - con `liner`: `skin + rib_height × Smooth01(nervadura / max(0.02, rounding) + 0.5)`;
   - sin capa: `Cascaron.Recortar(…, nervadura)` y `rib_height` constante.
7. `Cascaron.Engrosar(puntos, caras, normales, espesor)`.

**No usa** `repair`, `resolution_mm` ni `surface_step_mm` (B-19): son
parámetros de Blender y del refinamiento previo.

## `constants/Materials.py`

| Miembro | Contrato |
|---|---|
| `Material(name, density, price, color, kind, brand)` | `name` no vacío; densidad > 0 y finita (g/cm³); precio ≥ 0 y finito (por gramo, **sin moneda**). Si no, `MaterialInvalido`. Guarda `kind` como `self.type` |
| `Gramos(mm³)` | `mm³ × densidad / 1000`; `MaterialInvalido` si no es numérico, finito y ≥ 0 |
| `Costo(mm³)` | `Gramos × price` |
| `PETG()` | 1.27 g/cm³, 0.15 por gramo, `black`, `filament`, `Prusament` |

## `EscalaMalla.py`

| Miembro | Contrato |
|---|---|
| `Candidatos(dim)` | Factores `10^k`, con `k ∈ [−6, 6]`, que dejan `dim × f` en `[20, 1000]` mm, ordenados por `|k|` y prefiriendo `k` positivo; `[]` si `dim` no es finita o es ≤ 0 |
| `Diagnosticar(dim)` | `{factor, dimension_antes_mm, dimension_despues_mm, advertencia}`; factor = primer candidato, o 1 con advertencia si no hay |
| `AlcanzaPaso(arista, paso, f)` | `arista × f ≤ paso × 1.001 × 2^16` |
| `Presupuesto(arista, paso, n_caras, f)` | `False` si no alcanza el paso, si `n_caras > 500000` o si necesita 12 niveles o más; si no, `n_caras ≤ 500000 / 4^niveles` |
| `EsFalloDePaso(exc)` | `SuperficieInvalida` cuyo mensaje contiene «paso de superficie» |
| `Aplicar(dim, autoescalar, operacion, *, arista_maxima, paso_mm, n_caras)` | Con autoescala: prueba el factor preferido (el primero que alcanza el paso) y después los **menores** dentro del rango, y reintenta solo ante fallos de paso. Sin autoescala: un único intento con factor 1 y una advertencia con el factor sugerido. Devuelve `(resultado, diagnóstico)` con `factor_sugerido`. Puede cambiar el tamaño físico (A-14) |
| `Resolver(dim, autoescalar=True)` | Diagnóstico sin operación; sin autoescala, factor 1 y advertencia |

## `RefinadorMalla.py`

| Miembro | Contrato |
|---|---|
| `PasoPatron(opciones)` | `surface_step_mm`; si el patrón no es SOLID, `min(step, rib_width/3, cell/6)` |
| `AristaMayor(p, f)` | Longitud máxima de arista o 0 |
| `Refinar(v, f, n, paso)` | `SuperficieInvalida` si el paso no es positivo y finito. Hasta 16 rondas dividiendo aristas mayores de `paso × 1.001` con punto medio único; tope de 500000 vértices. Puede devolver éxito sin alcanzar el paso (A-06) **(cuerpo parcial)** |

## `Malla.py` · `AnalizadorMalla`

| Miembro | Contrato |
|---|---|
| `NormalesDeCaras(v, f)` | Normal por vértice, ponderada por área; no modifica la entrada |
| `Preparar(v, f, n, *, suavizarNormales)` | Contrato triangular, topología abierta, conectada y orientada de una capa, normales y borde Dijkstra → `(p, f, n, borde)`. `SuperficieInvalida` y familia. No detecta vértices no manifold (A-05) y acepta normales incompatibles (A-04) **(firma + auditoría)** |
| `DistanciaAlContorno(v, f)` | Distancia geodésica por aristas al contorno (mm); avisa si hay vértices inalcanzables |
| `_Adyacencia`, `_Geodesica` | Auxiliares de Dijkstra |

## `SuavizadoBorde.py`

| Miembro | Contrato |
|---|---|
| `Aplicar(v, f, n)` | Copias de vértices y normales con el contorno filtrado (pasabajos FFT, longitud de onda 8 mm, máximo 3 mm) y el desplazamiento máximo. El interior no se mueve |
| `_Bucles`, `_Pasabajos`, `_MascaraRota`, `_CarasRotas` | Detección de bucles, filtro y rechazo de propuestas que invierten caras **(firma)**. El filtro de normales mezcla distancias vectoriales con mm (A-22) |

## `Cascaron.py`

| Miembro | Contrato |
|---|---|
| `Smooth01(t)` | Hermite acotado a [0, 1] |
| `Recortar(p, f, n, campo)` | Conserva la región con campo ≥ 0 y comparte los cruces de arista **(firma)** |
| `Engrosar(p, f, n, t)` | Duplica por `p + n·t` y une **solo** las aristas libres con su copia (muros); nunca tapa aberturas |
| `Cerrar` | Alias de `Engrosar` |
| `VolumenMm3(v, f)` | Suma de tetraedros orientados, triangulando polígonos; error si no hay caras |

## `constants/Paterns.py`

| Clase | Código | `Distancia` |
|---|---|---|
| `Patron` (base) | — | `RotarXy`, `DistanciaCuadricula`, `DistanciaSemillas` (cota de semillas vecinas), `_DistanciaPlanos` (bisectriz), `Geometricos()` y `Obtener(código o nombre)` |
| `Voronoi` | `VORONOI` | Semillas con jitter de 0.28 y semilla del usuario |
| `HoneyComb` | `HEX` | Retícula hexagonal |
| `Diamond` | `DIAMOND` | Retícula girada |
| `Square` | `SQUARE` | Cuadrícula |
| `Solid` | `SOLID` | Campo constante (macizo) |
| `Triangle`, `Minimalistic` | Sin geometría | Solo catálogo; `PatronNoImplementado` |

## `Excepciones.py`

`OrtesisLabError(message, *, detalle)` es la base; al construirse intenta
registrar el mensaje. Hay 34 subclases agrupadas por fase:

| Fase | Subclases |
|---|---|
| Configuración | `ConfiguracionInvalida` |
| Entorno | `EntornoBlenderRequerido` |
| Entrada | `ArchivoSuperficieNoEncontrado`, `ArchivoSuperficieIlegible`, `SuperficieNoEsMalla`, `SuperficieInvalida`, `ModificadoresSinAplicar`, `EscalaSinAplicar`, `SuperficieSinCaras`, `SolidoCerrado`, `AristasNoManifold`, `VerticesSueltos`, `NormalesInvalidas` |
| Parámetros | `ParametrosNoReconocidos`, `ParametroNoPositivo`, `PatronNoReconocido`, `PatronNoImplementado`, `CeldaDemasiadoPequena`, `NervaduraDemasiadoAncha`, `ParametroNoFinito`, `ResolucionNoPositiva`, `SemillaInvalida`, `BordeNegativo` |
| Construcción | `SuperficieEliminadaPorPatron`, `ResolucionDemasiadoFina`, `GeometriaFragmentada`, `GeometriaInconsistente`, `MallaNoConstruida`, `ReconstruccionFallida` |
| Salida | `ModeloNoGenerado`, `MallaNoValida`, `ExportacionFallida`, `ModeloSinGeometria`, `MaterialInvalido` |

En la web, cualquier `OrtesisLabError` durante la construcción deja el ítem en
`failed` **sin reintento**.

## `util/Utilidades.py`

| Miembro | Contrato |
|---|---|
| `Registro.Configurar()` / `Obtener(nombre)` | Logger `ortesislab.<nombre>`: consola INFO y archivo DEBUG `GenerateModelsApp/logs/ortesislab.log` según `registro.json`. Si falla la lectura, usa los valores por defecto |
| `Configuracion.CargarJson(nombre)` | Lectura con caché; devuelve una copia superficial. `ConfiguracionInvalida` |
| `Recargar()` | Vacía la caché |
| `ParametrosDefecto()` / `Limites()` / `ValorLimite(clave)` | Comprueban claves y tipos |
| `ComprobacionDeReferencia()` | Referencias históricas (no son criterios de aceptación) |

## Configuración JSON del núcleo (valores en `e56df68`)

`parametros_defecto.json` (17 claves): `pattern` VORONOI, `cell_mm` 15,
`rib_width_mm` 2.8, `rib_height_mm` 1.4, `liner` true, `skin_mm` 1, `solid_mm`
2.4, `border_mm` 4, `rounding_mm` 0.8, `angle_deg` 0, `seed` 7,
`reinforce_y_mm` 0, `reinforce_width_mm` 0, `repair` false, `flip_normals`
false, `surface_step_mm` 1, `resolution_mm` 0.3.

`limites.json` (25 claves); las que usan web y núcleo son:

| Clave | Valor | Uso |
|---|---|---|
| `min_cell_mm` | 5 | Validación |
| `max_rib_width_ratio` | 0.75 | Validación |
| `min_rounding_width_mm` | 0.02 | Perfil de capa |
| `max_surface_vertices` | 500000 | Refinado y presupuesto |
| `surface_subdivision_iterations` | 16 | Refinado |
| `clip_snap_mm` | 0.0001 | Fusión STL y recorte |
| `border_smooth_wavelength_mm` / `border_smooth_max_mm` | 8 / 3 | Suavizado del contorno |
| `min_plausible_surface_extent_mm` / `max_plausible_surface_extent_mm` | 20 / 1000 | Escala |

Las de Blender son `min_voxel_repair_mm`, `fragment_vertex_floor` y `ratio`.
`max_refined_cache_entries` (2) solo aplica a la caché LRU de Blender.

## Adaptadores Blender

| Módulo | Miembros |
|---|---|
| `__init__.py` | `bl_info` 1.3.0 / Blender 5.0; `register`/`unregister` diferidos |
| `ApiBlender.py` | Reexporta `bpy`, `bmesh` y `mathutils`; `EntornoBlenderRequerido` fuera de Blender |
| `OrtesisLab.py` | `Complemento.BuildGeometry(source, **opts)`, `Retirar`, `Registrar`; `register`/`unregister` |
| `Superficie.py` | `SuperficieInterior._Candidatos`, `Cargar(path)` (compatibilidad NPZ), `_CorregirUnidades`, `Leer(source, *, paso_mm, autoescalar)` con LRU (≤ 2 refinadas) |
| `ReparacionMalla.py` | `ReparadorMalla.Arreglar(objeto, autoescalar)`: hornea la escala, fusiona, limpia y conserva la mayor componente; recalcula normales |
| `Objeto.py` | `GeneradorObjeto.Crear(source, **opts)`: datablock `OL_Ortesis` y voxel opcional (`resolution_mm`), descarte de fragmentos; reemplaza antes de validar (A-09) |
| `ValidacionMalla.py` | `ValidadorMalla.Comprobar(ob, intersections=True)`: componentes, bordes, no manifold, degeneradas y cruces BVH → `ol_validation` |
| `Exportacion.py` | `ExportadorStl.Exportar(ob, path)`: revalida, exporta la malla **evaluada** (A-08) y escribe `*.stl.json` |
| `Interfaz.py` | `PanelAyuda` (`OrigenAutoescala`, `AvisarEscala`, `OpcionesDesdeAjustes`, `Cancelar`), `OL_Preferences`, `OL_Settings`, los operadores `generate`, `use_surface`, `repair_surface`, `validate` y `export`, y el panel `OL_PT_panel` |

## Empaquetado

`scripts/EmpaquetarBlender.py`:

- **Incluye:** los `.py` y `.json` del paquete (sin `__pycache__` ni `logs`) y
  `docs/BlenderPlugin/LEEME.md` como `GenerateModelsApp/LEEME.md`.
- **Proceso:** escribe un ZIP temporal, ejecuta `testzip` y comprueba que exista
  `__init__.py`. La **primera** vez guarda una copia en
  `dist/GenerateModelsApp-anterior.zip` y después reemplaza el ZIP.
- **Estado en `e56df68`:** el `LEEME.md` del ZIP está desactualizado (B-16).
