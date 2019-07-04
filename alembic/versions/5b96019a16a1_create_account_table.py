"""create account table

Revision ID: 5b96019a16a1
Revises:
Create Date: 2019-07-02 06:34:57.236042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b96019a16a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(256), nullable=False),
        sa.Column('password', sa.String(256), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    )


def downgrade():
    op.drop_table('accounts')