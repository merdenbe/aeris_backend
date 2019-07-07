from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Profile(Base):
    ''' Stores the username and password combinations '''

    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, ForeignKey("account.id"))
    gradYear = Column(Integer, nullable=False)

    major = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)