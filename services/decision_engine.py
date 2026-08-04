# services/decision_engine.py

from services.location_extractor import extract_locations
from services.intent_detector import detect_intent
from services.context_builder import build_context
from services.llm import generate_response

from apis.geocoder import geocode
from apis.geoapify import search_places
from apis.weather import get_weather
from apis.wikipedia import get_place_information
import logging

logger = logging.getLogger(__name__)

# Intents that require geocoding
GEOCODING_REQUIRED = [
    "restaurants", "cafes", "hotels", "hostels",
    "hospitals", "pharmacies", "parks", "malls",
    "supermarkets", "airports", "weather"
]


def process(user_message, conversation_history=None):
    """
    Process user message through the decision engine.
    
    Parameters:
        user_message (str): User's message
        conversation_history (list): Previous conversation
        
    Returns:
        str: Generated response
    """
    try:
        logger.info(f"Processing: {user_message[:50]}...")
        
        # 1. Extract location
        location = extract_locations(user_message)
        logger.info(f"Extracted location: {location}")
        
        # 2. Detect intent
        intent = detect_intent(user_message)
        logger.info(f"Detected intent: {intent}")
        
        data = None
        
        # 3. Geocode only when required
        if intent in GEOCODING_REQUIRED:
            if location and location != "unknown":
                try:
                    lat, lon = geocode(location)
                    logger.info(f"Geocoded location: {lat}, {lon}")
                except Exception as e:
                    logger.warning(f"Geocoding failed: {e}")
                    lat, lon = None, None
            else:
                lat, lon = None, None
        else:
            lat, lon = None, None
        
        # 4. Route request
        if intent in GEOCODING_REQUIRED and lat and lon:
            if intent in [
                "restaurants", "cafes", "hotels", "hostels",
                "hospitals", "pharmacies", "parks", "malls",
                "supermarkets", "airports"
            ]:
                data = search_places(
                    lat=lat,
                    lon=lon,
                    category=intent
                )
                logger.info(f"Found {len(data) if data else 0} places")
                
            elif intent == "weather":
                data = get_weather(location) or get_weather_for_coordinates(lat, lon)
                logger.info("Retrieved weather data")
        
        elif intent == "place_information":
            if location and location != "unknown":
                data = get_place_information(location)
                logger.info(f"Retrieved information for {location}")
            else:
                # If location is unknown, skip the API and let the LLM ask for clarification
                data = None
                logger.info("Skipped Wikipedia - no valid location found")
        # 5. Build context
        prompt = build_context(
            user_message=user_message,
            intent=intent,
            locations=location,
            api_data=data,
            history=conversation_history
        )
        
        # 6. Generate final response
        answer = generate_response(prompt)
        
        return answer
    
    except Exception as e:
        logger.error(f"Error in decision engine: {str(e)}", exc_info=True)
        return f"I encountered an error while processing your request: {str(e)}"


def get_weather_for_coordinates(lat, lon):
    """
    Get weather using coordinates.
    
    Parameters:
        lat (float): Latitude
        lon (float): Longitude
        
    Returns:
        dict: Weather data
    """
    from apis.weather import get_weather_for_coordinates as get_weather_coords
    return get_weather_coords(lat, lon)