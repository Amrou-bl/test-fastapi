"""add content column to posts table

Revision ID: 038a09d87b2e
Revises: 05b5cb647831
Create Date: 2024-08-22 18:43:06.944350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '038a09d87b2e'
down_revision: Union[str, None] = '05b5cb647831'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
