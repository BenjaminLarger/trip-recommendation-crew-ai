import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dictionary import get_city_info

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)


# Sample data for mock suggestions (replace with real API or AI integration later)
MOCK_SUGGESTIONS = [
    {"name": "Paris", "latitude": 48.8566, "longitude": 2.3522},
    {"name": "New York", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "Tokyo", "latitude": 35.6895, "longitude": 139.6917},
]

@app.route('/')
def home():
    return "Travel Recommender Backend is running!"

@app.route('/api/suggestions', methods=['POST'])
def get_suggestions():
    # Get user input from the request
    data = request.get_json()
    query = data.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Mock response: Filter suggestions by query (case-insensitive search)
    filtered_suggestions = get_city_info(query)
    logging.info(f"Filtered suggestions: {filtered_suggestions} for query: {query}.")
    if filtered_suggestions is None:
        return jsonify({"error": "No matching city found"}), 404

    # Return filtered suggestions (or all if no matches for simplicity)
    return jsonify({"suggestions": filtered_suggestions or MOCK_SUGGESTIONS})

if __name__ == '__main__':
    app.run(debug=True)
