import requests

BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"


def get_place_information(place_name: str) -> dict:

    # Replace spaces with underscores for Wikipedia URL
    
    page = place_name.strip().replace(" ", "_")

    url = f"{BASE_URL}{page}"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    result = {
        "title": data.get("title"),
        "summary": data.get("extract"),
        "url": data.get("content_urls", {})
                  .get("desktop", {})
                  .get("page"),
        "thumbnail": None,
        "latitude": None,
        "longitude": None
    }

    # Optional thumbnail
    if "thumbnail" in data:
        result["thumbnail"] = data["thumbnail"].get("source")

    # Optional coordinates
    if "coordinates" in data:
        result["latitude"] = data["coordinates"].get("lat")
        result["longitude"] = data["coordinates"].get("lon")

    return result