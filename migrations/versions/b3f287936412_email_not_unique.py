"""email not unique

Revision ID: b3f287936412
Revises: 06ea9353b862
Create Date: 2017-06-09 21:17:04.021248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3f287936412'
down_revision = '06ea9353b862'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_email_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    # ### end Alembic commands ###
