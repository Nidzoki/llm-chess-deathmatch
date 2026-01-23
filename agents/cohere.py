import cohere
from utils.prompts import get_move_prompt

class CohereAgent:

    """Agent which uses Cohere API to generate chess moves."""
    def __init__(self, api_key):
        self.API_key = api_key
        self.cohere = cohere.Client(api_key=api_key)

    def get_move(self, fen: str, color:str) -> str:
        try:
            prompt = get_move_prompt(fen, color)
            response = self.cohere.chat(model="command-a-03-2025", message=prompt, max_tokens=10).text
            return response
        except Exception as e:
            return f"ERROR from Cohere: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"
