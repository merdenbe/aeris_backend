from ..find_tutor.models import Session
from ..utils import utcnow_datetime_aware, Session_Maker

from falcon import HTTPBadRequest


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session


    def cancel_session(self, session_id):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            s = session.query(Session).filter(Session.id == session_id).first()
            if s is None:
                msg = "Session does not exist."
                raise HTTPBadRequest("Bad session_id", msg)

            s.cancelled_at = utcnow_datetime_aware()
            s.status = 'cancelled'
            s.cancelled_by = 'pupil'

            session.commit()