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
    def validate(self, email, password):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            account = session.query(Account).filter(Account.email == email).first()
            if account is None:
                msg = "Email address is not in the system."
                raise HTTPUnauthorized("Email not found", msg)

            return verify_password(account.password, password)

    # Generates and stores access token
    def generate_token(self):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            token = Token(value=str(uuid.uuid4()))
            session.add(token)
            session.commit()

            return token.value


# Verify a stored password against one provided by user
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
