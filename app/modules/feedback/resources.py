import os
import ujson
import smtplib

from falcon import HTTPBadRequest, HTTPFailedDependency

from ..reauthenticate.authenticate import authenticate_request


class FeedbackResource:

    # Sends email to feedback email address
    def on_post(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check Parameters
        if body.keys() != {"msg"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Send email
        send_email(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"],
            os.environ["EMAIL_ADDRESS"],
            'User Feedback',
            body['msg']
        )

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    except Exception as e:
        raise HTTPFailedDependency("Failed to send email", str(e))
