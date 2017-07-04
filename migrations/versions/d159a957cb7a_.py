"""empty message

Revision ID: d159a957cb7a
Revises: 419ddb3f4752
Create Date: 2017-07-01 16:28:14.439906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd159a957cb7a'
down_revision = '419ddb3f4752'
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