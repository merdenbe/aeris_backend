from .models import Coupon
from ..utils import utcnow_datetime_aware, Session_Maker

from falcon import HTTPBadRequest


class db:

    def __init__(self, Api_Session):
        self.Api_Session = Api_Session

    # Creates course request
    def get_coupon_value(self, account_id, coupon_code):
        sm = Session_Maker(self.Api_Session)
        with sm as session:
            coupon = session.query(Coupon).filter(Coupon.code == coupon_code).first()
            if coupon is None:
                msg = "Coupon code not found."
                raise HTTPBadRequest("Invalid coupon", msg)

            if utcnow_datetime_aware() > coupon.expires_at:
                msg = "The coupon has expired."
                raise HTTPBadRequest("Expired coupon", msg)

            if coupon.is_redeemed:
                msg = "The coupon has already been used."
                raise HTTPBadRequest("Used coupon", msg)

            if coupon.created_for is not None and coupon.created_for != account_id:
                msg = "This coupon was created for another user."
                raise HTTPBadRequest("Incorrect user", msg)

            coupon.is_redeemed = True
            coupon.redeemed_by = account_id
            coupon.redeemed_at = utcnow_datetime_aware()
            session.commit()

            return coupon.value
