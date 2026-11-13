# Configuración compartida

Límites, tiempos, tamaños y etiquetas versionados. Las URL y los secretos no están aquí: van en el `.env` de la raíz y los lee `Ajustes`.

Los YAML los carga `ConfiguracionBackend.Cargar("<area>")` al importar el módulo que los usa. Un archivo o una clave ausente tumba ese proceso. Un cambio pide reiniciar la web y el trabajador.

Los JSON los lee el núcleo (`Configuracion` en el complemento). El empaquetado los copia dentro del ZIP, en `OrtesisLabPlugin/config/`, porque Blender no ve esta carpeta y su Python no trae PyYAML.

## YAML del backend

| Archivo | Para qué sirve |
|---|---|
| [almacen.yaml](almacen.yaml) | Timeouts e intentos del cliente S3 (`StorageS3`). |
| [cache.yaml](cache.yaml) | TTL, pausa tras un fallo, timeout y tamaño máximo de una superficie en Redis (`CacheRedis`). |
| [persistencia.yaml](persistencia.yaml) | Conexión a PostgreSQL, tope de lotes pendientes, reintentos, página del historial, cuotas de importación y plazos de purga. Un lote no tiene tope de variantes; `generation_batches.total_items` solo exige al menos una. |
| [sesion.yaml](sesion.yaml) | Duración de la sesión de servidor. |
| [trabajador.yaml](trabajador.yaml) | Lease, latido, supervisión y conciliación del trabajador, la estimación de segundos por variante que muestra la página, y los plazos del conciliador de archivos. `latido_s` tiene que ser bastante menor que `lease_s`. |
| [web.yaml](web.yaml) | Cada cuánto se consulta el progreso, la espera máxima al crear una variante, el tamaño máximo de una superficie subida las etiquetas de patrones, ejes y estados y la ayuda (`ayudas`) que la página muestra junto a cada parámetro. Las claves de esas etiquetas son las del núcleo y de `EstadoItem`; el YAML solo guarda el texto visible y el orden de los selectores. |

## JSON de geometría

| Archivo | Para qué sirve |
|---|---|
| [parametros_defecto.json](parametros_defecto.json) | Valores iniciales de las 17 opciones geométricas. Los usan la web y el complemento al abrir un trabajo nuevo. |
| [limites.json](limites.json) | Umbrales, tolerancias y presupuestos del algoritmo (celda mínima, caras, suavizado, caché de malla refinada). No son preferencias de la página. |
| [comprobacion_geometrica.json](comprobacion_geometrica.json) | Mediciones ya hechas de dos ejemplos. Sirven de referencia; no son umbrales de rechazo. |
| [registro.json](registro.json) | Nivel de la consola, nivel del archivo y nombre del log del complemento (`ortesislab.log`). |
