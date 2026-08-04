# apis/geoapify.py
import requests
from config import GEOAPIFY_API_KEY

CATEGORY_MAP = {
    "restaurants": "catering.restaurant",
    "cafes": "catering.cafe",
    "hotels": "accommodation.hotel",
    "hostels": "accommodation.hostel",
    "hospitals": "healthcare.hospital",
    "pharmacies": "healthcare.pharmacy",
    "parks": "leisure.park",
    "malls": "commercial.shopping_mall",
    "supermarkets": "commercial.supermarket",
    "airports": "airport",
}

def search_places(lat: float, lon: float, category: str):
    # ... keep your validation
    url = (
        "https://api.geoapify.com/v2/places"
        f"?categories={CATEGORY_MAP[category]}"
        f"&filter=circle:{lon},{lat},5000"
        f"&bias=proximity:{lon},{lat}"
        f"&limit=10"
        f"&apiKey={GEOAPIFY_API_KEY}"
    )



    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    places = []

    for feature in data.get("features", []):

        properties = feature["properties"]

        places.append({
            "name": properties.get("name"),
            "address": properties.get("formatted"),
            "latitude": properties.get("lat"),
            "longitude": properties.get("lon"),
            "categories": properties.get("categories", []),
            "distance": properties.get("distance")
        })

    return places