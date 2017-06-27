"""account 속성 변경

Revision ID: 4ef9c8fd0bb7
Revises: 3bd57d4d1ecf
Create Date: 2017-06-27 18:33:35.023543

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ef9c8fd0bb7'
down_revision = '3bd57d4d1ecf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('accounts', 'email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.alter_column('accounts', 'name',
               existing_type=mysql.VARCHAR(length=12),
               nullable=True)
    op.alter_column('accounts', 'nickname',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('accounts', 'passwd',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'passwd',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.alter_column('accounts', 'nickname',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('accounts', 'name',
               existing_type=mysql.VARCHAR(length=12),
               nullable=False)
    op.alter_column('accounts', 'email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    op.alter_column('accounts', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
