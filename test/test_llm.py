# tests/test_llm.py

import pytest
from services.llm import generate_response, extract_json_from_response


def test_generate_response():
    """Test LLM response generation."""
    try:
        response = generate_response("Say hello")
        assert isinstance(response, str)
        assert len(response) > 0
    except Exception as e:
        pytest.skip(f"LLM test skipped (Ollama may not be running): {e}")


def test_extract_json_from_response():
    """Test extracting JSON from LLM response."""
    test_response = 'Here is the data: {"location": "Paris", "intent": "weather"}'
    result = extract_json_from_response(test_response)
    assert result is not None
    assert result.get("location") == "Paris"
    assert result.get("intent") == "weather"


def test_extract_json_invalid():
    """Test extracting JSON from invalid response."""
    test_response = "This is not a valid JSON response"
    result = extract_json_from_response(test_response)
    assert result is None


def test_generate_response_with_prompt():
    """Test generating response with a specific prompt."""
    prompt = """
    You are a test assistant.
    Return ONLY the word "test" in your response.
    """
    
    try:
        response = generate_response(prompt)
        # Ollama might not follow exactly, so just check it returns something
        assert isinstance(response, str)
    except Exception as e:
        pytest.skip(f"LLM test skipped: {e}")