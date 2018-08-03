# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Table, Text
from sqlalchemy.ext.declarative import declarative_base

from run import db

Base = declarative_base()
metadata = Base.metadata


class Historical(db.Model):
    __tablename__ = 'historical'

    cust_id = Column(BigInteger, primary_key=True)
    customer_no = Column(Text)
    mobile = Column(Text)
    identity_type = Column(Text)
    customer_age = Column(BigInteger, nullable=False)
    gender = Column(Text)
    account_no = Column(Text)
    account_age_in_days = Column(Text)
    account_age_in_seconds = Column(Text)
    regis_year = Column(Text)
    regis_month = Column(Text)
    regis_weekday = Column(Text)
    tot_bal_duration = Column(BigInteger, nullable=False)
    max_bal_duration = Column(BigInteger, nullable=False)
    min_bal_duration = Column(BigInteger, nullable=False)
    avg_bal_duration = Column(Float(53), nullable=False)
    total_weighted_bal = Column(Float(53), nullable=False)
    avg_weighted_bal = Column(Float(53), nullable=False)
    tot_num_deposit = Column(BigInteger, nullable=False)
    total_deposit_amt = Column(Float(53), nullable=False)
    max_deposit_amt = Column(Float(53), nullable=False)
    min_deposit_amt = Column(Float(53), nullable=False)
    avg_deposit_amt = Column(Float(53), nullable=False)
    tot_num_withdrawal = Column(BigInteger, nullable=False)
    total_withdrawal_amt = Column(Float(53), nullable=False)
    min_withdrawal_amt = Column(Float(53), nullable=False)
    max_withdrawal_amt = Column(Float(53), nullable=False)
    avg_withdrawal_amt = Column(Float(53), nullable=False)
    avg_deposit_amount_per_day = Column(Float(53), nullable=False)
    avg_num_deposit_per_day = Column(Float(53), nullable=False)
    avg_withdrawal_amount_per_day = Column(Float(53), nullable=False)
    avg_num_withdrawal_per_day = Column(Float(53), nullable=False)
    last_deposit_amount = Column(Float(53), nullable=False)
    last_withdrawal_amount = Column(Float(53), nullable=False)
    time_since_last_deposit = Column(BigInteger, nullable=False)
    time_since_last_withdrawal = Column(BigInteger, nullable=False)
    balance = Column(Float(53), nullable=False)
    weighted_bal = Column(Float(53), nullable=False)


