def detect_intent(message):
    text = message.lower()

    car_words = {"car", "cars", "bmw", "mercedes", "toyota", "honda",
                 "suzuki", "audi", "engine", "horsepower", "electric vehicle"}
    ai_words = {"ai", "artificial intelligence", "machine learning",
                "deep learning", "neural network", "llm", "chatbot", "python"}

    if any(word in text for word in car_words):
        return "cars"
    if any(word in text for word in ai_words):
        return "ai"
    if any(word in text for word in {"about me", "my profile", "what do you know"}):
        return "profile"
    return "general"
