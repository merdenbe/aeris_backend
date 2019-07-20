import ujson

from falcon import HTTPBadRequest

from .db import db


class ReauthenticateResource:

    # Checks email/password combination and generates a token if verified
    def on_post(self, req, resp):
        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check body parameters
        password = body.get("password")
        email = body.get("email")
        if password is None or email is None:
            msg = "Must provide email and password."
            raise HTTPBadRequest("Bad Request", msg)

        # Validate email password combination
        account_id = self.db.validate(email, password)

        resp.media = {'account_id': account_id, 'token': self.db.generate_token()}

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
