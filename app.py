from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pry:pass@localhost/sfl_demo_nigeria'

ma = Marshmallow()
ma.init_app(app)

db = SQLAlchemy()
db.init_app(app)


from models import Customer, Transaction
from serializers import c_schema, t_schema

@app.route('/get/<id>', methods=['GET'])
def get_customer(id):  
    # h = Historical.query.all()
    c = Customer.query.filter_by(customer_index=id).first()
    result = c_schema.dump(c)
    # result = h_schema.dump(h)
    # print("hist- {}".format(h))
    return jsonify(result)


@app.route('/transactions/get/<id>', methods=['GET'])
def get_transaction(id):  
    # h = Historical.query.all()
    c = Transaction.query.filter_by(transaction_index=id).first()
    result = c_schema.dump(c)
    # result = h_schema.dump(h)
    # print("hist- {}".format(h))
    return jsonify(result)



# @app.route('/load', methods=['PUT'])
# def load():
#     df = pd.read_json(request.json)
#     # print len(df)
#     return jsonify({'numrecs': len(df)})




