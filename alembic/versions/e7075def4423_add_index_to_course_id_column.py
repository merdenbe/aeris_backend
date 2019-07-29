"""add index to course_id column

Revision ID: e7075def4423
Revises: c85d4260172c
Create Date: 2019-07-29 14:53:29.477704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7075def4423'
down_revision = 'c85d4260172c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('topics_course_id', 'topics', ['course_id'])


def downgrade():
    op.drop_index('topics_course_id', table_name='topics')
