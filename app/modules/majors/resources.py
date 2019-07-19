from .db import db


class MajorResource:

    # Return a list of majors for a given university
    def on_get(self, req, resp):
        majors = self.db.listMajors()

        resp.media = {'majors': majors}

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session
