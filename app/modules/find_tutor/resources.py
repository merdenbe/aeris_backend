import ujson
import random

from falcon import HTTPBadRequest, HTTPFailedDependency

from .db import db
from ..reauthenticate.authenticate import authenticate_request


class FindTutorResource:

    # Sends email to feedback email address
    def on_post(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check Parameters
        if body.keys() != {"topic_id", "account_id"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Get list of possible tutors
        tutors = self.db.find_tutors(body["topic_id"], body["account_id"])
        if len(tutors) == 0:
            msg = "No available tutors on that topic."
            raise HTTPFailedDependency("No tutors", msg)

        # Select random tutor
        tutor = random.choice(tutors)

        # Create session
        session_id = self.db.create_session(tutor.id, body["account_id"], body["topic_id"])

        resp.media = {
            "session_id": session_id,
            "first_name": tutor.first_name,
            "last_name": tutor.last_name,
            "phone_number": tutor.phone_number
        }

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
