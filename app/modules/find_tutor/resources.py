import ujson

from falcon import HTTPBadRequest

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

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session
