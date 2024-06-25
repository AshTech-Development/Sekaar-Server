# eso_addon_data.py
from flask import request, jsonify

eso_addon_data = {}

def receive_eso_addon_data():
    data = request.get_json()
    if data:
        eso_addon_data.update(data)
        return jsonify({'message': 'Data received successfully'}), 200
    else:
        return jsonify({'error': 'No data received'}), 400

def get_eso_addon_data():
    return eso_addon_data
