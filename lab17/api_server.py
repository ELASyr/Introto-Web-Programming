# Lab 17 - Example 2
# Exposing an API using Flask (Simple Weather API)

from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "New York": {"temperature": 20, "condition": "Sunny"},
    "London": {"temperature": 15, "condition": "Cloudy"},
    "Tokyo": {"temperature": 10, "condition": "Rainy"},
}

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404

@app.route("/", methods=["GET"])
def home():
    return "Lab 17 API Server is running. Try /weather?city=London"

if __name__ == "__main__":
    app.run(debug=True)
