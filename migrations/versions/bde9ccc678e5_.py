"""empty message

Revision ID: bde9ccc678e5
Revises: d054fd8553a2
Create Date: 2017-07-01 16:30:30.073844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bde9ccc678e5'
down_revision = 'd054fd8553a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('device_id', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'device_id')
    # ### end Alembic commands ###
