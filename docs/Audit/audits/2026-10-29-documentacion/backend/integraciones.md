# Backend · Integraciones: bucket S3, Redis, lector de superficies, OIDC

**Estado:** propuesta. **Archivos:** `web/storage/**`, `web/cache/CacheRedis.py`,
`web/LectorSuperficie.py`, `web/services/AutenticacionOidc.py`,
`infra/database/minio/**`.

## Bucket S3 (`web/storage/`)

### Protocolo `AlmacenamientoPrivado`

| Método | Contrato |
|---|---|
| `Url(clave)` | `<s3_public_url o endpoint>/<bucket>/<quote(clave)>`, sin firma |
| `Publicar(clave, datos, media, sha, nombre?)` | `put_object` con `ContentType`, metadato `sha256` y `Content-Disposition: attachment; filename="…"` si hay nombre. Después `head_object` comprueba la longitud y el SHA. Devuelve la URL. Errores: `AlmacenamientoNoDisponible` |
| `Leer(clave)` | Cuerpo completo en memoria. `ObjetoAusente` (404, `NoSuchKey`, `NotFound`) o `AlmacenamientoNoDisponible` |
| `Existe(clave)` | `head_object` → `bool` |
| `Borrar(clave)` | `delete_object` |
| `Claves(prefijo)` | Paginador `list_objects_v2` → `(clave, LastModified)` |

### `Almacen` (fábrica por proceso)

- `Actual()`: crea `StorageS3.DesdeAjustes()` la primera vez.
- `Usar(x)`: sustitución para pruebas.
- `Clave(user_id, asset_id, stl_publico)`: `usuarios/<u>/assets/<a>[.stl]`.
- `Sha256(bytes)`.
- `LeerVerificado(clave, sha)`: si el hash difiere, `ObjetoAusente`.

`PATRON_CLAVE` acepta UUID en minúsculas con sufijo `.stl` opcional. El sufijo
`.stl` es lo único que hace pública una clave.

### Cliente (`StorageS3`)

boto3 síncrono con direccionamiento por ruta. Timeouts de 3 s de conexión y
30 s de lectura, con 3 intentos en modo `standard`. Se llama desde hilos, nunca
dentro de una transacción.

### Política y cuentas (MinIO)

| Archivo | Concede |
|---|---|
| `politica-lectura-stl.json` | `s3:GetObject` anónimo en `usuarios/*/assets/*.stl` |
| `politica-aplicacion.json` | Cuenta de servicio: `Get`, `Put` y `DeleteObject` en el bucket; `ListBucket` y `GetBucketLocation` |
| `inicializar.sh` | `mc mb`, la política anónima, la política de aplicación y el usuario de servicio. El `attach` se ejecuta con `\|\| true`, de modo que un error no se detecta |

CORS: `MINIO_API_CORS_ALLOW_ORIGIN` es `http://localhost:3000,http://127.0.0.1:3000`
por defecto. Web y trabajador usan las mismas credenciales, sin separación por
rol.

### Objetos por tipo

| Tipo (`TipoAsset`) | Clave | Media | Pública | Productor |
|---|---|---|---|---|
| `import_original` | `…/<id>` | `model/stl` o `application/x-npz` | No | `ServicioImports` |
| `surface_npz` | `…/<id>` | `application/x-npz` | No | `ServicioImports` |
| `result_stl` | `…/<id>.stl` | `model/stl` | **Sí** | Trabajador |
| `export_json` | `…/<id>` | `application/json` | No | Trabajador |

## Caché Redis (`web/cache/CacheRedis.py`)

| Clave | Contenido | Escritor |
|---|---|---|
| `ortesislab:superficie:cruda:<sha_npz>` | NPZ sin comprimir `a0..a3` (vértices, caras, normales, borde) | `GeneradorWeb.Cruda`, `ServicioImports._Registrar` |
| `…:refinada:<sha>:<repr(paso)>:<0/1>` | Tupla refinada | `_SuperficieRefinadaConDiagnostico` |
| `…:diagnostico:<sha>:<0/1>[:<repr(paso)>]` | JSON del diagnóstico de escala | ídem |

- TTL de 7 días; `maxmemory 256mb` con `allkeys-lru` en Compose.
- Un `RedisError` apaga la caché 30 s en **ese proceso**.
- Un dato corrupto en `LeerTupla` devuelve `None`. En `LeerDiagnostico`, el
  `json.loads` no está protegido: un valor corrupto lanzaría `JSONDecodeError`.
- El SHA identifica el contenido, no el nombre. Dos usuarios con el mismo NPZ
  comparten la entrada; es seguro porque el contenido es idéntico.

## Lector de superficies (`web/LectorSuperficie.py`)

`Preparar(nombre, contenido, autoescalar=True) -> ((p, f, n, borde), info)`:

1. Extensión `.stl` o `.npz`; contenido no vacío y ≤ 50 MiB. Si no,
   `ArchivoSuperficieIlegible`.
2. STL:
   - binario si `84 + 50·n == len`; si no, ASCII (UTF-8 estricto, líneas
     `vertex x y z`, múltiplo de 3);
   - fusión por `round(coord / clip_snap_mm)` con `np.unique` (tolerancia en mm
     antes de corregir unidades, A-16);
   - normales por áreas.
3. NPZ: rechaza si la suma de `file_size` **declarados** supera 128 MiB. Después
   `np.load(allow_pickle=False)` con `vertices`, `faces` y `normals` (A-01: las
   cabeceras NPY pueden reservar más).
4. Coordenadas finitas; `EscalaMalla.Resolver`; factor aplicado si
   `autoescalar`.
5. `AnalizadorMalla.Preparar(..., suavizarNormales=False)`: topología y borde.

`info` contiene `nombre`, `vertices`, `caras`, `dimensiones` («x × y × z mm»),
`factor_escala` y `aviso`. La ruta web llama con `autoescalar=False`.

## OIDC y sesión

| Elemento | Valor |
|---|---|
| Proveedor de desarrollo | `ghcr.io/navikt/mock-oauth2-server:2.2.1`, perfil `auth-dev`, `interactiveLogin: true`; no es un IdP real |
| Cookie de identidad | `ortesislab_sesion`: token aleatorio de 32 bytes; la base guarda el SHA-256 |
| Cookie de intercambio | `ortesislab_oidc`, firmada con `ORTESISLAB_SESSION_SECRET`, 600 s |
| Revalidación | Cada evento Reflex con datos llama a `Requerir`, sin caché de sesión (una transacción por evento) |
| Rotación y purga | Token nuevo en cada inicio de sesión; las filas vencidas no se purgan (B-13) |
| Cuenta desactivada | `ResolverSesion` exige `status = active`; las sesiones existentes dejan de valer de inmediato |

Amenazas consideradas en el código: el navegador nunca envía `user_id`; un
recurso ajeno responde igual que uno inexistente; el token no se guarda en
claro. No consideradas: CSRF de logout y origen de WebSocket (B-15), y tasa de
inicio de sesión (B-05).
