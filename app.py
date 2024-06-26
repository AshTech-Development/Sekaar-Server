from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyrodiil_data.db'
db = SQLAlchemy(app)

class CyrodiilData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/receive-map-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if data:
        new_data = CyrodiilData(data=str(data))  # Ensure data is stored as a string
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Data received'}), 200
    return jsonify({'status': 'error', 'message': 'No data received'}), 400

@app.route('/api/get-map-data', methods=['GET'])
def get_map_data():
    results = CyrodiilData.query.order_by(CyrodiilData.timestamp.desc()).all()
    return jsonify([{
        'timestamp': entry.timestamp,
        'data': entry.data
    } for entry in results])

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
