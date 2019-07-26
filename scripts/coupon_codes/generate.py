#!/usr/bin/env python

import os
import sys
import argparse
import uuid
import arrow

from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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


# Retunrns current utc datetime
def utcnow_datetime_aware():
    """Returns a timezone-aware datetime for the current UTC moment."""

    return arrow.utcnow().datetime

# Generates a coupon code
def gen_code():
    broken_code = str(uuid.uuid4()).split('-')
    reformed_code = ''.join(broken_code)
    final_code = reformed_code[:4] + '-' + reformed_code[4:8] + '-' + reformed_code[8:12] + '-' + reformed_code[12:16]

    return final_code


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


# Main Execution
if __name__ == "__main__":

    # Process command line args
    parser = argparse.ArgumentParser(description="Generates coupon codes in the database.")

    parser.add_argument('-v', '--value',
        action='store', dest='coupon_value',help="value of coupons",
        type=float, default=100, required=False
    )

    parser.add_argument('-a', '--account_id',
        action='store', dest='account_id', default=None,
        help="account_id the coupons are attached to", type=int, required=False
    )

    parser.add_argument('-n', '--number',
        action='store', dest='num_coupons',
        help="number of coupons to be created", type=int, required=True
    )

    args = parser.parse_args()

    # Initialize SQLalchemy connection
    engine = create_engine(os.environ["DATABASE_URL"], echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    print('[LOG]: connected to database')

    print('[LOG]: generating coupons...')
    for _ in range(args.num_coupons):
        c = Coupon(
            created_for=args.account_id,
            value=args.coupon_value,
            code=gen_code()
        )
        session.add(c)
        session.commit()

    # Garbage collection
    session.close()
    engine.dispose()
    print('[LOG]: closed dependencies')

    print('[LOG]: complete.')