# Identidad del proyecto

**Estado:** propuesta. **Fuente:** `README.md`, `pyproject.toml`, código en `e56df68`.

## Qué es

OrtesisLab (repositorio `GenerateModelsApp`) genera la **geometría paramétrica
de una ortesis** a partir de una superficie interior abierta. Esa superficie es
la piel del paciente, sin espesor, y está expresada en milímetros. Sobre ella
se aplica un patrón de nervaduras (Voronoi, hexagonal, rombos, cuadrícula o
macizo), una capa continua opcional, un marco perimetral y una banda de
refuerzo, y se obtiene un cascarón imprimible.

Hay dos productos independientes que comparten el núcleo NumPy
`GenerateModelsApp/` y no se llaman entre sí:

| Producto | Usuario | Qué hace | Qué no hace |
|---|---|---|---|
| Complemento Blender 1.3.0 (`GenerateModelsApp.zip`) | Técnico en Blender 5.x | Genera, reconstruye con voxel, valida y exporta STL y sidecar JSON | No persiste ni comparte trabajo |
| Aplicación web Reflex | Usuario autenticado por OIDC | Sube superficies, genera variantes en lote, compara hasta 3, calcula volumen, peso y precio PETG, y guarda historial y versiones | No hace voxel ni validación final (`validation_status = not_checked`) |

## Tipo de proyecto y objetivos

El repositorio no declara si es un proyecto comercial, de investigación o
interno: `pyproject.toml` conserva la descripción de plantilla. **Cuestión
abierta:** el responsable debe declararlo, porque cambia los requisitos
(regulación de dispositivos médicos, privacidad, SLA).

Objetivos que se pueden inferir del código. Son **observados, no confirmados**:

1. Generar variantes geométricas reproducibles. Cada versión guarda parámetros
   canónicos, su SHA-256, la instantánea del material y la escala.
2. Comparar variantes por métricas de material antes de imprimir.
3. Aislar el trabajo por usuario: propiedad por `user_id` y FK compuestas.
4. Mantener la equivalencia entre el núcleo Blender y la web. Las pruebas
   `tests/nucleo` comparan con un cálculo de referencia.

## Alcance

- **Dentro:** superficie STL/NPZ abierta, conectada y orientada; patrones del
  catálogo; métricas del cascarón previo al voxel; lotes de hasta 12 variantes;
  historial, restauración y reintento.
- **Fuera (implementado como tal):** reconstrucción voxel en la web; validación
  de imprimibilidad en la web; soportes, relleno, merma, tiempo de máquina,
  moneda; resistencia mecánica; despliegue en la nube, TLS y CI de pruebas.

## Requisitos observados

Se presentan como trazabilidad y no son requisitos aprobados.

| ID | Requisito observado | Dónde se implementa | Evidencia de prueba |
|---|---|---|---|
| RQ-01 | Toda operación con datos exige sesión de servidor válida | `ContextoUsuario.Requerir` | `test_propiedad_datos.SesionesDeServidor` (omitida sin base) |
| RQ-02 | Un usuario no lee ni referencia recursos de otro | Filtros `user_id`, FK compuestas, `_DelUsuario` | `test_propiedad_datos.PropiedadDeRecursos` (omitida) |
| RQ-03 | Un lote se admite una sola vez por `request_id` | `ServicioLotes.Solicitar` | `test_lotes_trabajador` (no carga, B-01) |
| RQ-04 | Máximo 3 lotes pendientes y 12 ítems | `persistencia.yaml`, `CHECK` | ídem |
| RQ-05 | Un fallo de ítem no detiene el lote; hasta 3 intentos | `ServicioLotes.Fallar`, `Liberar` | ídem |
| RQ-06 | La superficie debe ser abierta, conectada y orientada, de una capa | `AnalizadorMalla.Preparar` | `tests/geometria/test_superficie_abierta.py` (pasa) |
| RQ-07 | Unidades en mm, con autoescala decimal opcional | `EscalaMalla` | `tests/geometria/test_escala_malla.py` (pasa) |
| RQ-08 | Volumen, peso y precio con PETG 1,27 g/cm³ y 0,15 por gramo | `Materials.py`, `Modeling.py` | `tests/nucleo/test_nucleo.py` (pasa) |
| RQ-09 | Los archivos privados no se exponen; el STL de resultado se lee por URL | Política MinIO | Sin prueba automatizada |

## Terminología confirmada en el código

| Término | Significado en el código |
|---|---|
| Superficie / base | Malla triangular abierta interior, en mm |
| Cascarón | Sólido resultante tras recortar el patrón y dar espesor (`Cascaron.Engrosar`) |
| Import | Fila `imports`: original subido y su NPZ normalizado |
| Versión | Fila inmutable `model_versions` con los parámetros de una variante |
| Lote / ítem / intento | `generation_batches` / `batch_items` / `generation_attempts` |
| Lease | Reserva temporal de un ítem por un trabajador (`lease_token`, `lease_expires_at`) |
| Plantilla | `assets/superficie_interior_mm.npz`, registrada como import propio de cada usuario |
| `pre_voxel_shell` | Alcance geométrico de las métricas web: el cascarón antes del voxel |
