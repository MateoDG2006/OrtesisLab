# Resoluciones

**Fecha:** 2026-11-12. **Cierre de `AUD-2026-10-13-001` (A-01…A-22):** ver
[RES-2026-11-12-ISSUE-9](2026-11-12-issue-9-seguimiento.md).

| Resolve | Estado | Alcance |
|---|---|---|
| [2026-11-12-resolve-cierre-issues-auditoria](2026-11-12-resolve-cierre-issues-auditoria.md) | EN_CURSO → autorización del plan | Edición autorizada |
| [issue-1](2026-11-12-issue-1-carga-presupuestos.md) | RESUELTO | A-01, A-03, A-11 |
| [issue-2](2026-11-12-issue-2-riesgo-stl-anonimo.md) | RIESGO_ACEPTADO | A-02 |
| [issue-3](2026-11-12-issue-3-normales-topologia.md) | RESUELTO | A-04…A-06, A-14, A-16, A-22 |
| [issue-4](2026-11-12-issue-4-validacion-exportacion.md) | RESUELTO | A-07, A-08, A-15 |
| [issue-5](2026-11-12-issue-5-rollback-stl-json.md) | RESUELTO | A-09, A-10 |
| [issue-6](2026-11-12-issue-6-cache-metricas.md) | RESUELTO | A-12, A-13 |
| [issue-7](2026-11-12-issue-7-contratos-wheel.md) | RESUELTO | A-17, A-18 |
| [issue-8](2026-11-12-issue-8-tests-visor-a11y.md) | RESUELTO | A-19…A-21 |
| [issue-9](2026-11-12-issue-9-seguimiento.md) | RESUELTO | Índice de seguimiento |
| [issue-b-indice](2026-11-12-issue-b-indice.md) | RESUELTO | AUD-2026-10-29-002 B-01…B-22 |
| [issue-b-cierre-parcial-a](2026-11-12-issue-b-cierre-parcial-a.md) | RESUELTO | B-05…B-13, B-15, B-19…B-22 |
| [issue-b-cierre-parcial-b](2026-11-12-issue-b-cierre-parcial-b.md) | RESUELTO | B-01…B-04, B-14, B-16…B-18 |
| [resolve-aud-2026-10-29](2026-11-12-resolve-aud-2026-10-29.md) | RESUELTO | Autorización y cierre B |
| [2026-11-12-resolve-quitar-seeds-test](2026-11-12-resolve-quitar-seeds-test.md) | EN_CURSO | Quitar fixture y base de pruebas |
| [2026-11-12-resolve-makefile](2026-11-12-resolve-makefile.md) | EN_CURSO | Objetivos de Make; no cierra hallazgos |
| [2026-11-12-resolve-revision-alembic](2026-11-12-resolve-revision-alembic.md) | EN_CURSO | Quitar la revisión que no generó Alembic |
| [2026-11-12-resolve-paquete-ortesislabplugin](2026-11-12-resolve-paquete-ortesislabplugin.md) | EN_CURSO | Imports del núcleo como `OrtesisLabPlugin` |

[RES-2026-10-13-001](2026-10-13-resolve-persistencia-postgres.md) y
[RES-2026-10-13-002](2026-10-13-resolve-organizar-pruebas.md) siguen como
trabajo previo `EN_CURSO` de persistencia y organización de pruebas.

[RES-2026-11-12-002](2026-11-12-resolve-simplificar-carga-yaml.md) autoriza
sustituir el `open` de `ConfiguracionBackend.Cargar` por `Path.read_text`.
Sigue en curso: no cierra B-09 ni desbloquea el archivo.

[RES-2026-11-12-003](2026-11-12-resolve-ajustes-entorno.md) autoriza quitar
`VariableFaltante`, `VariableInvalida` y `Ajustes.Faltante`. Sigue en curso:
no cierra la revisión de `apps/web/web/Ajustes.py`.

[RES-2026-11-12-004](2026-11-12-resolve-quitar-autoescala.md) autoriza quitar
el autoescalado de coordenadas. Sigue en curso y no cierra hallazgos.

## Protocolo

1. Identificar todas las auditorías que incluyan cada archivo y todos los
   hallazgos aplicables. Usar los inventarios e informes, no solo sus títulos.
2. Documentar la decisión y el alcance en un archivo
   `AAAA-MM-DD-resolve-<identificador>.md`.
3. Si se requiere editar un archivo bloqueado, obtener una instrucción explícita
   del usuario y registrarla antes de editar. Un resolve `EN_CURSO` sin esa
   instrucción no habilita cambios. No autoaprobar una excepción.
4. Ejecutar la corrección autorizada y las verificaciones indicadas, preservando
   datos originales y cambios ajenos. Registrar resultados reales, incluidos
   fallos y pruebas no ejecutadas.
5. Cerrar únicamente los archivos y hallazgos respaldados por la evidencia. Si
   queda un punto pendiente de cualquier auditoría, ese archivo sigue bloqueado
   para cambios generales.

## Plantilla orientativa

```markdown
# RES-AAAA-MM-DD-NNN — título

Fecha: AAAA-MM-DD (America/Bogota)
Auditorías: AUD-...
Estado: EN_CURSO | RESUELTO | DESCARTADO_CON_EVIDENCIA | RIESGO_ACEPTADO
Responsable: nombre o rol explícito

## Archivos y hallazgos

| Archivo desde la raíz | Hallazgos | SHA-256/revisión anterior | SHA-256/revisión verificada |
|---|---|---|---|
| ruta exacta | A-... o revisión sin hallazgos | ... | ... |

## Autorización para corregir (si había bloqueo)

Instrucción explícita del usuario, fecha, referencia y alcance autorizado.
No inventar autorización ni interpretar el silencio como aprobación.

## Decisión y trabajo realizado

Causa, tratamiento concreto y relación con cada hallazgo.
Un archivo sin hallazgos requiere una decisión explícita sobre su revisión.

## Verificación

Comandos, entorno, entradas, resultados observados y evidencias enlazadas.
Comparar el comportamiento antes/después y consignar pruebas no ejecutadas.

## Riesgo residual y cierre

Qué queda pendiente y qué archivos siguen bloqueados.
Para RIESGO_ACEPTADO: autorización explícita del usuario, motivo, controles,
responsable y fecha de revisión del riesgo.
```

No crear un resolve ficticio para cerrar esta auditoría documentalmente. El
informe inicial registra problemas existentes; no implementa sus correcciones.
