# apis/geocoder.py

import requests
from config import GEOAPIFY_API_KEY

def geocode(location: str):
    geocode_url = (
        f"https://api.geoapify.com/v1/geocode/search"
        f"?text={location}"
        f"&apiKey={GEOAPIFY_API_KEY}"
    )

    response = requests.get(geocode_url)

    response.raise_for_status()

    data = response.json()

    if not data.get("features"):
        raise ValueError(f"Location '{location}' not found.")

    properties = data["features"][0]["properties"]

    lat = properties["lat"]
    lon = properties["lon"]

    return lat, lon