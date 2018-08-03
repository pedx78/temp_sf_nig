from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pry:pass@localhost/sfl_fid_nig_demo'

ma = Marshmallow()
ma.init_app(app)

db = SQLAlchemy()
db.init_app(app)


from historic_model import Historical
from serializers import h_schema

@app.route('/get/<id>', methods=['GET'])
def get_customer(id):  
    # h = Historical.query.all()
    h = Historical.query.filter_by(cust_id=id).first()
    result = h_schema.dump(h)
    # print("hist- {}".format(h))
    return jsonify(result)
    # return 'Hi'






# @app.route('/load', methods=['PUT'])
# def load():
#     df = pd.read_json(request.json)
#     # print len(df)
#     return jsonify({'numrecs': len(df)})




