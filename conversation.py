from config import HISTORY_LIMIT

class Conversation:
    def __init__(self):
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        self.messages = self.messages[-HISTORY_LIMIT:]

    def get_messages(self):
        return list(self.messages)

    def clear(self):
        self.messages.clear()
