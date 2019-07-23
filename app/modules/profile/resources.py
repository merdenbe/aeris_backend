import ujson

from falcon import HTTPBadRequest

from .db import db
from ..reauthenticate.authenticate import authenticate_request


class ProfileResource:

    # Returns the profile info associated with an account_id
    def on_post(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        if body.keys() != {"account_id"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Grab profile
        profile = self.db.get_profile(body["account_id"])

        resp.media = {'profile': profile}

    def on_put(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        expected_params = {
            "account_id",
            "gradYear",
            "firstName",
            "lastName",
            "major"
        }

        if body.keys() != expected_params:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Edit profile
        self.db.edit_profile(body)

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
