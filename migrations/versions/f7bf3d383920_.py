"""empty message

Revision ID: f7bf3d383920
Revises: e7a1311fb434
Create Date: 2017-12-26 15:16:28.996678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7bf3d383920'
down_revision = 'e7a1311fb434'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_category',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE')
    )
    op.add_column('user', sa.Column('role', sa.Enum('admin', 'member'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    op.drop_table('post_category')
    # ### end Alembic commands ###