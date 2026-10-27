"""
Problem Statement: Create an interactive Number guessing game
Input: A random number from the user between the range of integers
Process: 
    1. Store a randomly generated number in a variable.
    2. Input a number from the user.
    3. Compare the two numbers and give out a result of the guess.
Output: Result of the guess as Found, number greater, or smaller.
"""

import random

def guess_me():
    """
    Runs an interactive number guessing game where the user tries 
    to guess a randomly generated number between 1 and 100.
    """
    print("Welcome to the Guessing Game!\n")
    
    # Store a randomly generated number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Initialize attempt counter

    while True:
        try:
            # Get input from the user and convert it to an integer
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            # Compare the user's guess with the secret number
            if guess < secret_number:
                print("Too Low! Try again.\n")
            elif guess > secret_number:
                print("Too High! Try again.\n")
            else:
                print(f"Found it! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            # Handle invalid non-integer inputs
            print("Invalid input! Please enter a valid integer between 1 and 100.\n")


if __name__ == "__main__":
    guess_me()  # Call the guess_me function
