from llm import TermAgent

def main():
    agent = TermAgent()
    agent.system.display()

    print("Welcome to TermAgent! Type 'exit' to quit.")

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() == "exit":
            print("Exiting TermAgent. Goodbye!")
            break

        if not user_input:
            continue

        try:
            result = agent.run(user_input)
            response = agent.get_response(result)
            print(f"\nTermAgent > {response}\n")
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()