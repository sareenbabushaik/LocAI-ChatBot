# 🌍 LocAI - Location-Aware AI Chatbot

LocAI is a smart, location-aware AI assistant built with **FastAPI**, **Ollama**, and **SQLite**. It can answer questions about weather, find nearby places (restaurants, hotels, parks, etc.), and provide historical or geographical information about cities and landmarks using Wikipedia.

---

## ✨ Features

- 🏙️ **Place Information**: Get summaries and facts about cities and landmarks via Wikipedia.
- 🌦️ **Weather Forecast**: Real-time weather data (temperature, humidity, wind speed) using Open-Meteo.
- 🍽️ **Nearby Search**: Find restaurants, cafes, hotels, hospitals, parks, malls, and airports using Geoapify.
- 🧠 **AI-Powered Responses**: Uses `phi3:mini` (Ollama) to generate natural, human-like conversations.
- 💾 **Conversation Memory**: Stores chat history in a local SQLite database.
- 🖥️ **Clean Web UI**: Simple dark-mode chat interface with a dedicated history panel.

---

## 📂 Project Structure
LocAI v1/
├── apis/ # External API integrations (Geoapify, Wikipedia, Weather)
├── database/ # SQLite database connection and operations
├── models/ # Pydantic schemas for request/response validation
├── routes/ # FastAPI route definitions (/chat, /history)
├── services/ # Core business logic (Intent detection, LLM, Context building)
├── test/ # Unit tests for APIs and services
├── utils/ # Helper functions and system prompts
├── app.py # FastAPI application entry point
├── config.py # Configuration settings and API keys
├── requirements.txt # Python dependencies
├── index.html # Simple web-based chat UI
└── chatbot.db # SQLite database file

text

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/LocAI-v1.git
   cd LocAI-v1
Create a virtual environment and install dependencies:

bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
Pull the Ollama model (Optimized for 8GB RAM):

bash
ollama pull phi3:mini
Run the FastAPI backend:

bash
uvicorn app:app --reload --port 8000
Open the Chat UI:
Simply open the index.html file in your web browser.

📸 Screenshots
(You can drag and drop a screenshot of your UI here!)

🛠️ Built With
FastAPI - Backend framework

Ollama - Local LLM hosting

SQLite - Embedded database

Geoapify - Geocoding and Places API

Open-Meteo - Weather API

Wikipedia API - Place information

📝 License
This project is for educational and personal use.
