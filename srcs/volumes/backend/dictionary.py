import csv

# Path to your CSV file
CSV_FILE_PATH = '/build/utils/worldcities.csv'

def get_cities_from_dictionary(city_name):
    """
    Returns city information (name, latitude, longitude) for a given city name.

    Args:
        city_name (str): The name of the city to search for.
        
    Returns:
        dict: A dictionary containing 'name', 'latitude', and 'longitude' if the city is found, or None if not found.
    """
    # Normalize the city_name input to handle case sensitivity
    city_name = city_name.lower()

    # Open the CSV file and search for the city
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check if the city matches the input (case-insensitive)
            if row['city_ascii'].lower() == city_name:
                # Return the city information as a dictionary
                return {
                    'name': row['city_ascii'],
                    'latitude': float(row['lat']),
                    'longitude': float(row['lng'])
                }

    # Return None if no matching city is found
    return None