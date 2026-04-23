import random

def play_game():
    options = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit'): ").lower()
        if user_choice == 'quit': break
        if user_choice not in options:
            print("Invalid choice.")
            continue
        computer_choice = random.choice(options)
        print(f"You: {user_choice}, Computer: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("Tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()
