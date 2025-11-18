from ai4free import KOBOLDAI

class KoboldAIAgent:
    """Agent which uses KoboldAI API to generate chat responses."""
    
    def __init__(self):
        self.koboldai = KOBOLDAI()

    def get_move(self, fen: str) -> str:
        try:
            prompt = f"""
                    The previous move you suggested was ILLEGAL in this chess position.
                    You MUST output exactly ONE legal move in UCI format.
                    No explanations. Only a single UCI move.
                    FEN: {fen}
                    Move:
                    """

            response = self.koboldai.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from KoboldAI: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"
