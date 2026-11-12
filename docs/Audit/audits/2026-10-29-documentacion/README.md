# Documentación granular propuesta — AUD-2026-10-29-002

**Estado:** propuesta (`proposed`), redactada durante la auditoría
[AUD-2026-10-29-002](../2026-10-29-auditoria-evaluacion.md).
**Revisión descrita:** `e56df68` (`master`). **Responsable:** sin asignar.

Esta carpeta **no sustituye** a la documentación canónica de `docs/AppBackend`,
`docs/AppFrontend` y `docs/BlenderPlugin`, bloqueada por `AUD-2026-10-13-001`.
Lleva el detalle a nivel de función, campo, estado y clave de configuración
contrastado con el código. Para incorporarla a la documentación canónica hace
falta un resolve con autorización explícita del usuario.

Solo se describe el comportamiento implementado. Cuando el código actual no
funciona (por ejemplo, la importación rota de B-01), se describe lo que el código
intenta hacer y se marca el bloqueo.

## Mapa por áreas

| Área | Responsabilidad | Documentos |
|---|---|---|
| Identidad | Qué es OrtesisLab, para quién, alcance y requisitos observados | [identidad/proyecto.md](identidad/proyecto.md) |
| Backend | Configuración, persistencia, servicios, cola, almacenamiento, caché, autenticación | [configuracion](backend/configuracion.md), [persistencia](backend/persistencia.md), [servicios y flujos](backend/servicios-y-flujos.md), [integraciones](backend/integraciones.md) |
| Frontend | Estado Reflex, eventos, páginas, visor 3D | [frontend/estado-paginas-visor.md](frontend/estado-paginas-visor.md) |
| Núcleo y Blender | Geometría NumPy compartida y adaptadores Blender | [nucleo-blender/modulos.md](nucleo-blender/modulos.md) |
| Infraestructura | Compose local, roles PostgreSQL, bucket, Makefile, migraciones, respaldo | [infraestructura/entorno-local.md](infraestructura/entorno-local.md) |
| Calidad | Pruebas, estándares y herramientas | [calidad/pruebas-y-estandares.md](calidad/pruebas-y-estandares.md) |
| Transversal | Archivo por archivo, y lo que falta | [cobertura-fuentes.md](cobertura-fuentes.md), [faltantes.md](faltantes.md) |

No se crean las áreas `ai/`, `notebooks/`, `data/` ni `hardware/`. El proyecto no
entrena ni infiere modelos ni tiene notebooks, y no contiene firmware: el
sketch de micrófono mencionado en la auditoría anterior está fuera del
repositorio. Los datos de entrada (superficies) se tratan en backend
(imports) y en el núcleo (validación).

## Cómo leer las fichas de función

Cada función se describe con:

- **E** (entrada): parámetros y unidades.
- **P** (proceso): qué hace y bajo qué transacción o bloqueo.
- **S** (salida): resultado.
- **Err** (errores): excepciones esperadas.
- **Ef** (efectos): filas, objetos, eventos o caché que modifica.

Las líneas citadas son de `e56df68`.

## Relación con la documentación canónica

| Canónico | Qué añade esta propuesta |
|---|---|
| `AppBackend/ARQUITECTURA.md` | Máquinas de estado completas, matriz de fallos por paso, transacciones exactas |
| `AppBackend/MODULOS.md` | Ficha E/P/S/Err/Ef de cada método público de servicios y repositorios |
| `AppBackend/CONTRATOS.md` | Corrección de `mode` (`sweep`), DTO campo a campo, eventos de historial con su emisor y carga útil |
| `AppBackend/OPERACION_Y_PRUEBAS.md` | Línea base de pruebas actual, configuración con su lector y su momento de lectura |
| `AppFrontend/*` | Variables de estado una a una, eventos con su efecto y sus mensajes |
| `BlenderPlugin/*` | Catálogo de funciones del núcleo y contrato de `Model3DForPrinting` |
