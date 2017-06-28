"""empty message

Revision ID: b648729c1973
Revises: 235ff38bff85
Create Date: 2017-06-28 12:26:48.009982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b648729c1973'
down_revision = '235ff38bff85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('evnt_point', sa.Integer(), nullable=True))
    op.add_column('accounts', sa.Column('point', sa.Integer(), nullable=True))
    op.add_column('accounts', sa.Column('profile_img', sa.String(length=255), nullable=True))
    op.add_column('accounts', sa.Column('voice', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'voice')
    op.drop_column('accounts', 'profile_img')
    op.drop_column('accounts', 'point')
    op.drop_column('accounts', 'evnt_point')
    # ### end Alembic commands ###
