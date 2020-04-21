"""create card table

Revision ID: d1e7191b312b
Revises: fcdc38469f1b
Create Date: 2020-04-21 16:03:10.637096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1e7191b312b'
down_revision = 'fcdc38469f1b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'card',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'))
    )


def downgrade():
    op.drop_table('card')
