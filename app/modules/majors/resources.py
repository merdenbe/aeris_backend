from .db import db
from ..reauthenticate.authenticate import authenticate_request


class MajorResource:

    # Return a list of majors for a given university
    def on_get(self, req, resp):
        authenticate_request(req, self.Api_Session)

        majors = self.db.listMajors()

        resp.media = {'majors': majors}

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
