from ai4free import BLACKBOXAI

class blackboxAIAgent:
    """Agent which uses BlackboxAI API to generate chess moves."""
    
    def __init__(self):
        self.blackboxai = BLACKBOXAI(
            is_conversation=True,
            max_tokens=800,
            timeout=30,
            intro=None,
            filepath=None,
            update_file=True,
            proxies={},
            history_offset=10250,
            act=None,
            model=None # You can specify a model if needed
        )

    def get_move(self, fen: str) -> str:
        try:
            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"
            response = self.blackboxai.ask(prompt)
            return response
        except Exception as e:
            return f"ERROR from BlackboxAI: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"