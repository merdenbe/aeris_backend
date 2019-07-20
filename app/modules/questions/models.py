from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Question(Base):
    ''' Stores the questions for the FAQ '''

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    content = Column(String(512), nullable=False)
    answer = Column(String(512), nullable=False)