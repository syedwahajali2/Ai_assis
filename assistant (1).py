from ai_client import AIClient
from conversation import Conversation
from intent_detector import detect_intent
from response_builder import ResponseBuilder
from commands import handle_command

class AIAssistant:
    def __init__(self):
        self.client = AIClient()
        self.conversation = Conversation()
        self.builder = ResponseBuilder()

    def reply(self, message):
        command_result = handle_command(message)
        if command_result is not None:
            return command_result

        intent = detect_intent(message)
        context = self.builder.context_for(intent)
        history = self.conversation.get_messages()
        answer = self.client.ask(message, context, history)

        self.conversation.add("user", message)
        self.conversation.add("assistant", answer)
        return answer
