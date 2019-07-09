import binascii
import hashlib
import os
import uuid

from ..reauthenticate.models import Token, Account
from .models import Profile
from ..utils import Session_Maker


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Validates an email password combination
    def create_account(self, body):
        # Salt and hash password
        password = hash_password(body['password'])

        # Create account and profile
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            account = Account(
                password=password,
                email=body['email']
            )
            session.add(account)
            session.commit()

            profile = Profile(
                account_id=account.id,
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


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
