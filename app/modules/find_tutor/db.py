from ..register.models import Profile
from .models import TutorProfile, Session, Tutor
from ..utils import Session_Maker


class TutorInfo:

    def __init__(self, row):
        self.first_name = row.Profile.firstName
        self.last_name = row.Profile.lastName
        self.phone_number = row.TutorProfile.phone_number
        self.id = row.Profile.account_id


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def find_tutors(self, topic_id, account_id):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            result = session.query(Tutor, Profile, TutorProfile).\
                        filter(Tutor.account_id == Profile.account_id).\
                        filter(Tutor.account_id == TutorProfile.account_id).\
                        filter(Tutor.account_id != account_id).\
                        filter(TutorProfile.is_available).\
                        filter(Tutor.topic_id == topic_id).all()

            tutors = [TutorInfo(row) for row in result]

            return tutors

    # Creates a session in the database
    def create_session(self, tutor_id, pupil_id, topic_id):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            s = Session(
                tutor_id=tutor_id,
                pupil_id=pupil_id,
                topic_id=topic_id,
                status='pending'
            )
            session.add(s)
            session.commit()

            return s.id
