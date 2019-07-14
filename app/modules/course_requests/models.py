from ..utils import utcnow_datetime_aware

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKeyConstraint,
    UniqueConstraint
)


Base = declarative_base()


class CourseRequest(Base):
    ''' Stores the a request for a new course '''

    __tablename__ = "course_requests"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, nullable=False)

    title = Column(String(256), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=utcnow_datetime_aware())

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )
    UniqueConstraint('account_id', 'title', name='uix_1')
