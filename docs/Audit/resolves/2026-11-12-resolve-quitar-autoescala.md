# RES-2026-11-12-004 — Quitar el autoescalado de coordenadas

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: EN_CURSO
Responsable: agente de implementación, por instrucción del usuario

## Autorización para corregir

Instrucción explícita del usuario, 2026-11-12, sobre `EstadoApp.set_autoescalar_superficie` y el resto del repositorio:

> «Revisa todo el repositorio en busca de la logica de autoescalado y eliminala, es un problema de datos crudos que no debe de ser contemplado en este caso, los datos que vienen son los que se mantienen»

Alcance autorizado: eliminar la decisión y la aplicación de un factor decimal sobre las coordenadas de entrada, en la web, el núcleo y el complemento de Blender, incluidas la casilla, la preferencia y las pruebas que solo cubrían esa corrección. Las coordenadas del archivo se usan tal como llegan. Arreglar sigue horneando la escala del objeto de Blender en los vértices. Las columnas `user_preferences.auto_scale` y `model_versions.auto_scale` permanecen en el esquema para no exigir una migración en esta entrega; la generación no las lee y cada versión nueva se inserta con `false`.

Los hallazgos de ambas auditorías siguen abiertos. Esta autorización no desbloquea otros cambios.

## Verificación

Se completa en el registro de cambios de esta entrega.
