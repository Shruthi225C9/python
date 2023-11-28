import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    computer_choice = get_computer_choice()
    
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

