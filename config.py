import os
from typing import Optional

# ---------- API Keys ----------
# This is your REAL key from the other files
GEOAPIFY_API_KEY = "Your Real Key"

# ---------- Model Settings ----------
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:8b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# ---------- App Settings ----------
APP_NAME = "GeoBot"
APP_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ---------- Database ----------
DATABASE_NAME = os.getenv("DATABASE_NAME", "chatbot.db")

# ---------- Search Settings ----------
DEFAULT_SEARCH_RADIUS = 5000
MAX_SEARCH_RESULTS = 10