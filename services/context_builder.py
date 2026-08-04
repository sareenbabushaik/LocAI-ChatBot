# services/context_builder.py

from utils.prompts import (
    SYSTEM_PROMPT,
    NEARBY_SEARCH_PROMPT,
    WEATHER_PROMPT,
    PLACE_INFORMATION_PROMPT,
    GENERAL_PROMPT
)


def build_context(user_message: str, intent: str, locations: str, api_data, history: list = None) -> str:
    """
    Build the appropriate prompt based on intent and available data.
    """
    system = SYSTEM_PROMPT.strip()
    
    # Build prompt based on intent
    if intent in ["restaurants", "cafes", "hotels", "hostels", 
                  "hospitals", "pharmacies", "parks", "malls", 
                  "supermarkets", "airports"]:
        
        return NEARBY_SEARCH_PROMPT.format(
            system=system,
            user_message=user_message,
            category=intent,
            location=locations,
            api_data=_format_api_data(api_data)
        )
    
    elif intent == "weather":
        return WEATHER_PROMPT.format(
            system=system,
            user_message=user_message,
            location=locations,
            api_data=_format_api_data(api_data)
        )
    
    elif intent == "place_information":
        return PLACE_INFORMATION_PROMPT.format(
            system=system,
            user_message=user_message,
            location=locations,
            api_data=_format_api_data(api_data)
        )
    
    else:
        history_text = _format_history(history) if history else "No previous conversation."
        return GENERAL_PROMPT.format(
            system=system,
            user_message=user_message,
            history=history_text
        )


def _format_history(history: list) -> str:
    """Format conversation history."""
    if not history:
        return "No previous conversation."
    
    formatted = []
    for msg in history:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        formatted.append(f"{role}: {content}")
    
    return "\n".join(formatted)


def _format_api_data(api_data) -> str:
    """Format API data for the prompt."""
    if api_data is None:
        return "No data available."
    
    if isinstance(api_data, str):
        return api_data
    
    if isinstance(api_data, list):
        if not api_data:
            return "No results found."
        
        formatted = []
        for item in api_data[:5]:  # Limit to 5 items
            if isinstance(item, dict):
                name = item.get("name", "Unknown")
                address = item.get("address", "No address")
                distance = item.get("distance", "N/A")
                formatted.append(f"- {name} ({address}, {distance}m away)")
            else:
                formatted.append(str(item))
        
        return "\n".join(formatted)
    
    if isinstance(api_data, dict):
        # Weather data
        if "current" in api_data:
            current = api_data["current"]
            temp = current.get("temperature_2m", "N/A")
            wind = current.get("wind_speed_10m", "N/A")
            humidity = current.get("relative_humidity_2m", "N/A")
            return f"Temperature: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind} km/h"
        
        # Wikipedia data
        if "summary" in api_data:
            return f"{api_data.get('title', 'Unknown')}: {api_data.get('summary', 'No summary')}"
    
    return str(api_data)