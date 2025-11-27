# --- Python Rock, Paper, Scissors Game ---
# This is a console application that runs in the terminal.

import random

def play_game():
    """Runs the main Rock, Paper, Scissors game loop."""
    print("\n--- Welcome to Rock, Paper, Scissors! ---")
    
    # List of valid choices
    choices = ['rock', 'paper', 'scissors']
    
    # Game loop to allow multiple rounds
    while True:
        # 1. Get user input
        user_choice = input("Enter your choice (Rock, Paper, Scissors) or 'quit' to end: ").lower().strip()

        # Check for quit command
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")
            continue
            
        # 2. Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"The computer chose: {computer_choice.capitalize()}")

        # 3. Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        
        # Winning conditions for the user
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("🎉 You win this round!")
        
        # If not a tie and not a win, it must be a loss
        else:
            print("🤖 The computer wins this round!")
        
        print("-" * 30) # Separator for next round

# Start the game
if __name__ == "__main__":
    play_game()