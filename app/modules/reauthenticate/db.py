import binascii
import hashlib
import binascii
import os
import uuid

from .models import Token, Account
from ..utils import Session_Maker


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    def validate(email, password):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            account = session.query(Account).filter(Account.email == email).first()
            return verify_password(account.password, password)

    def generate_token(self):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            # Generate token
            token = Token(value=str(uuid.uuid4()))

            # Store token
            session.add(token)
            session.commit()

            return token.value


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
