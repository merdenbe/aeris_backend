"""create profiles table

Revision ID: a8e8bb7fa4be
Revises: 20a750b50034
Create Date: 2019-07-08 06:16:51.290884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e8bb7fa4be'
down_revision = '20a750b50034'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'profiles',
        sa.Column('account_id', sa.Integer, primary_key=True),
        sa.Column('gradYear', sa.Integer, nullable=False),
        sa.Column('major', sa.String(128), nullable=False),
        sa.Column('firstName', sa.String(50), nullable=False),
        sa.Column('lastName', sa.String(50), nullable=False),
        sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    )


def downgrade():
    op.drop_table('profiles')
