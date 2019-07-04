import ujson

from falcon import HTTPBadRequest, HTTPUnauthorized

from .db import db


class ReauthenticateResource:

    # Checks email/password combination and generates a token if verified
    def on_post(self, req, resp):
        body = ujson.loads(req.stream.read())

        # Check body parameters
        password = body.get("password")
        email = body.get("email")
        if password is None or email is None:
            msg = "Must provide email and password."
            raise HTTPBadRequest("Bad Request", msg)

        # Validate email password combination
        valid_combo = self.db.validate(email, password)
        if not valid_combo:
            msg = "Invalid username/password combination."
            raise HTTPUnauthorized("Unauthorized", msg)

        resp.media = {'token': self.db.generate_token()}

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
