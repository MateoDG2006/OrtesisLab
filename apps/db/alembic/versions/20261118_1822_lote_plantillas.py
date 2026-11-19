"""lote_plantillas

Revision ID: a1b2c3d4e5f6
Revises: c4d8e1a90b27
Create Date: 2026-11-18 18:22:00
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "a1b2c3d4e5f6"
down_revision: str | Sequence[str] | None = "c4d8e1a90b27"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "lote_plantillas",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("nombre", sa.Text(), nullable=False),
        sa.Column(
            "payload",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("char_length(nombre) BETWEEN 1 AND 120", name="lote_plantillas_nombre_check"),
        sa.CheckConstraint("jsonb_typeof(payload) = 'object'", name="lote_plantillas_payload_check"),
        sa.ForeignKeyConstraint(["user_id"], ["app_users.id"], name=op.f("lote_plantillas_user_id_fkey")),
        sa.PrimaryKeyConstraint("id", name=op.f("lote_plantillas_pkey")),
        sa.UniqueConstraint("user_id", "nombre", name="lote_plantillas_user_nombre_key"),
        sa.UniqueConstraint("user_id", "id", name="lote_plantillas_user_id_uk"),
    )
    op.create_index(
        "lote_plantillas_user_updated_idx",
        "lote_plantillas",
        ["user_id", sa.literal_column("updated_at DESC")],
        unique=False,
    )
    op.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON lote_plantillas TO ortesislab_app")


def downgrade() -> None:
    op.execute("REVOKE ALL ON TABLE lote_plantillas FROM ortesislab_app")
    op.drop_index("lote_plantillas_user_updated_idx", table_name="lote_plantillas")
    op.drop_table("lote_plantillas")
