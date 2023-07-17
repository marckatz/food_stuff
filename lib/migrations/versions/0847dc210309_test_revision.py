"""test revision

Revision ID: 0847dc210309
Revises: daf0bd9abd22
Create Date: 2023-07-17 14:46:54.599727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0847dc210309'
down_revision = 'daf0bd9abd22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('new_column', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'new_column')
    # ### end Alembic commands ###