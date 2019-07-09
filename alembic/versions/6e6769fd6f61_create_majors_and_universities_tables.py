"""create majors and universities tables

Revision ID: 6e6769fd6f61
Revises: a8e8bb7fa4be
Create Date: 2019-07-08 19:32:58.925195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e6769fd6f61'
down_revision = 'a8e8bb7fa4be'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'universities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(128), nullable=False)
    )

    op.create_table(
        'majors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('university_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['university_id'], ['universities.id'], ),
    )


def downgrade():
    op.drop_table('majors')
    op.drop_table('universities')
