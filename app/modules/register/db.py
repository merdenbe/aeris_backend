import binascii
import hashlib
import uuid

from falcon import HTTPUnauthorized

from .models import Token, Account
from ..utils import Session_Maker


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def create_account(self, body):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            account = Account(
                password=body['password'],
                email=body['email']
            )
            session.add(Account)
            session.commit()

            profile = Profile(
                id=account.id,
                firstName=body['firstName'],
                lastName=body['lastName'],
                gradYear=body['gradYear'],
                major=body['major']
            )
            session.add(profile)
            session.commit()

    # Generates and stores access token
    def generate_token(self):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            token = Token(value=str(uuid.uuid4()))
            session.add(token)
            session.commit()

            return token.value