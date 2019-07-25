import ujson

from falcon import HTTPBadRequest

from ..reauthenticate.authenticate import authenticate_request
from .db import db

class CouponResource:

    def on_put(self, req, resp):
        authenticate_request(req, self.Api_Session)

        try:
            body = ujson.loads(req.stream.read())
        except ValueError:
            msg = "Must send request body."
            raise HTTPBadRequest("Bad Request", msg)

        # Check request parameters
        if body.keys() != {"account_id", "coupon_code"}:
            msg = "Missing or incorrect parameters."
            raise HTTPBadRequest("Bad Request", msg)

        # Find coupon value
        coupon_value = self.db.get_coupon_value(body["account_id"], body["coupon_code"])

        # Update balance
        updated_balance = self.db.add_coupon_value(account_id, coupon_value)

        return resp.media = {
            "coupon_value": coupon_value,
            "updated_balance": updated_balance
        }

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session
        self.db = db(Api_Session)
