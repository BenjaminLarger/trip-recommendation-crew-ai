import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from trip_agents import TripAgents
from tip_tasks import TripTasks
from crewai import Crew
from dictionary import (
    get_cities_from_dictionary,
    find_cities_suggestion_from_user_input_key,
)

# from gemini import get_cities

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
    logging.info(f"Received data: {data}")
    if not query:
        return jsonify({"status": "failure"}), 400

    agents = TripAgents()
    tasks = TripTasks()

    # trip_tasks = TripTasks()
    logging.info(
        f"Received query: {query['travelType']}, {query['travelBudget']}, {query['travelTime']}, {query['travelRegion']}, {query['travelActivity']}"
    )
    identify_task = tasks.identify_task(
        agents.city_selection_agent(),
        "origin",
        query["travelType"],
        query["travelBudget"],
        query["travelTime"],
        query["travelRegion"],
        query["travelActivity"],
    )

    crew = Crew(
        agents=[agents.city_selection_agent()],
        tasks=[identify_task],
        verbose=True,
    )
    # identify_task = tasks.identify_task(
    #    city_selector_agent,
    #    self.origin,
    #    self.cities,
    #    self.interests,
    #    self.date_range
    # )
    # logging.info(f"Cities Info JSON: {cities_info_json}")
    result = crew.kickoff()
    logging.info(f"Kickoff Result: {result}")
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
