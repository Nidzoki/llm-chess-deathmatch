from ai4free import YEPCHAT

class YepAgent:
    """Agent which uses YEPCHAT API to generate chess moves."""
    
    def __init__(self):
        self.yepchat = YEPCHAT()

    def get_move(self, fen: str) -> str:
        try:
            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"
            response = self.yepchat.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from YEPCHAT: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"