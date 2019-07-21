"""create questions table

Revision ID: e89afdcbc9db
Revises: 8a5eb277d078
Create Date: 2019-07-20 14:41:36.129291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e89afdcbc9db'
down_revision = '8a5eb277d078'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('content', sa.String(512), nullable=False),
        sa.Column('answer', sa.String(512), nullable=False)
    )


def downgrade():
    op.drop_table('questions')
