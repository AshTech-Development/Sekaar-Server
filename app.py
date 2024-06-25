from flask import Flask, jsonify
from eso_addon_data import receive_eso_addon_data, get_eso_addon_data

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


# Alliance IDs and names
ALLIANCES = {
    1: 'Ebonheart Pact',
    2: 'Aldmeri Dominion',
    3: 'Daggerfall Covenant'
}

# Campaign IDs and names
CAMPAIGNS = {
    95: "CP Imerial City",
    96: "Non-CP Imerial City",
    101: "Blackreach",
    102: "Gray Host",
    103: "Ravenwatch",
    104: "Icereach"
}

# Dictionary to store the data received from the addon
CYRODIIL_DATA = {}

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/receive-map-data', methods=['POST'])
def receive_map_data():
    data = request.get_json()
    if data:
        # Process the received data
        print("Received data:", data)
        # Additional processing or rendering logic goes here
        return jsonify({"success": True})
    else:
        return jsonify({"error": "No data received"}), 400

@app.route('/')
def get_eso_map_data():
    eso_data = get_eso_addon_data()
    return jsonify(eso_data)

if __name__ == '__main__':
    app.run()
