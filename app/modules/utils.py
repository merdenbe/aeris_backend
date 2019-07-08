import arrow
import uuid

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

