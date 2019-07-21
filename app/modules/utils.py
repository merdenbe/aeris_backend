import arrow
import smtplib

from falcon import HTTPFailedDependency


# Sends an email
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


# Retunrns current utc datetime
def utcnow_datetime_aware():
    """Returns a timezone-aware datetime for the current UTC moment."""

    return arrow.utcnow().datetime


# Session Maker Context Manager
class Session_Maker():

    def __init__(self, sm):
        self.session = sm()

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
