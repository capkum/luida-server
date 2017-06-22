"""empty message

Revision ID: 0b52df29be48
Revises: be1e91c45e81
Create Date: 2017-06-22 22:51:19.252255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0b52df29be48'
down_revision = 'be1e91c45e81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'passwd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('passwd', mysql.VARCHAR(length=20), nullable=False))
    # ### end Alembic commands ###
