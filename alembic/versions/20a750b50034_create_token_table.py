"""create token table

Revision ID: 20a750b50034
Revises: 5b96019a16a1
Create Date: 2019-07-02 15:53:14.981738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a750b50034'
down_revision = '5b96019a16a1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tokens',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
    )


def downgrade():
    op.drop_table('tokens')
