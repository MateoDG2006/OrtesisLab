# Frontend · Estado, páginas y visor

**Estado:** propuesta. **Archivos:** `web/EstadoApp.py`, `web/EstadoHistorial.py`,
`web/PaginaComparacion.py`, `web/PaginaHistorial.py`, `web/Sesion.py`,
`web/GenerateModelsApp.py`, `assets/visor.html`, `assets/favicon.ico`, `rxconfig.py`.

Reflex compila los componentes Python a React. El estado (`rx.State`) vive en el
servidor y los eventos viajan por WebSocket. Toda identidad se resuelve en el
servidor desde la cabecera `Cookie` del WebSocket (`self.router.headers.cookie`).

## Rutas

| Ruta | Componente | `on_load` | Título |
|---|---|---|---|
| `/` | `PaginaComparacion.Index` | `EstadoApp.CargarPredeterminados` | OrtesisLab |
| `/historial` | `PaginaHistorial.Index` | `EstadoHistorial.Cargar` | Historial · OrtesisLab |
| `/auth/*` | Starlette (no Reflex) | — | — |
| `/visor.html` | Recurso estático de `assets/` | — | Vista previa |

## `EstadoApp`: variables de estado

| Grupo | Variable (tipo, inicial) | Uso |
|---|---|---|
| Parámetros geométricos | `pattern` (`"VORONOI"`); como `str`: `cell_mm` `"15"`, `rib_width_mm` `"2.8"`, `rib_height_mm` `"1.4"`, `skin_mm` `"1"`, `solid_mm` `"2.4"`, `border_mm` `"4"`, `rounding_mm` `"0.8"`, `angle_deg` `"0"`, `seed` `"7"`, `reinforce_y_mm` `"0"`, `reinforce_width_mm` `"0"`, `resolution_mm` `"0.3"`, `surface_step_mm` `"1"`; como `bool`: `liner` `True`, `flip_normals` `False`, `repair` `False` | Texto editable; `CargarPredeterminados` lo sobrescribe con el JSON |
| Lote | `usar_voronoi` `True`, `usar_hex`/`usar_diamond`/`usar_square`/`usar_solid` `False`, `eje` `"ninguno"`, `desde` `"10"`, `hasta` `"20"`, `paso` `"5"`, `ambos_revestimientos` `False` | Entrada de `Combinaciones` |
| Trabajo | `ocupado`, `mensaje`, `hechos`, `total`, `modo_lote`, `lote_id`, privadas `_trabajando`, `_solicitud` | Progreso y exclusión |
| Vista | `archivo` (`object_url`), `ficha_detalle`, `ficha_volumen`, `ficha_peso`, `ficha_precio`, `ficha_error`, `resultados: list[dict[str,str]]`, `vistas: list[str]` (≤ 3) | Fichas y visores |
| Superficie | `superficie_archivo` (`""` = plantilla), `superficie_nombre`, `superficie_detalle`, `superficie_error`, `subiendo_superficie`, `autoescalar_superficie`, `superficie_eje_mm` | Entrada |
| Sesión | `autenticado`, `usuario_nombre`, privadas `_propietario`, `_revision_preferencias` | Barra y limpieza al cambiar de usuario |

Variables calculadas (`@rx.var`):

- `aviso_escala`: texto según `EscalaMalla.Resolver(superficie_eje_mm)`.
- `espesor_total`: `skin + rib_height` con formato; `""` si no se puede
  convertir.
- `porcentaje`: `int(hechos × 100 / total)`.

## `EstadoApp`: eventos

