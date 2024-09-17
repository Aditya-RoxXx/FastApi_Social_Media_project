"""add last few columns to posts table

Revision ID: fe6386379d7b
Revises: feea9cbeee66
Create Date: 2024-09-17 16:08:40.051240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe6386379d7b'
down_revision: Union[str, None] = 'feea9cbeee66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default=sa.text('true')),)
     op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
