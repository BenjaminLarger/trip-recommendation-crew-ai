import csv, logging, os

logging.basicConfig(level=logging.INFO)
# Path to your CSV file
CSV_FILE_PATH = "/build/utils/worldcities.csv"


def highlight_differences(str1, str2):
    differences = []
    for i, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            differences.append(f"Position {i}: '{char1}' != '{char2}'")
    if len(str1) != len(str2):
        longer_str = str1 if len(str1) > len(str2) else str2
        for i in range(len(str1), len(str2)):
            differences.append(f"Position {i}: '{longer_str[i]}' (extra character)")
    return differences


def get_cities_from_dictionary(city, country):
    """
    Returns city information (name, latitude, longitude) for a given city name.

    Args:
      city (str): Name of the city
      country (str): Name of the country

    """
    logging.info(f"Searching for city: {city}, in country: {country}")
    city_name = city.strip().lower()
    country_name = country.strip().lower()

    with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["city_ascii"].strip().lower() == city_name:
                difference = highlight_differences(
                    row["country"].strip().lower(), country_name
                )
                if difference:
                    logging.info(
                        f"Country name difference: {difference}, for city: {city_name}, in country: {row['country'].strip().lower()}"
                    )
            if (
                row["city_ascii"].strip().lower() == city_name.strip()
                and row["country"].strip().lower() == country_name.strip()
            ):
                return {"latitude": float(row["lat"]), "longitude": float(row["lng"])}


def find_cities_suggestion_from_user_input_key(user_input_key):
    """
    Returns a list of city suggestions based on user input key.

    Args:
      user_input_key (str): User input key

    """
    city_data = {}
    with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (
                row["city_ascii"]
                .strip()
                .lower()
                .startswith(user_input_key.strip().lower())
            ):
                # Append city, longitude and latitude to the list
                city_data[f"{row['city_ascii'].strip()} ({row['country'].strip()})"] = {
                    "latitude": float(row["lat"]),
                    "longitude": float(row["lng"]),
                }
                if len(user_input_key.strip().lower()) > 4:
                  logging.info(
                      f"City found: {row['city_ascii'].strip()}, Country: {row['country'].strip()}, Latitude: {row['lat']}, Longitude: {row['lng']}"
                  )


    # Sort cities alphabetically
    #cities.sort()

    # Sprt city_data alphabetically by city name
    city_data = dict(sorted(city_data.items()))

    # Limit to top 10 suggestions city_data
    city_data = dict(list(city_data.items())[:10])

    return city_data
