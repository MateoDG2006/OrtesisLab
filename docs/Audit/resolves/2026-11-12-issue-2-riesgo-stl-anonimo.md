# RES-2026-11-12-ISSUE-2 — Lectura anónima del STL (A-02 / B-14 parcial)

Fecha: 2026-11-12 (America/Bogota)
Auditorías: AUD-2026-10-13-001, AUD-2026-10-29-002
Estado: RIESGO_ACEPTADO
Responsable: agente de implementación
Issues: #2

## Autorización explícita del riesgo

Instrucción del usuario al planificar el cierre de issues (2026-11-12):

> Opción elegida: «Aceptar el riesgo: la URL anónima del STL se mantiene y se
> documenta como RIESGO_ACEPTADO, con controles y fecha de revisión.»

Fecha de revisión del riesgo: **2027-05-12**.

## Hallazgo

A-02 (y tramo STL de B-14): quien conoce `object_url` de un STL de resultado
(`usuarios/*/assets/*.stl`) puede leerlo sin sesión. Originales, NPZ y JSON
siguen privados.

## Controles que permanecen

1. Solo claves con sufijo `.stl` tienen `s3:GetObject` anónimo
   (`infra/database/minio/politica-lectura-stl.json`).
2. Originales, NPZ y JSON exigen credenciales del backend.
3. La clave incluye dos UUID; no se listan públicamente.
4. Una superficie nueva no se escribe en `uploaded_files/` servido por Reflex
   (`Almacen.Clave` + `ServicioImports`).
5. `scripts/MigrarSubidas.py` solo traslada el directorio histórico.

## Verificación

```
.venv\Scripts\python.exe -m unittest tests.persistencia.test_superficie_no_estatica tests.e2e.test_dos_sesiones -v
```

(si la base de pruebas no está disponible, los casos de persistencia se omiten;
los E2E de contrato de política pasan sin base).

## Riesgo residual

Quien obtenga o adivine la URL del STL puede descargarlo. Revisión obligatoria
en 2027-05-12 o antes si cambia el modelo de amenaza.
