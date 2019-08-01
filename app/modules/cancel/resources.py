import ujson

from falcon import HTTPBadRequest

from .db import db
from ..reauthenticate.authenticate import authenticate_request


class CancelResource:

    # Cancels a session
    def on_put(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        if body.keys() != {"session_id"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        self.db.cancel_session(body["session_id"])

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session

