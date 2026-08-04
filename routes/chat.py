# routes/chat.py

from fastapi import APIRouter, HTTPException
from models import ChatRequest, ChatResponse 
from services import process
from services import get_history, add_user_message, add_assistant_message, clear_history
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        if not request.message or not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        history = get_history()
        logger.info(f"Processing: {request.message[:50]}...")
        
        answer = process(
            user_message=request.message,
            conversation_history=history
        )
        
        add_user_message(request.message)
        add_assistant_message(answer)
        
        return ChatResponse(answer=answer)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/chat/history")
def get_chat_history():
    try:
        history = get_history()
        return {"status": "success", "history": history, "count": len(history)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/chat/history")
def delete_chat_history():
    try:
        clear_history()
        return {"status": "success", "message": "History cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))