from ai4free import LEO

class LeoAgent:
    """Agent which uses LEO API to generate chess moves."""
    
    def __init__(self):
        self.leo = LEO()

    def get_move(self, fen: str) -> str:
        try:
            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"
            response = self.leo.ask(prompt)
            return response
        except Exception as e:
            return f"ERROR from LEO: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"