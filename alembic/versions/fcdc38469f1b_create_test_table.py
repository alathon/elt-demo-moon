"""create user table

Revision ID: fcdc38469f1b
Revises: 
Create Date: 2020-04-21 13:57:59.056223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcdc38469f1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

def downgrade():
    op.delete_table('user')
