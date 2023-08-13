"""add content column to post table

Revision ID: 9b12cf05bea9
Revises: b716d06e12be
Create Date: 2023-08-12 21:45:47.509039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b12cf05bea9'
down_revision: Union[str, None] = 'b716d06e12be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
