from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import ollama

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str

chat_history = []

def generate_response(prompt: str) -> str:
    try:
        response = ollama.chat(
            model="phi3:mini",
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return "I'm sorry, I encountered an error processing your request. Please try again."

@app.post("/api/v1/chat")
async def chat(request: ChatRequest):
    try:
        response = generate_response(request.message)
        chat_history.append({"role": "user", "content": request.message})
        chat_history.append({"role": "assistant", "content": response})
        return ChatResponse(answer=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/chat/history")
async def get_history():
    return {"history": chat_history}

@app.get("/")
async def home():
    return {
        "status": "running",
        "name": "Loc AI",
        "version": "1.0.0",
        "model": "phi3:mini",
        "message": "Loc AI Backend is running."
    }