from chatbot import Chatbot
from solving import calculate_numerical_solutions, generate_response

def main():
    print("Chatbot: Hello! How can I assist you today?")
    chatbot = Chatbot('intents.json')

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        if chatbot.recognize_intent(chatbot.process_input(user_input)) == 'calculate_numerical_solutions':
            results = calculate_numerical_solutions(user_input)

            if "error" in results:
                print("Chatbot: " + results["error"])
            else:
                response = generate_response(results)
                print("Chatbot:", response)
        else:
            response = chatbot.handle_intent(user_input)
            print("SciBot:", response)

if __name__ == "__main__":
    main()
