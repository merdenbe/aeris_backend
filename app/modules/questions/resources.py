import os
import ujson

from falcon import HTTPBadRequest

from .db import db
from ..reauthenticate.authenticate import authenticate_request
from ..utils import send_email


class QuestionResource:

    # Return a list of majors for a given university
    def on_get(self, req, resp):
        authenticate_request(req, self.Api_Session)

        questions = self.db.listQuestions()

        resp.media = {'questions': questions}

    # Emails the company about the question
    def on_post(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check Parameters
        if body.keys() != {"question", "user_email"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Prepare email body
        email_body = compose_email(body["question"], body["user_email"])

        # Send email
        send_email(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"],
            os.environ["EMAIL_ADDRESS"],
            'Question',
            email_body
        )

    def __init__(self, Api_Session):
        self.db = db(Api_Session)
        self.Api_Session = Api_Session


def compose_email(question, user_email):
    email_body = 'Hi Michael,\n\nI had a question:\n\n' + question + '\n\nFrom\n' + user_email

    return email_body
