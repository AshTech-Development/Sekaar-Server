# eso_addon_data.py
from flask import request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

eso_addon_data = {}

def receive_eso_addon_data():
    data = request.get_json()
    if data:
        eso_addon_data.update(data)
        logger.debug("Received data: %s", data)  # Log the received data
        return jsonify({'message': 'Data received successfully'}), 200
    else:
        logger.debug("No data received")  # Log when no data is received
        return jsonify({'error': 'No data received'}), 400

def get_eso_addon_data():
    logger.debug("Retrieved data: %s", eso_addon_data)  # Log the retrieved data
    return eso_addon_data
