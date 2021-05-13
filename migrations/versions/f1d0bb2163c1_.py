"""empty message

Revision ID: f1d0bb2163c1
Revises: 147ec7e4ecee
Create Date: 2021-05-11 05:39:25.427227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1d0bb2163c1'
down_revision = '147ec7e4ecee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('goal', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('goal', 'id')
    # ### end Alembic commands ###
