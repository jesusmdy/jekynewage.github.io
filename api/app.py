from flask import Flask, request, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

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
    # Since we always generate data, the "else" part for 404 might not be hit
    # unless get_mock_flight_data explicitly returns None or an empty list.
    # For this task, it will always generate 1 to 5 flights.
    else: # This case should ideally not be reached if get_mock_flight_data always returns data.
        return jsonify({"message": f"No flights found from {source_city} to {destination_city}"}), 404

def get_mock_flight_data(source_city, destination_city):
    """
    Generates dynamic mock flight data for a given source and destination city.
    """
    flights = []
    num_flights = random.randint(1, 5)

    for _ in range(num_flights):
        airline = fake.company()
        price = random.randint(200, 1200)
        hours = random.randint(1, 12)
        minutes = random.randint(0, 59)
        duration = f"{hours}h {minutes}m"
        
        flights.append({
            "airline": airline,
            "price": price,
            "duration": duration
        })
    return flights

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
