from ai4free import ThinkAnyAI

class thinkAnyAIAgent:
    """Agent which uses ThinkAnyAI API to generate chess moves."""
    
    def __init__(self):
        self.thinkanyai = ThinkAnyAI()

    def get_move(self, fen: str) -> str:
        try:
            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"
            response = self.thinkanyai.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from ThinkAnyAI: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"