# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from run import db

Base = declarative_base()
metadata = Base.metadata


class Customer(db.Model):
    __tablename__ = 'customers'

    customer_index = Column(BigInteger, nullable=False)
    customer_no = Column(Text, primary_key=True)
    mobile = Column(Text)
    identity_type = Column(Text)
    customer_age = Column(BigInteger, nullable=False)
    gender = Column(Text)
    account_no = Column(Text)
    account_age_in_days = Column(Float(53), nullable=False)
    account_age_in_seconds = Column(Float(53), nullable=False)
    regis_year = Column(BigInteger, nullable=False)
    regis_month = Column(Text)
    regis_weekday = Column(Text)
    tot_bal_duration = Column(Float(53), nullable=False)
    max_bal_duration = Column(Float(53), nullable=False)
    min_bal_duration = Column(Float(53), nullable=False)
    avg_bal_duration = Column(Float(53), nullable=False)
    total_weighted_bal = Column(Float(53), nullable=False)
    avg_weighted_bal = Column(Float(53), nullable=False)
    tot_num_deposit = Column(Float(53), nullable=False)
    total_deposit_amt = Column(Float(53), nullable=False)
    max_deposit_amt = Column(Float(53), nullable=False)
    min_deposit_amt = Column(Float(53), nullable=False)
    avg_deposit_amt = Column(Float(53), nullable=False)
    tot_num_withdrawal = Column(Float(53), nullable=False)
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
    time_since_last_deposit = Column(Float(53), nullable=False)
    time_since_last_withdrawal = Column(Float(53), nullable=False)
    balance = Column(Float(53), nullable=False)
    weighted_bal = Column(Float(53), nullable=False)
    customer_type = Column(Text)


class Transaction(db.Model):
    __tablename__ = 'transactions'

    transaction_index = Column(BigInteger, primary_key=True)
    transaction_id = Column(Text)
    transaction_type = Column(Text)
    status = Column(Text)
    payer_name = Column(Text)
    account_no = Column(Text)
    currency = Column(Text)
    amount = Column(Float(53), nullable=False)
    date = Column(DateTime)
    customer_no = Column(ForeignKey('customers.customer_no'), nullable=False)
    mtn_transaction_no = Column(Text)
    fbl_transaction_no = Column(Text)

    customer = relationship('Customer')
