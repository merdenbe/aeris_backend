"""create topics and courses table

Revision ID: c85d4260172c
Revises: f9b29c077e12
Create Date: 2019-07-29 06:44:25.472438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c85d4260172c'
down_revision = 'f9b29c077e12'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "courses",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(256), nullable=False),
        sa.Column('university_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['university_id'], ['universities.id'], ),
    )
    op.create_table(
        "topics",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(256), nullable=False),
        sa.Column('course_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    )


def downgrade():
    op.drop_table("topics")
    op.drop_table("courses")
