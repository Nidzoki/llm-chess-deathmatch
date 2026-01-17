from ai4free import YouChat

class YouChatAgent:
    """Agent which uses YouChat API to generate chess moves."""
    
    
    def __init__(self):
        self.youchat = YouChat()
        self.name = "YouChat Agent"

    def get_move(self, fen: str, color: str) -> str:
        try:
            prompt = f"""You are a chess engine.

                    Given the position in FEN format:
                    {fen}

                    Your task:
                    - Output ONLY ONE legal chess move.
                    - Format MUST be exactly UCI (e.g. "e2e4", "g8f6").
                    - NO words, NO sentences, NO punctuation, NO commentary.
                    - Output MUST contain ONLY 4 characters (or 5 if promotion, e.g. "e7e8q").

                    If you output anything except a single valid UCI move, the response is considered INVALID.

                    You are playing as {color}.

                    Now output the move:
                    """
            
            response = self.youchat.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from YouChat: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"