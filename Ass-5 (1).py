responses = {
    "greeting": "Hello! How can I help you today?",
    "pricing": "Our pricing starts at ₹500.",
    "hours": "We are open from 9 AM to 6 PM, Monday to Saturday.",
    "services": "We offer web development, app development, and support services.",
    "goodbye": "Goodbye! Have a great day!"
}

def get_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in user_input for word in ["price", "cost", "charges"]):
        return "pricing"
    elif any(word in user_input for word in ["time", "hours", "open"]):
        return "hours"
    elif any(word in user_input for word in ["service", "offer"]):
        return "services"
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "goodbye"
    else:
        return "fallback"

def chatbot():
    print("Chatbot: Hi! Ask me anything (type 'bye' to exit).")

    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)

        if intent == "fallback":
            print("Chatbot: Sorry, I didn’t understand that.")
        else:
            print("Chatbot:", responses[intent])

        if intent == "goodbye":
            break

chatbot()
