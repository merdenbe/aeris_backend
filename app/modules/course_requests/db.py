from .models import CourseRequest
from ..utils import Session_Maker

from falcon import HTTPBadRequest


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Creates course request
    def create_course_request(self, title, account_id):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            try:
                cr = CourseRequest(title=title, account_id=account_id)
                session.add(cr)
                session.commit()
            except Exception as e:
                msg = "Could not insert into database."
                raise HTTPBadRequest("DB Exception", msg)

    # Return set of requested course titles
    def get_requested_courses(self):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            rows = session.query(CourseRequest).all()
            requested_courses = list({row.title for row in rows})

            return requested_courses