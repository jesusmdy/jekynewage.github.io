# Flight Comparison API

## Overview
This API provides a simple way to compare mock flight data between two cities. It's a Flask-based application designed to return flight options including airline, price, and duration.

## Setup and Installation
It is assumed that you have Python 3 installed on your system.

1.  **Clone the repository (if applicable) or ensure you have the `api` directory.**
2.  **Navigate to the `api` directory:**
    ```bash
    cd path/to/your/project/api
    ```
3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the API
Once the setup is complete, you can run the Flask development server:

1.  **Ensure you are in the `api` directory where `app.py` is located.**
2.  **Run the application:**
    ```bash
    python app.py
    ```
    Alternatively, you can use the `flask` command (this might require setting `FLASK_APP=app.py` environment variable first):
    ```bash
    flask run
    ```
3.  The API will be accessible at `http://127.0.0.1:5000` by default.

## API Endpoint

### `/compare_flights`
*   **Method:** `GET`
*   **Description:** Retrieves mock flight information based on source and destination cities.
*   **Parameters:**
    *   `source_city` (string, **required**): The city of departure.
    *   `destination_city` (string, **required**): The city of arrival.
*   **Example Usage:**
    ```
    http://127.0.0.1:5000/compare_flights?source_city=NYC&destination_city=LON
    ```
*   **Success Response (200 OK):**
    Returns a JSON object containing a list of flights.
    ```json
    {
      "flights": [
        {
          "airline": "Airline A",
          "price": 500,
          "duration": "7h"
        },
        {
          "airline": "Airline B",
          "price": 550,
          "duration": "7h 30m"
        }
      ]
    }
    ```
*   **Error Responses:**
    *   **400 Bad Request:** Returned if `source_city` or `destination_city` parameters are missing.
        ```json
        {
          "error": "Missing source_city or destination_city parameter"
        }
        ```
    *   **404 Not Found:** Returned if no flights are found for the given city pair.
        ```json
        {
          "message": "No flights found from [source_city] to [destination_city]"
        }
        ```
