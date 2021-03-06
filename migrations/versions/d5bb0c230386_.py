"""empty message

Revision ID: d5bb0c230386
Revises: 
Create Date: 2017-11-22 20:53:34.092945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5bb0c230386'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('prject', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'projects', ['prject'], ['id'])
    op.drop_column('tasks', 'taskdesc')
    op.create_foreign_key(None, 'tstresults', 'projects', ['projects_id'], ['id'])
    op.create_foreign_key(None, 'users', 'works', ['work_id'], ['id'])
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'level')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('level', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'tstresults', type_='foreignkey')
    op.add_column('tasks', sa.Column('taskdesc', sa.VARCHAR(length=252), nullable=True))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'prject')
    # ### end Alembic commands ###
