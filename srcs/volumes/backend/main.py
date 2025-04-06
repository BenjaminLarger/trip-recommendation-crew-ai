import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from crew import LatestAiDevelopmentCrew
from dictionary import (
    find_cities_suggestion_from_user_input_key,
)

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


@app.route("/")
def home():
    return "Travel Recommender Backend is running!"


@app.route("/api/suggestions", methods=["POST"])
def get_suggestions():
    # Get user input from the request
    # data = request.get_json()
    data = {
        "query": {
            "travelType": "relaxation",
            "travelBudget": "luxury",
            "travelTime": "november",
            "travelRegion": "africa",
            "travelActivity": ["adventure", "sightseeing"],
            "departureCity": "Madrid (Spain)",
        }
    }
    query = data.get("query", "")
    LatestAiDevelopmentCrew().crew().kickoff(inputs=query)
    logging.info(f"Received data: {data}")
    if not query:
        return jsonify({"status": "failure"}), 400

    return jsonify(
        {"status": "success", "message": "Suggestions generated successfully"}
    )


@app.route("/api/input", methods=["POST"])
def update_input():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    logging.info(f"Received data: {data}")
    cities_suggestions = find_cities_suggestion_from_user_input_key(query)
    logging.info(f"Cities suggestions: {cities_suggestions}")
    return jsonify({"status": "success", "cities_suggestions": cities_suggestions})


if __name__ == "__main__":
    app.run(debug=True)
