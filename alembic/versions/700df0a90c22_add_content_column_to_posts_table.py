"""add content column to posts table

Revision ID: 700df0a90c22
Revises: 7ba3d2389e92
Create Date: 2024-09-16 21:44:37.229715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '700df0a90c22'
down_revision: Union[str, None] = '7ba3d2389e92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
