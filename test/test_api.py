# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_chat_endpoint():
    """Test the chat endpoint with a valid request."""
    response = client.post(
        "/chat",
        json={"message": "What is the weather in Paris?"}
    )
    
    assert response.status_code == 200
    assert "answer" in response.json()


def test_chat_endpoint_empty_message():
    """Test the chat endpoint with an empty message."""
    response = client.post(
        "/chat",
        json={"message": ""}
    )
    
    # Should handle empty message gracefully
    assert response.status_code == 200


def test_chat_endpoint_long_message():
    """Test the chat endpoint with a long message."""
    long_message = "Tell me about " + "restaurants " * 50
    response = client.post(
        "/chat",
        json={"message": long_message}
    )
    
    assert response.status_code == 200
