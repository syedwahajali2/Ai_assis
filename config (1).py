import os

API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
MAX_OUTPUT_TOKENS = 700
ASSISTANT_NAME = "Wahaj AI Assistant"
HISTORY_LIMIT = 20
