# services/llm.py

import ollama
import json
import re
from typing import Optional, Dict, Any

MODEL_NAME = "phi3:mini"

def generate_response(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Generate a response using Ollama.
    
    Parameters:
        prompt (str): The formatted prompt to send to the LLM
        model (str): The Ollama model to use
        
    Returns:
        str: The generated response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        
        return response["message"]["content"].strip()
    
    except Exception as e:
        error_msg = f"Error generating response: {str(e)}"
        print(error_msg)
        return "I'm sorry, I encountered an error processing your request. Please try again."


def extract_json_from_response(response: str) -> Optional[Dict[str, Any]]:
    """
    Extract JSON from LLM response.
    
    Parameters:
        response (str): The raw response from LLM
        
    Returns:
        Optional[Dict[str, Any]]: Parsed JSON or None if not found
    """
    try:
        # Try to find JSON in the response using regex
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)
        
        return None
    
    except json.JSONDecodeError:
        return None