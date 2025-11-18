from xml.parsers.expat import model
from ai4free import PhindSearch

class PhindAgent:
    """Agent which uses Google Phind API to generate chess moves."""

    def __init__(self):
        self.phind = PhindSearch()
       
    def get_move(self, fen: str) -> str:
        try:
            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"
            response = self.phind.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from Phind: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"

