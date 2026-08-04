def detect_intent(message: str) -> str:
    """
    Ultra-fast intent detection using keywords (perfect for 8GB RAM)
    """
    msg = message.lower()

    # WEATHER
    if any(word in msg for word in ["weather", "temperature", "rain", "humidity", "wind", "forecast", "hot", "cold"]):
        return "weather"

    # PLACE INFORMATION (Wikipedia)
    if any(word in msg for word in ["tell me about", "history of", "information", "facts about", "hometown", "who is", "what is", "about"]):
        return "place_information"

    # RESTAURANTS
    if any(word in msg for word in ["restaurant", "eat", "food", "dinner", "lunch", "breakfast", "hungry", "meal"]):
        return "restaurants"

    # CAFES
    if any(word in msg for word in ["cafe", "coffee", "tea", "latte", "cappuccino"]):
        return "cafes"

    # HOTELS
    if any(word in msg for word in ["hotel", "stay", "accommodation", "room", "lodging", "motel", "inn"]):
        return "hotels"

    # HOSPITALS
    if any(word in msg for word in ["hospital", "doctor", "medical", "clinic", "emergency", "health"]):
        return "hospitals"

    # PARKS
    if any(word in msg for word in ["park", "garden", "nature", "walk", "trail"]):
        return "parks"

    # MALLS
    if any(word in msg for word in ["mall", "shop", "shopping", "store", "market"]):
        return "malls"

    # AIRPORTS
    if any(word in msg for word in ["airport", "flight", "fly", "plane", "terminal", "travel"]):
        return "airports"

    # Default to general
    return "general"