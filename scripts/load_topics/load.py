import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


Base = declarative_base()


# Tables used in script
class Course(Base):
    ''' Stores the courses of a university '''

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)

    name = Column(String(256), nullable=False)
    university_id = Column(Integer, nullable=False)

    ForeignKeyConstraint(['university_id'], ['universities.id'], )


class Topic(Base):
    ''' University information '''

    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)

    name = Column(String(256), nullable=False)
    course_id = Column(Integer, nullable=False)

    ForeignKeyConstraint(['course_id'], ['courses.id'], )


# Main Execution
if __name__ == "__main__":
    csv = './fund_comp_topics.csv'
    print('[LOG]: opening csv')
    with open(csv) as c:
        # Read in file
        topics = [line.strip() for line in c.readlines()]

        # Open database connection
        print('[LOG]: connecting to database')
        Api_Engine = create_engine(os.environ["DATABASE_URL"], echo=False)
        Api_Session = sessionmaker(bind=Api_Engine)
        session = Api_Session()

        # Inserting course
        c = Course(name="Fundamentals of Computing", university_id=1)
        session.add(c)
        session.commit()
        print('[LOG]: inserted course into database')

        # Insert majors into the db, even ""Film, Television, and Theatre"""
        print('[LOG]: inserting topics into database')
        for topic in topics:
            t = Topic(name=topic, course_id=c.id)
            session.add(t)
            session.commit()

        # Close session and dispose connection
        print('[LOG]: closing dependencies')
        session.close()
        Api_Engine.dispose()

    print('[LOG]: complete.')