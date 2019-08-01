from ..find_tutor.models import Session
from ..utils import utcnow_datetime_aware, Session_Maker

from falcon import HTTPBadRequest


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session


    def pupil_log_session(self, session_id, pupil_logged_time, rating):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            s = session.query(Session).filter(Session.id == session_id).first()
            if s is None:
                msg = "Session does not exist."
                raise HTTPBadRequest("Bad session_id", msg)

            s.pupil_logged_time = pupil_logged_time
            s.rating = rating
            s.status = 'incomplete'

            session.commit()