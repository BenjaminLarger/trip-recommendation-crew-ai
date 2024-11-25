def get_cities(user_input):
    # Print API key for debugging
    logging.info(f"API key: {GEMENI_API_KEY}")
    try:
        # Prepare the API request
        prompt = f"Generate a list of cities based on the following input, separated by a line break:\n{user_input}"
        response = model.generate_content(prompt)

        # Split the response into an array of cities
        cities = response.split("\n")

        # Check if the request was successful
        if response:
            return cities  # Process and return the interrogator's response
        else:
            logging.error("Interrogator API error: No response")
            return []  # Return an empty list if the request fails

    except Exception as e:
        logging.error(f"Error calling Interrogator API: {e}")
        return {"error": str(e)}