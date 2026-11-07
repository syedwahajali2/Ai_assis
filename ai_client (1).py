from openai import OpenAI
from config import API_KEY, MODEL, MAX_OUTPUT_TOKENS
from validator import clean_text

class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY) if API_KEY else None

    def ask(self, question, context, history):
        if not self.client:
            return (
                "The AI connection is not configured yet. Add your API key to the "
                "OPENAI_API_KEY environment variable, then restart the program. "
                "You can still use the built-in 'help' and 'profile' commands."
            )

        messages = [{"role": "system", "content": context}]
        messages.extend(history[-10:])
        messages.append({"role": "user", "content": clean_text(question)})

        try:
            response = self.client.responses.create(
                model=MODEL,
                input=messages,
                max_output_tokens=MAX_OUTPUT_TOKENS
            )
            return response.output_text.strip() or "I could not create a response."
        except Exception as error:
            return f"I couldn't reach the AI service. Check your connection and API settings. Details: {error}"
