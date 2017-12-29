"""empty message

Revision ID: 1758d84223ba
Revises: f7bf3d383920
Create Date: 2017-12-27 22:03:38.532863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1758d84223ba'
down_revision = 'f7bf3d383920'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('slug', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'category', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_column('category', 'slug')
    # ### end Alembic commands ###