| Evento | Tipo | Comportamiento y mensajes |
|---|---|---|
| `set_*` (26 setters; no hay para `repair` ni `resolution_mm`) | Sincrónico salvo uno | Asignan el valor sin validar. `set_autoescalar_superficie` es asíncrono: guarda la preferencia con revisión; ante conflicto recarga y muestra el mensaje de `ConflictoRevision` |
| `CargarSuperficie(archivos)` | Asíncrono | Exige exactamente 1 archivo («Seleccione un único archivo STL o NPZ.») y sesión («Inicie sesión para guardar la superficie.»). Lee hasta 50 MiB + 1 y ejecuta `GuardarSuperficie` en un hilo. Mensajes: «La superficie subida no es válida.», «No se pudo guardar la superficie.», «No se pudo leer la superficie.» o «Superficie cargada; lista para generar.». Siempre limpia la selección |
| `UsarSuperficieIncluida` | Asíncrono | Vuelve a la plantilla, recalcula `superficie_eje_mm` y borra fichas y vistas |
| `CargarPredeterminados` | Asíncrono, `on_load` | JSON → formulario. Si cambió el usuario y no hay trabajo en curso, `_OlvidarTrabajo`. Calcula el eje de la plantilla (B-04). Lee preferencias y último lote; si está abierto, encadena `SeguirLote` |
| `Previsualizar` / `PedirLote` | Sincrónico | `modo_lote` = `False`/`True`, `_solicitud` = UUID nuevo → `Generar` |
| `Generar` | `background=True` | Exclusión por `_trabajando`. `_Variantes()` bajo el bloqueo del estado y, fuera de él: `Requerir`, `Resolver`, `Solicitar` (`mode` = `sweep` si hay más de una variante, si no `single`). Mensaje «En cola. El trabajador construye cada variante.» y después `_Seguir` |
| `SeguirLote` | `background=True` | Reanuda `_Seguir` con `lote_id` |
| `CancelarLote` | Asíncrono | **Sin control en la UI** (B-22). Mensaje «Cancelación pedida; la variante en curso termina antes de parar.» |
| `Ver(id)` | Sincrónico | Muestra la ficha |
| `Comparar(id)` | Sincrónico | Alterna en `vistas`; la cuarta: «La comparación muestra tres ortesis a la vez…» |
| `Descargar(id)` | Asíncrono | Extrae el `asset` de la URL con `PATRON_CLAVE` → `RegistrarDescarga` → `rx.download(url, filename="ortesis-<8 hex>.stl")` |

Auxiliares:

- `_Usuario()`: sesión o `None`; actualiza `autenticado`.
- `_Seguir(usuario, lote)`: bucle de 1 s hasta que el lote cierra.
- `_Publicar(progreso)`: fichas de los ítems terminales; mensajes «En cola,
  esperando al trabajador.», «x de y», «Lote cancelado…», «Listo. n de m no se
  pudieron construir.» y «Listo. n variante(s).».
- `_OlvidarTrabajo()`, `_Mostrar(ficha)`, `_Variantes()`, `_Opciones()`.
- `_Numero(texto, etiqueta)`: acepta coma decimal y rechaza no finitos. En el
  navegador, los `rx.input(type="number")` de `Campo` limitan qué puede
  escribirse según el locale, así que la coma puede no llegar nunca.

## `EstadoHistorial`

| Variable | Uso |
|---|---|
| `filtro_patron`, `filtro_estado` (`"todos"`), `filtro_desde`, `filtro_hasta` (`AAAA-MM-DD`) | Filtros que se aplican con «Filtrar» |
| `filas: list[dict]` | Las claves son `item_id`, `version_id`, `version`, `proyecto`, `fecha` (hora local del **servidor**, `astimezone()`), `patron`, `detalle`, `estado`, `volumen`, `peso`, `precio`, `url`, `asset_id` y `aviso` |
| `pagina`, `hay_siguiente`, privadas `_cursores`, `_siguiente` | Paginación por cursor; «Anterior» retrocede en la pila |
| `seleccion` (≤ 3 ids), `comparacion` (tarjetas) | Comparación |

Eventos:

| Evento | Comportamiento |
|---|---|
| `Cargar` | Página 1 y vacía la selección |
| `Siguiente` / `Anterior` | Navegación por la pila de cursores |
| `Seleccionar` | Alterna la selección y recalcula las tarjetas |
| `Restaurar` / `Reintentar` | Crean el lote y redirigen a `/` |
| `Descargar` | Igual que en la comparación; nombre `ortesis-v<n>.stl` |

Cada tarjeta muestra los parámetros que cambian respecto de la **primera**
versión seleccionada, la última URL STL disponible, las métricas y «n
intento(s); último: <estado>».

