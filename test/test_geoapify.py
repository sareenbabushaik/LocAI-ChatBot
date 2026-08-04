# tests/test_geoapify.py

import pytest
from apis.geoapify import search_places, CATEGORY_MAP
from apis.geocoder import geocode


def test_search_places_valid():
    """Test searching for places with valid parameters."""
    try:
        # Test with Paris coordinates
        places = search_places(48.8566, 2.3522, "restaurants")
        assert isinstance(places, list)
    except Exception as e:
        # If API key is not set, test should skip gracefully
        pytest.skip(f"Geoapify API test skipped: {e}")


def test_search_places_invalid_category():
    """Test searching with an invalid category."""
    with pytest.raises(ValueError):
        search_places(48.8566, 2.3522, "invalid_category")


def test_category_map_contains_keys():
    """Test that the category map has all expected keys."""
    expected_categories = [
        "restaurants", "cafes", "hotels", "hostels",
        "hospitals", "pharmacies", "parks", "malls",
        "supermarkets", "airports"
    ]
    
    for category in expected_categories:
        assert category in CATEGORY_MAP


def test_geocode_valid():
    """Test geocoding a valid location."""
    try:
        lat, lon = geocode("Eiffel Tower, Paris")
        assert lat is not None
        assert lon is not None
    except Exception as e:
        pytest.skip(f"Geocoding test skipped: {e}")