"""add few columns to post table

Revision ID: ddc33dbaa574
Revises: 47e58a72e67a
Create Date: 2024-08-22 19:05:02.224812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddc33dbaa574'
down_revision: Union[str, None] = '47e58a72e67a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')
    ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
