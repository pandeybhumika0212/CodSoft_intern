print("=" * 50)
print("        WELCOME TO RULE-BASED AI CHATBOT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! I am your AI Chatbot.")
print("Type 'help' to see the available commands.")
print("Type 'exit' to close the chatbot.\n")

while True:

    user = input("You: ").strip().lower()

    if user == "hello" or user == "hi":
        print(f"Bot: Hello {name}! How can I help you today?")

    elif user == "how are you":
        print("Bot: I am doing great. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodSoft AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Bhumika for the CodSoft AI Internship.")

    elif user == "what is python":
        print("Bot: Python is a high-level programming language used in AI, Machine Learning, Web Development, Data Science, and Automation.")

    elif user == "what is artificial intelligence":
        print("Bot: Artificial Intelligence (AI) enables computers to learn, reason, solve problems, and make decisions like humans.")

    elif user == "tell me about this project":
        print("Bot: This is a Rule-Based AI Chatbot developed in Python for the CodSoft AI Internship.")

    elif user == "help":
        print("\nYou can ask questions like:")
        print("- Hello")
        print("- How are you")
        print("- What is your name")
        print("- Who created you")
        print("- What is Python")
        print("- What is Artificial Intelligence")
        print("- Tell me about this project")
        print("- Exit\n")

    elif user == "thanks" or user == "thank you":
        print("Bot: You're welcome!")

    elif user == "exit":
        print(f"Bot: Goodbye {name}! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry! I don't understand that. Type 'help' to see available commands.")