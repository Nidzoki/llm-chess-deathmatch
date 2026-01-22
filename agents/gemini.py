import google.generativeai as genai
from utils.prompts import get_move_prompt

class GeminiAgent:

    """Agent which uses Google Gemini API to generate chess moves."""
    def __init__(self, api_key=None):
        self.API_key = api_key
        
    def get_move(self, fen: str, color:str) -> str:
        if not self.API_key:
            return "ERROR: GOOGLE_API_KEY not set."
        try:
            genai.configure(api_key=self.API_key)
            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = get_move_prompt(fen, color)

            resp = model.generate_content(prompt)
            return resp.text
        except Exception as e:
            return f"ERROR from Gemini: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"

