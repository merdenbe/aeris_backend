from falcon import HTTPUnauthorized

from .models import Token
from ..utils import utcnow_datetime_aware, Session_Maker


# Authenticates Request
def authenticate_request(req, Api_Session):
    value = req.get_header('Authorization')

    # Check existence of token
    if value is None:
        msg = 'Authorization required'
        raise HTTPUnauthorized('Unauthorized', msg)
    else:
        value = value.split(' ')[1]

    # Verify validity of token
    sm = Session_Maker(Api_Session)
    with sm as session:
        token = session.query(Token).filter(Token.value == value).first()

        # Check existence of token
        if token is None:
            msg = "Invalid token."
            raise HTTPUnauthorized("Invalid token", msg)

        # Check expiration of token
        if utcnow_datetime_aware() > token.expires_at:
            msg = "Expired token."
            raise HTTPUnauthorized("Expired token", msg)
