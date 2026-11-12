"""Esquema inicial ortesislab: tablas, trigger de versiones y GRANT."""

from collections.abc import Sequence

from alembic import op

revision: str = "f8e2a91c0b3d"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

ESQUEMA = "ortesislab"

SQL_TRIGGER = """
CREATE FUNCTION model_versions_comprobar() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM imports
        WHERE id = NEW.import_id AND user_id = NEW.user_id AND status = 'ready'
    ) THEN
        RAISE EXCEPTION 'La versión requiere un import ready del mismo usuario'
            USING ERRCODE = 'check_violation';
    END IF;
    IF NEW.parent_version_id IS NOT NULL AND NOT EXISTS (
        SELECT 1 FROM model_versions
        WHERE id = NEW.parent_version_id AND version_number < NEW.version_number
    ) THEN
        RAISE EXCEPTION 'El padre debe ser una versión anterior del proyecto'
            USING ERRCODE = 'check_violation';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER model_versions_comprobar_trg BEFORE INSERT ON model_versions
    FOR EACH ROW EXECUTE FUNCTION model_versions_comprobar();
"""

SQL_GRANTS = """
GRANT SELECT, INSERT, UPDATE ON app_users, user_preferences, auth_sessions, file_assets, projects, imports TO ortesislab_app;
GRANT SELECT, INSERT ON model_versions TO ortesislab_app;
GRANT SELECT, INSERT, UPDATE ON generation_batches, batch_items TO ortesislab_app;
GRANT SELECT ON generation_attempts, generation_results, exports TO ortesislab_app;
GRANT SELECT, INSERT ON history_events TO ortesislab_app;
GRANT SELECT ON app_users, projects, imports, model_versions TO ortesislab_worker;
GRANT SELECT, UPDATE ON generation_batches, batch_items TO ortesislab_worker;
GRANT SELECT, INSERT, UPDATE ON generation_attempts, file_assets, exports TO ortesislab_worker;
GRANT SELECT, INSERT ON generation_results TO ortesislab_worker;
GRANT SELECT, INSERT ON history_events TO ortesislab_worker;
"""

SQL_REVOKE = """
REVOKE ALL ON ALL TABLES IN SCHEMA ortesislab FROM ortesislab_app, ortesislab_worker;
"""


def upgrade() -> None:
    from web.persistence.Modelos import Base

    bind = op.get_bind()
    bind.exec_driver_sql(f"SET search_path TO {ESQUEMA}")
    # use_alter en batch_items_winning_attempt_fk: create_all aplica la FK en un segundo paso.
    Base.metadata.create_all(bind=bind)
    op.execute(SQL_TRIGGER)
    op.execute(SQL_GRANTS)


def downgrade() -> None:
    from web.persistence.Modelos import Base

    bind = op.get_bind()
    bind.exec_driver_sql(f"SET search_path TO {ESQUEMA}")
    op.execute(SQL_REVOKE)
    bind.exec_driver_sql(
        "DROP TRIGGER IF EXISTS model_versions_comprobar_trg ON model_versions"
    )
    bind.exec_driver_sql("DROP FUNCTION IF EXISTS model_versions_comprobar()")
    op.drop_constraint(
        "batch_items_winning_attempt_fk",
        "batch_items",
        type_="foreignkey",
    )
    Base.metadata.drop_all(bind=bind)
