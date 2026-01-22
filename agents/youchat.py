from ai4free import YouChat
from utils.prompts import get_move_prompt

class YouChatAgent:
    """Agent which uses YouChat API to generate chess moves."""
    
    
    def __init__(self):
        self.youchat = YouChat()
        self.name = "YouChat Agent"

    def get_move(self, fen: str, color: str) -> str:
        try:
            prompt = get_move_prompt(fen, color)
            
            response = self.youchat.chat(prompt)
            return response
        except Exception as e:
            return f"ERROR from YouChat: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"