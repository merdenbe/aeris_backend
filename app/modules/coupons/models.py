from ..utils import utcnow_datetime_aware

from datetime import timedelta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    Float,
    ForeignKeyConstraint
)


Base = declarative_base()


class Coupon(Base):
    ''' Stores coupon information '''

    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True)
    created_for = Column(Integer)
    redeemed_by = Column(Integer)

    value = Column(Float, nullable=False)

    code = Column(String(64), nullable=False)

    is_redeemed = Column(Boolean, nullable=False, default=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utcnow_datetime_aware()
    )
    expires_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=(utcnow_datetime_aware()+timedelta(weeks=12))
    )
    redeemed_at = Column(
        DateTime(timezone=True),
    )

    ForeignKeyConstraint(['created_for'], ['accounts.id'], )
    ForeignKeyConstraint(['redeemed_by'], ['accounts.id'], )
