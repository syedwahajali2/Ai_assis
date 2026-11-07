from conversation import Conversation
from user_profile import profile_summary

def handle_command(message):
    command = message.strip().lower()

    if command == "help":
        return (
            "Commands:\n"
            "- help: show commands\n"
            "- profile: show your saved learning profile\n"
            "- clear: clear this conversation\n"
            "- exit: close the assistant\n\n"
            "You can also ask normal questions about AI, Python, and cars."
        )

    if command == "profile":
        return profile_summary()

    if command == "clear":
        return "To clear the chat, restart the program. (Conversation history is kept only in memory.)"

    return None
