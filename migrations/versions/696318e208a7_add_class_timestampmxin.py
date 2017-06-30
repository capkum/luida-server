"""add class TimestampMxin

Revision ID: 696318e208a7
Revises: b648729c1973
Create Date: 2017-06-29 17:13:43.100418

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '696318e208a7'
down_revision = 'b648729c1973'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column(
        'updated_at', sa.DateTime(), nullable=True))
    op.alter_column('accounts', 'created_at',
                    existing_type=mysql.DATETIME(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'created_at',
                    existing_type=mysql.DATETIME(),
                    nullable=False)
    op.drop_column('accounts', 'updated_at')
    # ### end Alembic commands ###