from ..utils import utcnow_datetime_aware

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Enum,
    ForeignKeyConstraint,
    UniqueConstraint
)


Base = declarative_base()


class TutorProfile(Base):
    ''' Additional profile information for tutors only '''

    __tablename__ = "tutor_profiles"

    account_id = Column(Integer, primary_key=True)

    phone_number = Column(String(16), nullable=False)
    is_available = Column(Boolean, default=False, nullable=False, index=True)

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )


class Tutor(Base):
    ''' Stores relationship between a tutor and the topics they tutor '''

    __tablename__ = "tutors"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, nullable=False, index=True)
    topic_id = Column(Integer, nullable=False, index=True)

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )
    ForeignKeyConstraint(['topic_id'], ['accounts.id'], )

    UniqueConstraint('account_id', 'topic_id', name='uix_2')


class Session(Base):
    ''' Stores the information on a tutor session '''

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    tutor_id = Column(Integer, nullable=False, index=True)
    pupil_id = Column(Integer, nullable=False, index=True)
    topic_id = Column(Integer, nullable=False, index=True)

    tutor_logged_time = Column(Integer)
    pupil_logged_time = Column(Integer)
    rating = Column(Integer)

    created_at = Column(DateTime(timezone=True), nullable=False, default=utcnow_datetime_aware())
    completed_at = Column(DateTime(timezone=True))
    cancelled_at = Column(DateTime(timezone=True))

    status = Column(
        Enum(
            'pending',
            'cancelled',
            'incomplete',
            'complete',
            name='session_status'
        ),
        nullable=True
    )

    cancelled_by = Column(
        Enum(
            'tutor',
            'pupil',
            name='session_cancelled_by'
        ),
        nullable=True
    )

    ForeignKeyConstraint(['tutor_id'], ['accounts.id'], )
    ForeignKeyConstraint(['pupil_id'], ['accounts.id'], )
    ForeignKeyConstraint(['topic_id'], ['topics.id'], )
