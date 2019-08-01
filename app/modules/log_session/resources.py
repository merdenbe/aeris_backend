import ujson

from falcon import HTTPBadRequest

from .db import db
from ..reauthenticate.authenticate import authenticate_request


class LogSessionResource:

    # Cancels a session
    def on_put(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        if body.keys() != {"session_id", "pupil_logged_time", "rating"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        self.db.pupil_log_session(body["session_id"], body["pupil_logged_time"], body["rating"])

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
