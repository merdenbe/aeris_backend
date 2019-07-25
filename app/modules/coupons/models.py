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

class Balance(Base):
    ''' Stores the balances of accounts '''

    __tablename__ = "balances"

    account_id = Column(Integer, primary_key=True)

    value = Column(Float, nullable=False, default=0.0)

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utcnow_datetime_aware()
    )

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )

class BalanceTransaction(Base):
    ''' Stores a transaction for every change made to the balances table '''

    __tablename__ = "balance_log"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, nullable=False)

    old_value = Column(Float, nullable=False)
    new_value = Column(Float, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=utcnow_datetime_aware()
    )

    ForeignKeyConstraint(['account_id'], ['accounts.id'], )