from flask import Flask, render_template, request, flash, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:livanshu123@localhost/flaskapi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class demotable(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(80), unique=True, nullable=False)
    mac_address = db.Column(db.String(120))
    scan_timestamp = db.Column(db.String(120))
    rssi = db.Column(db.String(120))
    broadcast_data = db.Column(db.String(120))
    broadcast_name = db.Column(db.String(120))


    def __init__(self, index, source_id, mac_address,scan_timestamp,rssi,broadcast_data,broadcast_name):
        self.index = index
        self.source_id = source_id
        self.mac_address = mac_address
        self.scan_timestamp = scan_timestamp
        self.rssi = rssi
        self.broadcast_data = broadcast_data
        self.broadcast_name = broadcast_name

@app.route('/test',methods=['GET'])
def test():
    return {
        'test':'test1'
    }

@app.route('/demo1',methods=['GET'])
def getdemo():
    alldemo = demotable.query.all()
    output = []
    for demo in alldemo:
        currdemo = {}
        currdemo['index']= demotable.index
        currdemo['source_id'] = demotable.source_id
        currdemo['mac_address'] = demotable.mac_address
        currdemo['scan_timestamp'] = demotable.scan_timestamp
        currdemo['rssi'] = demotable.rssi
        currdemo['broadcast_data'] = demotable.broadcast_data
        currdemo['broadcast_name'] = demotable.broadcast_name
        output.append(currdemo)
    return jsonify(output)

@app.route('/demo1',methods=['POST'])
def postdemo():
    demodata = request.get_json()
    test = demotable(index=demodata['index'],source_id=demodata['source_id'],mac_address=demodata['mac_address'],scan_timestamp=demodata["scan_timestamp"],rssi=demodata["rssi"],broadcast_data=demodata["broadcast_data"],broadcast_name=demodata['broadcast_name'])
    db.session.add(test)
    db.session.commit()
    return jsonify(demodata)



#if __name__ == '__main__':
#    db.create_all()
#    app.run()