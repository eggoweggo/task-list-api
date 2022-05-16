"""empty message

Revision ID: 21150f4a87ed
Revises: f7d7f2e862ff
Create Date: 2022-05-16 03:10:34.445140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21150f4a87ed'
down_revision = 'f7d7f2e862ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
