# services/memory.py

from database.database import save_message, get_history as db_get_history, clear_history as db_clear_history

# In-memory cache for faster access
_conversation_cache = []


def get_history(use_cache: bool = True):
    """
    Get conversation history.
    
    Parameters:
        use_cache (bool): Whether to use cached version
        
    Returns:
        list: Conversation history
    """
    if not use_cache:
        # Fetch from database
        return db_get_history()
    
    # Return from cache or fetch from database
    if not _conversation_cache:
        _conversation_cache.extend(db_get_history())
    
    return _conversation_cache.copy()


def add_user_message(message: str):
    """
    Add a user message to history.
    
    Parameters:
        message (str): User message
    """
    # Save to database
    save_message("user", message)
    
    # Update cache
    _conversation_cache.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(message: str):
    """
    Add an assistant message to history.
    
    Parameters:
        message (str): Assistant message
    """
    # Save to database
    save_message("assistant", message)
    
    # Update cache
    _conversation_cache.append({
        "role": "assistant",
        "content": message
    })


def clear_history():
    """
    Clear all conversation history.
    """
    # Clear database
    db_clear_history()
    
    # Clear cache
    _conversation_cache.clear()


def get_last_n_messages(n: int = 10):
    """
    Get the last N messages from history.
    
    Parameters:
        n (int): Number of messages to retrieve
        
    Returns:
        list: Last N messages
    """
    history = get_history()
    return history[-n:] if history else []


def get_conversation_context(max_messages: int = 20):
    """
    Get conversation context for the LLM.
    
    Parameters:
        max_messages (int): Maximum number of messages to include
        
    Returns:
        str: Formatted conversation context
    """
    history = get_last_n_messages(max_messages)
    
    if not history:
        return "No previous conversation."
    
    formatted = []
    for msg in history:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        formatted.append(f"{role}: {content}")
    
    return "\n".join(formatted)