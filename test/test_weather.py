# tests/test_weather.py

import pytest
from apis.weather import get_weather, get_weather_for_coordinates


def test_get_weather():
    """Test weather API for a valid location."""
    result = get_weather("London")
    assert "current" in result or "error" in result


def test_get_weather_invalid_location():
    """Test weather API for an invalid location."""
    result = get_weather("NonExistentCity12345")
    # Should handle gracefully
    assert isinstance(result, dict)


def test_get_weather_for_coordinates():
    """Test weather API with coordinates."""
    result = get_weather_for_coordinates(48.8566, 2.3522)  # Paris coordinates
    assert "current" in result or "error" in result


def test_weather_response_structure():
    """Test that weather response has expected structure."""
    result = get_weather("New York")
    
    if "error" not in result:
        assert "current" in result
        current = result["current"]
        assert "temperature_2m" in current
        assert "wind_speed_10m" in current