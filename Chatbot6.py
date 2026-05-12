# ==========================================
#      CUSTOMER SUPPORT CHATBOT
# ==========================================
# This is a simple rule-based chatbot
# developed for customer interaction.
# ==========================================

# Dictionary containing chatbot responses
responses = {
    "greeting": "Hello! Welcome to TechSolutions Support 😊",
    
    "pricing": (
        "Our pricing starts from ₹500.\n"
        "For detailed pricing, visit: www.techsolutions.com/pricing"
    ),
    
    "hours": (
        "Our working hours are:\n"
        "Monday to Saturday: 9 AM to 6 PM"
    ),
    
    "services": (
        "We provide the following services:\n"
        "1. Web Development\n"
        "2. App Development\n"
        "3. Technical Support\n"
        "4. UI/UX Design"
    ),
    
    "contact": (
        "You can contact us through:\n"
        "📞 Phone: +91 9876543210\n"
        "📧 Email: support@techsolutions.com"
    ),
    
    "location": "We are located in Pune, Maharashtra.",
    
    "thanks": "You're welcome! Happy to help 😊",
    
    "goodbye": "Thank you for chatting with us. Have a great day! 👋"
}


# Function to identify user intent
def get_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "cost", "charges", "fee"]):
        return "pricing"

    elif any(word in user_input for word in ["time", "hours", "open", "working"]):
        return "hours"

    elif any(word in user_input for word in ["service", "offer", "provide"]):
        return "services"

    elif any(word in user_input for word in ["contact", "phone", "email"]):
        return "contact"

    elif any(word in user_input for word in ["location", "address", "where"]):
        return "location"

    elif any(word in user_input for word in ["thank", "thanks"]):
        return "thanks"

    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        return "goodbye"

    else:
        return "fallback"


# Main chatbot function
def chatbot():

    print("=" * 50)
    print("      🤖 CUSTOMER SUPPORT CHATBOT")
    print("=" * 50)

    print("\nChatbot: Hello! I am your virtual assistant.")
    print("Type 'bye' anytime to exit.\n")

    while True:

        user_input = input("You: ").strip()

        # Handling empty input
        if user_input == "":
            print("Chatbot: Please type something so I can help you.")
            continue

        # Detect user intent
        intent = get_intent(user_input)

        # Better fallback response
        if intent == "fallback":
            print("\nChatbot: Sorry, I didn't understand that.")
            print("You can ask about:")
            print("- Services")
            print("- Pricing")
            print("- Working hours")
            print("- Contact information\n")

        else:
            print(f"\nChatbot: {responses[intent]}\n")

        # Exit condition
        if intent == "goodbye":
            break


# Run chatbot
chatbot()