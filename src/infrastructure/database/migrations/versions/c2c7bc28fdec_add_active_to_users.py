"""add active to users

Revision ID: c2c7bc28fdec
Revises: f676baa22f91
Create Date: 2026-07-02 01:29:38.365350

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c2c7bc28fdec"
down_revision: Union[str, Sequence[str], None] = "f676baa22f91"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "active")