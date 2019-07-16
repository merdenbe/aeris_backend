import ujson

from falcon import HTTPBadRequest
from profanity import profanity

from .db import db
from ..reauthenticate.authenticate import authenticate_request


class CourseRequestResource:

    # Return a set of all previously requested courses
    def on_get(self, req, resp):
        authenticate_request(req, self.Api_Session)

        requested_courses = self.db.get_requested_courses()

        resp.media = {"requested_courses": requested_courses}

    # Create a new course request
    def on_post(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        if body.keys() != {"account_id", "title"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Check for profanity
        if profanity.contains_profanity(body["title"]):
            msg = "Contains profanity."
            raise HTTPBadRequest("Bad Request", msg)

        # Insert into database
        self.db.create_course_request(body["title"], body["account_id"])

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
