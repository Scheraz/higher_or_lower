from game_data import data
from art import logo, vs
import random

def generate_people():
    """Generate two distinct random people from the data."""
    list_A = random.choice(data)
    list_B = random.choice(data)
    while list_A == list_B:  # Ensure list_B is different from list_A
        list_B = random.choice(data)
    return list_A, list_B

def comparison(list_A, list_B, current_score):
    """Compare follower counts and return updated score or end the game."""
    user_input = input("Who has more followers? Type 'A' or 'B' ")
    if user_input == 'A':
        if list_A['follower_count'] > list_B['follower_count']:
            current_score += 1
            print(f"You are right. Current score is {current_score}")
            return current_score, True  # Continue the game
        else:
            print(f"Sorry you lose. Final score is {current_score}")
            return current_score, False  # End the game
    elif user_input == "B":
        if list_B['follower_count'] > list_A['follower_count']:
            current_score += 1
            print(f"You are correct. Your score is {current_score} ")
            return current_score, True  # Continue the game
        else:
            print(f"Sorry you lose! Final score is {current_score}")
            return current_score, False  # End the game

def game():
    """Main game loop."""
    current_score = 0
    list_A, list_B = generate_people() # Initialize list_A and list_B here
    while True:

        print(logo)
        print(f"Compare A: {list_A['name']}, {list_A['description']}")
        print(vs)
        print(f"Compare B: {list_B['name']}, {list_B['description']}")


        current_score, continue_game = comparison(list_A, list_B, current_score)

        if not continue_game:
            break  # Exit the game loop if the player loses

        # Update list_A and list_B for the next round
        list_A = list_B
        list_B, _ = generate_people()  # Generate a new list_B

# Run the game
game()





















