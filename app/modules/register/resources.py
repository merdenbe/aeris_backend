import ujson

from falcon import HTTPBadRequest, HTTPUnauthorized

from .db import db


class RegisterResource:

    # Creates account and profile
    def on_post(self, req, resp):
        body = ujson.loads(req.stream.read())

        # Check request body
        if not is_valid(body):
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Create account
        account_id = self.db.create_account(body)



    def __init__(self, Api_Session):
        self.db = db(Api_Session)



def is_valid(body):
    necessaryParams = {
        'email',
        'password',
        'firstName',
        'lastName',
        'gradYear',
        'major'
    }
    passedParams = set(body.keys())

    return passedParams == necessaryParams