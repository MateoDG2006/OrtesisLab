# Auditorías

**Fecha:** 2026-11-12.

| ID | Informe | Alcance | Estado |
|---|---|---|---|
| `AUD-2026-10-13-001` | [Auditoría de toda la base de código](2026-10-13-auditoria-base-codigo.md) | Núcleo, Blender, web, scripts, pruebas, configuración y artefactos versionados | **CERRADA** (A-01…A-22) — [índice](../resolves/2026-11-12-issue-9-seguimiento.md) |
| `AUD-2026-10-29-002` | [Auditoría y evaluación del proyecto](2026-10-29-auditoria-evaluacion.md) | 181 archivos versionados en `e56df68` (salvo `docs/Audit` y `.agents`): backend persistente, frontend, núcleo, infraestructura, pruebas y documentación | **CERRADA** (B-01…B-22) — [índice](../resolves/2026-11-12-issue-b-indice.md), [adenda](2026-10-29-adenda-cierre-b.md) |

Evidencias de `AUD-2026-10-29-002` (añadido el 2026-10-29):

- [Inventario con huellas, hallazgos por archivo y bloqueo](2026-10-29-inventario.json).
- [Comandos ejecutados y resultados](2026-10-29-evidencias.json).
- [Documentación granular propuesta y aspectos faltantes](2026-10-29-documentacion/README.md).
- [Adenda de cierre B-01…B-22](2026-10-29-adenda-cierre-b.md) (2026-11-12).

Evidencias de la revisión:

- [Inventario con huellas y estado por archivo](2026-10-13-inventario.json).
- [Resultados de las comprobaciones adicionales](2026-10-13-evidencias.json).
- [Discrepancia entre validación y exportación Blender](2026-10-13-export-evidence.json).

Las rutas de código del informe son relativas a la raíz del repositorio y las
líneas corresponden a esta fecha. Consultar también los símbolos y huellas para
evitar atribuir un hallazgo a otra revisión. No considerar los logs históricos
del repositorio como pruebas ejecutadas en una nueva auditoría.
