"""empty message

Revision ID: e7a1311fb434
Revises: 
Create Date: 2017-12-25 22:51:17.161422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7a1311fb434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=16), nullable=False),
    sa.Column('last_name', sa.String(length=16), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('time_updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('slug', sa.String(length=250), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('content_md', sa.Text(), nullable=False),
    sa.Column('status', sa.Enum('public', 'private', 'draft', 'trash'), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('time_updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('post_category',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_category')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
