from app import ma
from marshmallow import fields, pprint

from historic_model import Historical
from models import Customer, Transaction


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer

class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction



# class Customer360Schema(ma.Schema):
#     transactions = fields.Nested('MiniTransactionSchema', many=True)
#     class Meta:
#         fields = ('customer_no', "customer_type")


# class MiniTransactionSchema(ma.Schema):
#     class Meta:
#         model = Transaction



c_schema = CustomerSchema()
t_schema = TransactionSchema()

