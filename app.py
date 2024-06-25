from flask import Flask, jsonify, request

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

@app.route('/api/receive-map-data', methods=['POST'])
def receive_map_data():
    data = request.get_json()
    campaign_id = data.get('campaignId')
    if campaign_id in CAMPAIGNS:
        campaign_name = CAMPAIGNS[campaign_id]
        CYRODIIL_DATA[campaign_name] = data
        return jsonify({'message': 'Data received successfully'}), 200
    else:
        return jsonify({'error': 'Invalid campaign ID'}), 400

@app.route('/api/get-map-data', methods=['GET'])
def get_map_data():
    return jsonify(CYRODIIL_DATA)

if __name__ == '__main__':
    app.run(debug=True)
