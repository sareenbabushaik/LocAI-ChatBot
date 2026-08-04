from datetime import datetime

def normalize_text(text: str) -> str:
    """
    Remove leading/trailing spaces and convert to lowercase.
    """
    return text.strip().lower()

def format_distance(distance: float) -> str:
    """
    Convert distance in meters to a readable format.
    """
    if distance < 1000:
        return f"{distance:.0f} m"
    return f"{distance / 1000:.2f} km"

def current_timestamp() -> str:
    """
    Return current timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_location(location: str) -> bool:
    """
    Check if a location string is valid.
    """
    return bool(location and location.strip())

def safe_get(dictionary: dict, *keys, default=None):
    """
    Safely retrieve nested dictionary values.
    """
    value = dictionary
    for key in keys:
        try:
            value = value[key]
        except (KeyError, IndexError, TypeError):
            return default
    return value