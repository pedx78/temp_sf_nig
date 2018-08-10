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


@app.route('/customer360/get/<id>', methods=['GET'])
def get_customer360(id):  
    c = Customer.query.filter_by(customer_index=id).first()
    # result = c_schema.dump(c)
    transactions = Transaction.query.filter_by(customer_no=c.customer_no)
    print('txns_ {}'.format(transactions[3].payer_name))

    result = {
        "name": c.customer_no,
        "stats": {
            "age": c.customer_age,
            # "dob": "1990-01-01",
            "segment": c.customer_type,
            "Average balance": c.avg_weighted_bal,
            "deposits": c.total_deposit_amt,        
            }
    }

    t_dicts = []
    for t in transactions:
        t_dicts.append({
            "date": t.date,
            "type": t.transaction_type,
            "amount": t.amount
        })

    trans = {
        "transactions": t_dicts
    }

    return jsonify(result, trans)




@app.route('/transactions/get/<id>', methods=['GET'])
def get_transaction(id):  
    c = Transaction.query.filter_by(transaction_index=id).first()
    result = c_schema.dump(c)

    return jsonify(result)


@app.route('/dummy', methods=['GET'])
def get_dummy():  

    name = {'name': 'Holly'} 
    trans = {
        "transactions": [
            {
            "date": "1990-01-02",
            "type": "C",
            "amount": "+100"
            }]
    }
    return jsonify(name, trans)

# @app.route('/load', methods=['PUT'])
# def load():
#     df = pd.read_json(request.json)
#     # print len(df)
#     return jsonify({'numrecs': len(df)})




