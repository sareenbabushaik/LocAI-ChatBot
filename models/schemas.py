from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime


# ---------- Request ----------

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


# ---------- Response ----------

class ChatResponse(BaseModel):
    answer: str
    intent: Optional[str] = None
    location: Optional[str] = None
    data: Optional[Any] = None
    timestamp: Optional[datetime] = datetime.now()


# ---------- Conversation ----------

class Message(BaseModel):
    role: str
    content: str
    timestamp: Optional[datetime] = datetime.now()


class Conversation(BaseModel):
    history: List[Message] = []


# ---------- Location ----------

class Location(BaseModel):
    name: str
    latitude: float
    longitude: float
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None


# ---------- Place ----------

class Place(BaseModel):
    name: str
    address: Optional[str] = None
    latitude: float
    longitude: float
    distance: Optional[float] = None
    categories: List[str] = []


# ---------- Weather ----------

class Weather(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    condition: str
