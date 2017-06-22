"""empty message

Revision ID: be1e91c45e81
Revises: 6f2d7dcd8ef9
Create Date: 2017-06-22 14:20:50.277037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be1e91c45e81'
down_revision = '6f2d7dcd8ef9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'flag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('flag', mysql.VARCHAR(length=2), nullable=True))
    # ### end Alembic commands ###