# apis/weather.py

import requests
from apis.geocoder import geocode


def get_weather(location: str) -> dict:
    """
    Get weather information for a location.
    
    Parameters:
        location (str): Location name
        
    Returns:
        dict: Weather data
    """
    try:
        # Geocode the location
        lat, lon = geocode(location)
        
        if lat is None or lon is None:
            return {"error": f"Could not geocode location: {location}"}
        
        # Get weather data from Open-Meteo
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m"
            f"&forecast_days=1"
        )
        
        response = requests.get(weather_url)
        response.raise_for_status()
        
        data = response.json()
        
        # Add location info to the response
        data["location"] = location
        
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return {"error": f"Weather API error: {str(e)}"}
    
    except Exception as e:
        print(f"Unexpected error in weather: {e}")
        return {"error": f"Unexpected error: {str(e)}"}


def get_weather_for_coordinates(lat: float, lon: float) -> dict:
    """
    Get weather information for coordinates.
    
    Parameters:
        lat (float): Latitude
        lon (float): Longitude
        
    Returns:
        dict: Weather data
    """
    try:
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m"
            f"&forecast_days=1"
        )
        
        response = requests.get(weather_url)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return {"error": f"Weather API error: {str(e)}"}