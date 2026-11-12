# RES-2026-11-12-008 — El núcleo se importa como `OrtesisLabPlugin`

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001 y AUD-2026-10-29-002. Varios archivos de `web/`, `scripts/` y pruebas figuran en esos inventarios con la ruta anterior al monorepo.
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12, al fallar `make web` en `from GenerateModelsApp.util.Utilidades import Registro`:

> «Ya no se llama mas asi el modulo»

Alcance autorizado: que el código y la documentación vigente importen y empaqueten el complemento con el nombre de la carpeta que está en disco, `OrtesisLabPlugin`. No se renombra `web/GenerateModelsApp.py`, ni `app_module_import`, ni el archivo `GenerateModelsApp.zip`. No se cierran hallazgos.

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | Decisión |
|---|---|---|
| `apps/web/web/*.py` que importaban el núcleo, `apps/web/rxconfig.py` | Inventarios de ambas auditorías; hallazgos de cada archivo siguen abiertos | Sustituir el import y corregir `sys.path` hacia `apps/ortesis-plugin` |
| `scripts/EmpaquetarBlender.py`, `scripts/EjecutarOrtesisLab.py`, `scripts/IniciarConsola.py`, `src/generatemodelsapp/__init__.py`, `pyproject.toml` | Revisión de empaquetado y entrada de consola | Carpeta fuente y prefijo interno del ZIP: `OrtesisLabPlugin`. El `.zip` conserva el nombre |
| Pruebas en `tests/` que importaban `GenerateModelsApp` | Revisión de pruebas | Mismo nombre de paquete |
| Documentación canónica que citaba el paquete antiguo | B-17 donde aplique | Frases que quedarían falsas. No se reescriben informes de `docs/Audit/audits/` ni el historial de `REGISTRO_CAMBIOS.md` |

## Decisión

La carpeta del complemento ya es `apps/ortesis-plugin/OrtesisLabPlugin`. Los imports seguían el nombre anterior y `rxconfig.py` añadía `apps/apps/ortesis-plugin` al path. Los hallazgos no se cierran.

## Verificación

Se completa en el registro de cambios de esta entrega.

## Riesgo residual y cierre

Los archivos siguen bloqueados para cualquier otro cambio. Una instalación de Blender hecha con un ZIP cuyo directorio raíz era `GenerateModelsApp` hay que reinstalarla: el módulo dentro del ZIP pasa a llamarse `OrtesisLabPlugin`.
