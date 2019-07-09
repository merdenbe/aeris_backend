import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint


Base = declarative_base()


# Tables used in script
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


# Main Execution
if __name__ == "__main__":
    csv = './NDMajors.csv'
    print('[LOG]: opening csv')
    with open(csv) as c:
        # Read in file
        majors = [line.strip() for line in c.readlines()]

        # Open database connection
        print('[LOG]: connecting to database')
        Api_Engine = create_engine(os.environ["DATABASE_URL"], echo=False)
        Api_Session = sessionmaker(bind=Api_Engine)
        session = Api_Session()

        # Insert majors into the db, even ""Film, Television, and Theatre"""
        print('[LOG]: inserting majors into database')
        or major in majors:
            if major == "\"Film, Television, and Theatre\"":
                major = "Film, Television, and Theatre"
            m = Major(name=major, university_id=1)
            session.add(m)
            session.commit()

        # Close session and dispose connection
        print('[LOG]: closing dependencies')
        session.close()
        Api_Engine.dispose()

    print('[LOG]: complete.')