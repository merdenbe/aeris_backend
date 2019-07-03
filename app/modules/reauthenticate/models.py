from ..utils import utcnow_datetime_aware

from datetime import timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class Account(Base):
    ''' Stores the username and password combinations '''

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)

    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=utcnow_datetime_aware())


class Token(Base):
    ''' Authentication token for API access '''

    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)

    value = Column(String(64), nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False, default=utcnow_datetime_aware())
    expires_at = Column(DateTime(timezone=True), nullable=False, default=(utcnow_datetime_aware()+timedelta(weeks=12)))