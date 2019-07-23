from ..register.models import Profile
from ..utils import Session_Maker

from falcon import HTTPUnauthorized


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    def get_profile(self, account_id):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            profile = session.query(Profile).filter(Profile.account_id == account_id).first()
            if profile is None:
                msg = "Uknown account_id passed."
                raise HTTPUnauthorized("Bad account_id", msg)

            profile_dict = {
                'gradYear': str(profile.gradYear),
                'firstName': profile.firstName,
                'lasName': profile.lastName,
                'major': profile.major
            }

            return profile_dict

    def edit_profile(self, body):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            profile = session.query(Profile).filter(Profile.account_id == body["account_id"]).first()
            if profile is None:
                msg = "Uknown account_id passed."
                raise HTTPUnauthorized("Bad account_id", msg)

            profile.gradYear = body["gradYear"]
            profile.firstName = body["firstName"]
            profile.lastName = body["lastName"]
            profile.major = body["major"]

            session.commit()
