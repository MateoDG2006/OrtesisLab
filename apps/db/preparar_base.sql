-- Vuelve a crear el esquema y los permisos de ortesislab_dev después de
-- `make db-reset`. Los roles ya existen: son globales del clúster.
-- No crea tablas: el esquema lo aplica Alembic con el rol migrador.
REVOKE ALL ON DATABASE :"base" FROM PUBLIC;
GRANT CONNECT, TEMPORARY ON DATABASE :"base"
    TO ortesislab_migrator, ortesislab_app, ortesislab_worker, ortesislab_backup;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
CREATE SCHEMA ortesislab AUTHORIZATION ortesislab_migrator;
GRANT USAGE ON SCHEMA ortesislab TO ortesislab_app, ortesislab_worker, ortesislab_backup;
