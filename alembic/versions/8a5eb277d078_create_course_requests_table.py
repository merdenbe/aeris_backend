"""create course_requests table

Revision ID: 8a5eb277d078
Revises: 6e6769fd6f61
Create Date: 2019-07-13 15:53:24.308821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5eb277d078'
down_revision = '6e6769fd6f61'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "course_requests",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('account_id', sa.Integer, nullable=False),
        sa.Column('title', sa.String(256), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
        sa.UniqueConstraint('account_id', 'title', name='uix_1')
    )


def downgrade():
    op.drop_table("course_requests")
