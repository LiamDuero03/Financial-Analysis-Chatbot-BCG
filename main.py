
print("test")
from chatbot import simple_chatbot
def main():
    print("Welcome to the Financial Analysis Chatbot!")
    print("You can ask about:")
    print("- Total revenue")
    print("- Net income change")
    print("- Total assets")
    print("- Cash flow from operating activities")
    print("- Liabilities change")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYour question: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = simple_chatbot(user_input)
        print(response)

if __name__ == "__main__":
    main()
