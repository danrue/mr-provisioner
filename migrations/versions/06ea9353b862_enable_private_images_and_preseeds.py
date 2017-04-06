"""Enable private images and preseeds

Revision ID: 06ea9353b862
Revises: afb154b31046
Create Date: 2017-06-07 18:56:57.666548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ea9353b862'
down_revision = 'afb154b31046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('public', sa.Boolean(), nullable=False, server_default='false'))
    op.add_column('preseed', sa.Column('public', sa.Boolean(), nullable=False, server_default='false'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('preseed', 'public')
    op.drop_column('image', 'public')
    # ### end Alembic commands ###
