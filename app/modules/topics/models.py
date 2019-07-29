from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


Base = declarative_base()


class Topic(Base):
    ''' University information '''

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)

    name = Column(String(256), nullable=False)
    course_id = Column(Integer, nullable=False)

    ForeignKeyConstraint(['course_id'], ['courses.id'], )


class Course(Base):
    ''' Stores the courses of a university '''

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)

    name = Column(String(256), nullable=False)
    university_id = Column(Integer, nullable=False)

    ForeignKeyConstraint(['university_id'], ['universities.id'], )