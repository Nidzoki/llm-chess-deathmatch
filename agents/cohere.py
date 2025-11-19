import cohere

class CohereAgent:

    """Agent which uses Cohere API to generate chess moves."""
    def __init__(self, api_key):
        self.API_key = api_key
        self.cohere = cohere.Client(api_key=api_key)

    def get_move(self, fen: str) -> str:
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

                    Now output the move:
"""
            response = self.cohere.chat(model="command-a-03-2025", message=prompt, max_tokens=10).text
            return response
        except Exception as e:
            return f"ERROR from Cohere: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"

