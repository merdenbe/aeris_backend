from .db import db
from ..reauthenticate.authenticate import authenticate_request


class TopicResource:

    # Return a list of majors for a given university
    def on_get(self, req, resp, course_id):
        authenticate_request(req, self.Api_Session)

        topics = self.db.listTopics(course_id)

        resp.media = {'topics': topics}

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
