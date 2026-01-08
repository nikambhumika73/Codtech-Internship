print("Chatbot: Hello! I am an AI chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Chatbot: I am fine, thank you! What about you?")

    elif "your name" in user_input:
        print("Chatbot: My name is CodTech AI Chatbot.")

    elif "help" in user_input:
        print("Chatbot: I can answer simple questions like greetings and my name.")

    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a great day 😊")
        break

    else:
        print("Chatbot: Sorry, I didn't understand that.")