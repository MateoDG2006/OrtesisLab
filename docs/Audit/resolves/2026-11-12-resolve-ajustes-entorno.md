# RES-2026-11-12-003 — Aviso de clave ausente dentro de `Variable.__get__`

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12, señalando
`VariableFaltante`, `VariableInvalida`, `Ajustes.cookie_secure` y
`Ajustes.Faltante` en `Ajustes.py`:

> «Todas estas clases y funciones son innecesarias si dentro de variable
> agregamos dentro de la funcion get simplemente una advertencia que la llave
> falta»

Alcance autorizado: en `apps/web/web/Ajustes.py` (el inventario de la auditoría
lo registra como `web/Ajustes.py`; el archivo vive ahora bajo `apps/web`) quitar
las dos clases de error y `Faltante`. El texto de clave ausente y el de prefijo
incorrecto quedan en `Variable.__get__` y la lectura sigue deteniendo el proceso
con `RuntimeError`. `cookie_secure` no entra en el borrado: convierte la cadena
del entorno en bool para las cookies. En
`tests/persistencia/apoyo_persistencia.py` solo se sustituye la llamada a
`Faltante` por la captura de ese `RuntimeError`. No cierra la revisión pendiente
de `AUD-2026-10-29-002`.

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | SHA-256 anterior | SHA-256 verificada |
|---|---|---|---|
| `apps/web/web/Ajustes.py` | Revisión pendiente, sin hallazgos individuales | `10cf732d7551c50d8e9ad278edb655e87e4e3c599aa1f3b53d1010290672e583` | `a8fa4a1c722f8a6f634555e66910737f8d341118a3d1bdacbec5ceb693fa7a25` |
| `tests/persistencia/apoyo_persistencia.py` | Revisión pendiente, sin hallazgos individuales | `356281ead7052a8e803964876e45b3099e5e07518016c2b9b6e3d9b5b9e92797` | `fc4d3d74f7d98e1651b3ff4d1dc2685295c3c0ea6558db5b9deb4509b10d43c5` |

## Decisión y trabajo realizado

Las clases solo nombraban el mismo `RuntimeError`. El mensaje queda en
`Variable.__get__`. No se sustituye por `warnings.warn`: una clave obligatoria
vacía (secreto de sesión, URL, OIDC) no puede seguir como cadena vacía.

## Verificación

`py -3` con `PYTHONPATH=apps/web`, sin imprimir valores del `.env`:

- `Ajustes({}).session_secret` y `database_url` lanzan `RuntimeError` «Falta la variable de entorno …».
- `postgresql://` lanza `RuntimeError` con el prefijo `postgresql+psycopg://`.
- URL correcta, `cookie_secure` con `TRUE` y ausente, Redis vacío, `app_url` y bucket vacío usan el valor o el defecto declarados.

`python docs/Agents/Scripts/GenerarIndices.py` y `--comprobar`: catálogos al día. No se ejecutaron las pruebas de persistencia ni el arranque de la web. La revisión de `AUD-2026-10-29-002` sigue abierta.
