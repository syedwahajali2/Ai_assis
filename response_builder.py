from ai_knowledge import AI_GUIDE
from cars_knowledge import CARS_GUIDE
from user_profile import profile_summary

GENERAL_GUIDE = """
You are a friendly, accurate assistant. Answer the user's actual question.
Use simple English unless the user writes in another language. Keep answers
clear and organized. If unsure, say so instead of making up facts.
"""

class ResponseBuilder:
    def context_for(self, intent):
        if intent == "cars":
            return GENERAL_GUIDE + "\n" + CARS_GUIDE
        if intent == "ai":
            return GENERAL_GUIDE + "\n" + AI_GUIDE
        if intent == "profile":
            return GENERAL_GUIDE + "\nUser profile:\n" + profile_summary()
        return GENERAL_GUIDE + "\n" + AI_GUIDE + "\n" + CARS_GUIDE
