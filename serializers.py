from app import ma

from historic_model import Historical
from models import Customer, Transaction


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer

class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction

class HistoricalSchema(ma.ModelSchema):
    class Meta:
        model = Historical

h_schema = HistoricalSchema()
c_schema = CustomerSchema()
t_schema = TransactionSchema()

