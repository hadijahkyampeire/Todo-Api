"""empty message

Revision ID: 895138467a23
Revises: 
Create Date: 2018-04-04 15:42:11.981296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '895138467a23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('day', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_name'), 'todo', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_name'), table_name='todo')
    op.drop_table('todo')
    # ### end Alembic commands ###
