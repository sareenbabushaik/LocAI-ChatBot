import re

def extract_locations(message: str) -> str:
    """
    Extract location names from user message using smart keywords.
    """
    msg = message.lower()
    
    # List of common known cities (you can add more here)
    known_cities = [
        "trichy", "chennai", "mumbai", "delhi", "bangalore", "hyderabad", 
        "kolkata", "pune", "ahmedabad", "jaipur", "lucknow", "kanpur", 
        "nagpur", "indore", "bhopal", "visakhapatnam", "patna", "vadodara",
        "london", "paris", "new york", "tokyo", "dubai", "singapore", 
        "khammam", "hyderabad"
    ]
    
    # Check if any known city is in the message
    for city in known_cities:
        if city in msg:
            return city.title() # Return with proper capitalization (e.g., "Trichy")
            
    # If no known city is found, try to extract the last word 
    # (e.g., "Tell me about Mumbai" -> "Mumbai")
    words = message.split()
    if len(words) > 0:
        # Check if the last word might be a location
        potential_location = words[-1].strip('.,!?')
        if len(potential_location) > 2: # Must be at least 3 letters
            return potential_location
            
    return "unknown"