from .models import Topic
from ..utils import Session_Maker

from falcon import HTTPBadRequest


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def listTopics(self, course_id):
        # Get Majors
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            topics = session.query(Topic).filter(Topic.course_id == course_id).all()
            if len(topics) == 0:
                msg = "No topics associated with given course_id."
                raise HTTPBadRequest("No topics", msg)

            return [{"name": topic.name, "id": topic.id} for topic in topics]
