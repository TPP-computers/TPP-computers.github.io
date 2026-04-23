import random

def play_game():
    options = ["rock", "paper", "scissors", "fire", "human", "sponge", "air", "water", "gun"]
    # Define which choices each option beats
    beats = {
        "rock": ["scissors", "fire", "human", "sponge"],
        "paper": ["rock", "air", "human", "sponge"],
        "scissors": ["paper", "air", "water", "gun"],
        "fire": ["scissors", "paper", "human", "sponge"],
        "human": ["air", "water", "paper", "sponge"],
        "sponge": ["air", "water", "paper", "gun"],
        "air": ["rock", "fire", "water", "gun"],
        "water": ["scissors", "fire", "rock", "gun"],
        "gun": ["scissors", "fire", "human", "rock"]
    }

    while True:
        user_choice = input(f"Enter one of {', '.join(options)} (or 'quit'): ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in options:
            print("Invalid choice.")
            continue

        computer_choice = random.choice(options)
        print(f"You: {user_choice}, Computer: {computer_choice}")

        if user_choice == computer_choice:
            print("Tie!")
        elif computer_choice in beats[user_choice]:
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()
