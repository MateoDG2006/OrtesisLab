# Mapa completo del paquete Blender y del núcleo

El [índice de símbolos](SIMBOLOS.md) complementa este mapa con cada método y su ubicación. Todas las rutas siguientes son enlaces al código actual, no al ZIP publicado.

## Paquete y adaptadores Blender

| Archivo | Responsabilidad / entradas y salidas |
|---|---|
| [`__init__.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/__init__.py) | Metadatos `bl_info` 1.3.0 / Blender 5.0; `register` y `unregister` importan diferidamente el registro |
| [`ApiBlender.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/ApiBlender.py) | Importa y reexporta API Blender; falla explícitamente fuera de ese entorno |
| [`OrtesisLab.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/OrtesisLab.py) | `Complemento` registra/retira clases; `BuildGeometry` devuelve arrays; funciones de entrada Blender |
| [`Interfaz.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Interfaz.py) | `PanelAyuda`, `OL_Preferences`, `OL_Settings`, cinco operadores y panel; transforma acciones en llamadas de dominio |
| [`Superficie.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Superficie.py) | `Leer` valida objeto y prepara copia, escala/refinamiento y caché LRU; `Cargar` conserva carga NPZ explícita de compatibilidad |
| [`ReparacionMalla.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/ReparacionMalla.py) | `ReparadorMalla`: hornear escala, fusionar, limpiar, conservar mayor componente de caras y recalcular normales |
| [`Objeto.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Objeto.py) | `GeneradorObjeto`: cascarón → datablock/objeto; voxel, descarte de fragmentos y smooth opcionales |
| [`ValidacionMalla.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/ValidacionMalla.py) | `ValidadorMalla`: informe de conectividad, bordes, no manifold, degeneradas y cruces; guarda `ol_validation` |
| [`Exportacion.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Exportacion.py) | `ExportadorStl`: revalida, exporta seleccionado, escribe `*.stl.json`; bloquea informe inválido |

### Responsabilidades de los operadores

`OL_OT_use_surface` comprueba y asigna la base, sin guardarla desde NPZ. `OL_OT_repair_surface` limpia el objeto activo, no necesariamente el previamente asignado. `OL_OT_generate` toma parámetros de `OL_Settings`. `OL_OT_validate` comprueba `OL_Ortesis`, no el activo. `OL_OT_export` exporta ese mismo nombre y abre selector mediante `invoke`. `PanelAyuda.Cancelar` publica el error y retorna `CANCELLED`; la validación con informe malo termina `FINISHED` con aviso, mientras la exportación de ese informe sí se cancela.

Cambiar el JSON de defaults no cambia automáticamente los `default` declarados en `OL_Settings`: deben mantenerse sincronizados.

## Núcleo independiente de Blender

| Archivo | Componentes y finalidad |
|---|---|
| [`Modeling.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Modeling.py) | `Model3DForPrinting`: valida opciones, combina patrón/marco/banda, suaviza borde, recorta o varía espesor y llama engrosado; conserva geometría para métricas |
| [`Malla.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Malla.py) | `AnalizadorMalla`: normales de caras, contrato triangular, topología abierta/conectada, suavizado de normales y Dijkstra desde el contorno |
| [`RefinadorMalla.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/RefinadorMalla.py) | Divide aristas largas con punto medio único; casos de 0/1/2/3 cortes por triángulo; suaviza normales y vuelve a analizar |
| [`SuavizadoBorde.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/SuavizadoBorde.py) | Descubre bucles, remuestrea por longitud, filtra FFT y limita desplazamiento para evitar caras invertidas |
| [`Cascaron.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Cascaron.py) | Hermite `Smooth01`, recorte por campo escalar con cruces compartidos, duplicación por normales, muros del contorno y volumen |
| [`Excepciones.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/Excepciones.py) | Taxonomía de errores previstos, heredados de `OrtesisLabError`; al construirse intentan registrar mensaje y detalle |

El encabezado histórico de `Cascaron.py` dice «en contra de la normal»; la implementación vigente de `Engrosar` usa **`p + n*t`**. La documentación describe esa expresión ejecutada. `flip_normals=True` invierte normales y orden de caras antes del engrosado.

## `constants/`

| Archivo | Uso |
|---|---|
| [`Paterns.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Paterns.py) | `Patron`, rotación XY, retícula, semillas y bisectrices; subclases `Voronoi`, `HoneyComb`, `Diamond`, `Square`, `Solid`; catálogo y aliases |
| [`Materials.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Materials.py) | `Material` valida nombre/densidad/precio; `Gramos` y `Costo`; `PETG` establece densidad 1.27 y precio 0.15 |
| [`Nombres.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/Nombres.py) | Nombres estables de objetos, atributos, propiedades, modificadores y STL por defecto |
| [`__init__.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/constants/__init__.py) | Marcador del subpaquete |

Se conserva la ortografía de archivo `Paterns.py` y del alias de método `ChangePatern`: cambiarla rompe imports existentes. `ChangePattern` reenvía a `ChangePatern`. `Triangle` y `Minimalistic` tienen metadata de catálogo, pero no geometría. Las imágenes de catálogo son un placeholder remoto; el panel actual no las utiliza para construir geometría.

## `util/` y `config/`

[`util/Utilidades.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/util/Utilidades.py) contiene `Registro` y `Configuracion`. `Registro.Configurar` monta consola/archivo y `Obtener` devuelve logger hijo. La carpeta [`util/__init__.py`](../../apps/ortesis-plugin/OrtesisLabPlugin/util/__init__.py) marca el paquete. `Configuracion.CargarJson` cachea y devuelve copia superficial; `Recargar` vacía esa caché; `ParametrosDefecto`, `Limites` y `ValorLimite` verifican claves y tipos; `ComprobacionDeReferencia` obtiene resultados históricos.

| JSON | Contrato |
|---|---|
| [`parametros_defecto.json`](../../core/config/parametros_defecto.json) | 17 opciones iniciales compartidas; no incluye el objeto `source` |
| [`limites.json`](../../core/config/limites.json) | Umbrales y presupuestos de algoritmos; cambiarlo afecta núcleo y adaptadores |
| [`registro.json`](../../core/config/registro.json) | Nivel consola/archivo y nombre del log |
| [`comprobacion_geometrica.json`](../../core/config/comprobacion_geometrica.json) | Referencias históricas, no criterios de aceptación de la malla actual |

Los valores exactos y claves de los cuatro archivos se mantienen en [CONFIGURACION_GENERADA.md](CONFIGURACION_GENERADA.md). La comprobación documental detecta cambios en ellos.

## Scripts y distribución

[`scripts/EmpaquetarBlender.py`](../../scripts/EmpaquetarBlender.py) incluye `.py` y `.json` del paquete y `docs/BlenderPlugin/LEEME.md`, excluyendo logs/cache; escribe un ZIP temporal, comprueba integridad y reemplaza el destino. El directorio raíz dentro del ZIP es `OrtesisLabPlugin`, que es el módulo que importa Blender. No incluye Reflex, visor, pruebas ni NPZ. Si ya existe el ZIP principal, conserva una copia anterior una sola vez en `dist/GenerateModelsApp-anterior.zip`.

[`scripts/EjecutarOrtesisLab.py`](../../scripts/EjecutarOrtesisLab.py) añade `apps/ortesis-plugin` a `sys.path` y llama `register` dentro de Blender. `scripts/IniciarConsola.py` es solo el saludo de consola. Los archivos `GenerateModelsApp.zip`, `dist/` y logs de tests son artefactos de distribución/históricos; no sustituyen a la fuente revisada.