Los filtros `desde` y `hasta` combinan la fecha con `time.min` y `time.max` en
**UTC**, mientras la columna «Fecha» se muestra en la zona del servidor: el
filtrado y la visualización pueden diferir hasta un día.

## Componentes

### `PaginaComparacion`

- **`Index`:** botón de modo de color, `Sesion.Barra`, título y descripción;
  `Formulario` y `Vista` en una fila; `Lote` debajo.
- **`Formulario`:**
  - `Superficie` y selector de patrón.
  - Con `SOLID`: solo el espesor macizo.
  - Con otro patrón: celda, nervadura, capa continua (si está activa, piel y
    transición, y el «Espesor total en nervadura»; si no, «Rejilla abierta…»),
    giro, semilla (solo `VORONOI`), marco y banda.
  - Paso de superficie (no `SOLID`), «Invertir lado del espesor», un texto sobre
    voxel y resolución, el botón «Previsualizar» y `mensaje`.
- **`Superficie`:** interruptor de autoescala, `aviso_escala`, `rx.upload`
  (`accept` `.stl`/`.npz`, `max_files=1`, `max_size=50 MiB`) y los botones
  «Cargar archivo» y «Usar incluida», con el nombre, el detalle y el error.
- **`Vista`:** visor de 560 px y medidas de volumen, peso PETG y precio, con la
  nota «PETG a 0,15 por gramo…». Sin archivo muestra «La malla aparece aquí…».
- **`Lote`:**
  - cinco interruptores de patrón, el eje, y desde/hasta/cada;
  - «Probar con capa continua y sin ella» y «Generar lote»;
  - barra de progreso;
  - tabla con patrón, parámetros, volumen, peso, precio, aviso y los botones
    «Ver», «Comparar» y «STL»;
  - comparación con hasta 3 iframes de 320 px.
- **`Visor` y `Enlace`:** `iframe` con `src` =
  `/visor.html?src=<encodeURIComponent(object_url)>`. Usa `reflex_base.vars.base.Var`,
  una API interna de Reflex que puede cambiar entre versiones.
- **`Campo`, `Interruptor`, `Selector`, `Medida`:** primitivas. La etiqueta usa
  `as_="label"` sin `htmlFor` (A-20).

### `PaginaHistorial`

`Index` (barra, título, filtros, tabla, paginación y comparación), `Filtros`,
`Fecha` (`input type=date`), `Tabla`, `Fila` (botones Comparar/Quitar,
Restaurar, Reintentar y STL), `Comparacion` y `Tarjeta` (visor o «Sin STL
disponible.»).

### `Sesion`

- `Ruta(r)`: `api_url` + ruta.
- `Boton(texto, ruta, variante)`: un ancla con `reloadDocument`; sin ella, el
  enrutador mostraría su 404 en `/auth`.
- `Barra(autenticado?, nombre?)`: enlaces Comparar e Historial, el nombre y
  «Cerrar sesión», o bien «Iniciar sesión».

## Visor (`assets/visor.html`)

1. Lee `src` de la query. Si falta: «Genere una ortesis para verla aquí.».
2. Importa Three.js `0.169.0` desde unpkg, sin SRI (B-14).
3. `fetch(src)`:
   - un error de red muestra «No se pudo contactar con el almacén de
     archivos.»;
   - 403 o 404: «El STL ya no está en el almacén…»;
   - otro código: «No se pudo leer la malla generada.».
4. Parser STL binario: confía en el contador de la cabecera, no en la longitud
   (A-21). `computeVertexNormals` y la esfera envolvente.
5. Cámara orbital (arrastrar), zoom con la rueda (0,4–12 × el radio), luces
   ambiente, hemisférica y direccional, y `DoubleSide`.

Cada iframe crea un contexto WebGL; con 1 + 3 visores hay 4 contextos
simultáneos.

## Accesibilidad e internacionalización

- Todos los textos están en español y fijos en el código; no hay i18n, y
  `user_preferences.locale` (`es-CO` en el seed) no se usa en la UI.
- Los números se formatean con `GeneradorWeb.Numero` (punto de miles y coma
  decimal), sin depender del locale.
- El iframe tiene `title`. Las etiquetas no están asociadas a sus campos (A-20).
- Los errores no se marcan por campo; solo hay un mensaje global.
