print("=" * 50)
print("🤖 Welcome to DecodeLabs Rule-Based AI Chatbot")
print("Type 'bye' anytime to exit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a powerful and easy-to-learn programming language.")

    elif user == "what is chatbot":
        print("Bot: A chatbot is a computer program that talks with users.")

    elif user == "who created you":
        print("Bot: I was created by Minahil as a DecodeLabs internship project.")

    elif user == "help":
        print("Bot: You can ask me:")
        print("- Hi")
        print("- Hello")
        print("- Good Morning")
        print("- Good Evening")
        print("- How are you")
        print("- What is AI")
        print("- What is Python")
        print("- What is Chatbot")
        print("- Who created you")
        print("- Thank you")
        print("- Bye")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    elif user == "my mood is bad":
        print("Bot: I'm sorry to hear that. I hope everything gets better soon. ❤️")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")