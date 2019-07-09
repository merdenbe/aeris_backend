from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


Base = declarative_base()


class Major(Base):
    ''' Stores the majors of a univeristy '''

    __tablename__ = "majors"

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)
    university_id = Column(Integer, nullable=False)

    ForeignKeyConstraint(['university_id'], ['universities.id'], )


class University(Base):
    ''' University information '''

    __tablename__ = "universities"

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)
