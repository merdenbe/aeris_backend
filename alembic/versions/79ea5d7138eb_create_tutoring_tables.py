"""create tutoring tables

Revision ID: 79ea5d7138eb
Revises: e7075def4423
Create Date: 2019-07-30 16:29:27.450386

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '79ea5d7138eb'
down_revision = 'e7075def4423'
branch_labels = None
depends_on = None


def upgrade():
    # Create tutor_profiles table
    op.create_table(
        "tutor_profiles",
        sa.Column('account_id', sa.Integer, primary_key=True),
        sa.Column('phone_number', sa.String(16), nullable=False),
        sa.Column('is_available', sa.Boolean, nullable=False),

        sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    )

    # Set tutor_profile indexes
    op.create_index('tutor_profiles_is_available', 'tutor_profiles', ['is_available'])

    # Create tutors table
    op.create_table(
        "tutors",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('account_id', sa.Integer, nullable=False),
        sa.Column('topic_id', sa.Integer, nullable=False),

        sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ),

        sa.UniqueConstraint('account_id', 'topic_id', name='uix_2')
    )

    # Set tutors indexes
    op.create_index('tutors_account_id', 'tutors', ['account_id'])
    op.create_index('tutors_topic_id', 'tutors', ['topic_id'])

    # Create sessions table
    op.create_table(
        "sessions",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tutor_id', sa.Integer, nullable=False),
        sa.Column('pupil_id', sa.Integer, nullable=False),
        sa.Column('topic_id', sa.Integer, nullable=False),
        sa.Column('tutor_logged_time', sa.Integer),
        sa.Column('pupil_logged_time', sa.Integer),
        sa.Column('rating', sa.Integer),

        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('completed_at', sa.DateTime(timezone=True)),
        sa.Column('cancelled_at', sa.DateTime(timezone=True)),

        sa.Column('status', sa.Enum('pending', 'cancelled', 'incomplete', 'complete', name='session_status'), nullable=True),
        sa.Column('cancelled_by', sa.Enum('tutor', 'pupil', name='session_cancelled_by'), nullable=True),

        sa.ForeignKeyConstraint(['tutor_id'], ['accounts.id'], ),
        sa.ForeignKeyConstraint(['pupil_id'], ['accounts.id'], ),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ),
    )

    # Set session indexes
    op.create_index('sessions_tutor_id', 'sessions', ['tutor_id'])
    op.create_index('sessions_pupil_id', 'sessions', ['pupil_id'])
    op.create_index('sessions_topic_id', 'sessions', ['topic_id'])


def downgrade():
    # Dop tables
    op.drop_table("tutor_profiles")
    op.drop_table("tutors")
    op.drop_table("sessions")

    # Drop sessions Enums
    session_status = postgresql.ENUM('pending', 'cancelled', 'incomplete', 'complete', name='session_status')
    session_status.drop(op.get_bind())
    session_cancelled_by = postgresql.ENUM('tutor', 'pupil', name='session_cancelled_by')
    session_cancelled_by.drop(op.get_bind())
