"""create coupons table

Revision ID: f9b29c077e12
Revises: e89afdcbc9db
Create Date: 2019-07-24 17:20:31.730537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b29c077e12'
down_revision = 'e89afdcbc9db'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "coupons",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_for', sa.Integer),
        sa.Column('redeemed_by', sa.Integer),
        sa.Column('value', sa.Float, nullable=False),
        sa.Column('code', sa.String(64), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('redeemed_at', sa.DateTime(timezone=True)),
        sa.Column('is_redeemed', sa.Boolean, nullable=False),
        sa.ForeignKeyConstraint(['created_for'], ['accounts.id'], ),
        sa.ForeignKeyConstraint(['redeemed_by'], ['accounts.id'], ),
    )


def downgrade():
    op.drop_table("coupons")
