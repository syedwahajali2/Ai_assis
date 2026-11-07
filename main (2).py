from assistant import AIAssistant

def main():
    assistant = AIAssistant()
    print("\nWahaj AI Assistant")
    print("Ask about AI, Python, your learning profile, or cars.")
    print("Type 'help' for commands and 'exit' to close.\n")

    while True:
        try:
            message = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAssistant: Goodbye!")
            break

        if not message:
            continue
        if message.lower() in {"exit", "quit", "bye"}:
            print("Assistant: Goodbye!")
            break

        print(f"Assistant: {assistant.reply(message)}\n")

if __name__ == "__main__":
    main()
