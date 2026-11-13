"""select de sesiones para el trabajador

Revision ID: c4d8e1a90b27
Revises: b7c1d4e9a2f0
Create Date: 2026-11-12 17:16:00
"""

from collections.abc import Sequence

from alembic import op

revision: str = "c4d8e1a90b27"
down_revision: str | Sequence[str] | None = "b7c1d4e9a2f0"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # El DELETE de la purga filtra por expires_at y revoked_at: PostgreSQL exige SELECT.
    op.execute("GRANT SELECT ON ortesislab.auth_sessions TO ortesislab_worker")


def downgrade() -> None:
    op.execute("REVOKE SELECT ON ortesislab.auth_sessions FROM ortesislab_worker")
