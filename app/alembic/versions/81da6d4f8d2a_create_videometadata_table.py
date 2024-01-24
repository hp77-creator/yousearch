"""create_videometadata_table

Revision ID: 81da6d4f8d2a
Revises: 
Create Date: 2024-01-24 09:19:41.715213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81da6d4f8d2a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videometadata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('published_date', sa.DateTime(), nullable=True),
    sa.Column('thumbnail_url', sa.String(), nullable=True),
    sa.Column('channel_url', sa.String(), nullable=True),
    sa.Column('channel_title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_videometadata_id'), 'videometadata', ['id'], unique=False)
    op.create_index(op.f('ix_videometadata_title'), 'videometadata', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_videometadata_title'), table_name='videometadata')
    op.drop_index(op.f('ix_videometadata_id'), table_name='videometadata')
    op.drop_table('videometadata')
    # ### end Alembic commands ###