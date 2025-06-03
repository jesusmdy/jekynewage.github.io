from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/compare_flights')
def compare_flights():
    source_city = request.args.get('source_city')
    destination_city = request.args.get('destination_city')

    if not source_city or not destination_city:
        return jsonify({"error": "Missing source_city or destination_city parameter"}), 400

    flight_data = get_mock_flight_data(source_city, destination_city)
    if flight_data:
        return jsonify({"flights": flight_data}), 200
    else:
        return jsonify({"message": f"No flights found from {source_city} to {destination_city}"}), 404

MOCK_FLIGHT_DATA = {
    "NYC-LON": [
        {"airline": "Airline A", "price": 500, "duration": "7h"},
        {"airline": "Airline B", "price": 550, "duration": "7h 30m"}
    ],
    "LAX-TOK": [
        {"airline": "Airline C", "price": 800, "duration": "11h"},
        {"airline": "Airline D", "price": 820, "duration": "11h 15m"}
    ],
    "CHI-PAR": [
        {"airline": "Airline E", "price": 600, "duration": "8h"},
    ]
}

def get_mock_flight_data(source_city, destination_city):
    """
    Retrieves mock flight data for a given source and destination city.
    """
    key = f"{source_city}-{destination_city}"
    return MOCK_FLIGHT_DATA.get(key)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
