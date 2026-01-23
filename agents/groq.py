from ai4free import GROQ
from utils.prompts import get_move_prompt

class GroqAgent:

    """Agent which uses Groq API to generate chess moves."""
    def __init__(self, api_key=None):
        self.groq = GROQ(api_key=api_key, model="openai/gpt-oss-20b")
        
    def get_move(self, fen: str, color: str) -> str:
        try:
            prompt = get_move_prompt(fen, color)
            response = self.groq.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from Groq: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"
