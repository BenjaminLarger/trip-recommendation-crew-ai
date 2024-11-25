import logging
import requests
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dictionary import get_cities_from_dictionary
from gemini import get_cities
import google.generativeai as genai
import os

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
CORS(app)


# Get GEMENI_API_KEY from the environment
GEMENI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key="GEMENI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

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

    # Call the Interrogator API
    cities = get_cities(query)
    #cities = ['Sevilla']

    # For each city, select only the ones present in the dictionary. City info contain{'name', 'latitude', 'longitude'}

    cities_info_json = {}
    for city in cities:
      city_info = get_cities_from_dictionary(city)
      if city_info:
        cities_info_json[city] = {
          'latitude': city_info['latitude'],
          'longitude': city_info['longitude']
        }

    return jsonify(cities_info_json)
    
if __name__ == '__main__':
    app.run(debug=True)
