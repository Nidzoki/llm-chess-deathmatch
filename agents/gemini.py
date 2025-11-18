import google.generativeai as genai

class GeminiAgent:

    """Agent which uses Google Gemini API to generate chess moves."""
    API_key = ""
    def __init__(self, api_key=""):
        self.API_key = api_key

    def set_api_key(self, api_key):
        self.API_key = api_key
        
    def get_move(self, fen: str) -> str:
        if not self.API_key:
            return "ERROR: GOOGLE_API_KEY not set."
        try:
            genai.configure(api_key=self.API_key)
            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = f"You are a chess engine. Position (FEN): {fen}\nProvide your next move in UCI format:"

            resp = model.generate_content(prompt)
            return resp.text
        except Exception as e:
            return f"ERROR from Gemini: {e}"
        
    def check_is_alive(self):
        return "I'm alive!"

