from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


Base = declarative_base()


class Profile(Base):
    ''' Stores the username and password combinations '''

    __tablename__ = "profiles"

    account_id = Column(Integer, primary_key=True)
    gradYear = Column(Integer, nullable=False)

    major = Column(String(128), nullable=False)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )
