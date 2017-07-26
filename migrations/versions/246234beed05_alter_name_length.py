"""alter name length

Revision ID: 246234beed05
Revises: c3c9da07c55d
Create Date: 2017-07-14 22:10:39.619489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '246234beed05'
down_revision = 'c3c9da07c55d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'name',
                    existing_type=mysql.VARCHAR(length=30),
                    type_=sa.String(length=60),
                    existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'name',
                    existing_type=sa.String(length=60),
                    type_=mysql.VARCHAR(length=30),
                    existing_nullable=False)
    # ### end Alembic commands ###
