"""purga del trabajador

Revision ID: b7c1d4e9a2f0
Revises: 0ea8eb9c0ca2
Create Date: 2026-11-12 11:35:00
"""

from collections.abc import Sequence

from alembic import op

revision: str = "b7c1d4e9a2f0"
down_revision: str | Sequence[str] | None = "0ea8eb9c0ca2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # La conciliación borra eventos y sesiones vencidas. La aplicación no recibe DELETE.
    op.execute(
        """
        GRANT DELETE ON history_events TO ortesislab_worker;
        GRANT DELETE ON auth_sessions TO ortesislab_worker;
        """
    )


def downgrade() -> None:
    op.execute(
        """
        REVOKE DELETE ON history_events FROM ortesislab_worker;
        REVOKE DELETE ON auth_sessions FROM ortesislab_worker;
        """
    )
