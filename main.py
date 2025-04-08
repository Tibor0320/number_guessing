# Importing the random module to generate a random number
import random

# Constants for the number of turns based on difficulty level
EASY_TURNS = 10
HARD_TURNS = 5

# Variable to store the number of turns (initialized to 0)
turns = 0

def check_answer(user_guess, actual_answer, turns):
    """
    Checks the user's guess against the actual answer.
    Returns the number of turns remaining after each guess.
    """
    if user_guess < actual_answer:
        print("Too low")  # Inform the user their guess is too low
        return turns - 1  # Decrease the number of turns
    elif user_guess > actual_answer:
        print("Too high")  # Inform the user their guess is too high
        return turns - 1  # Decrease the number of turns
    else:
        print(f'Correct! The answer was {actual_answer}.')  # User guessed correctly

def set_dif():
    """
    Sets the difficulty level of the game.
    Returns the number of turns based on the chosen difficulty.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS  # Easy difficulty gives more turns
    else:
        return HARD_TURNS  # Hard difficulty gives fewer turns

def game():
    """
    Main function to run the number guessing game.
    Handles the game flow, including setting up the game,
    taking user input, and checking guesses.
    """
    print("Welcome to the number guessing game!")
    print("I have chosen a number between 1 and 100.")

    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)

    # Set the number of turns based on the chosen difficulty
    turns = set_dif()

    # Initialize the user's guess
    guess = 0
    while guess != answer:
        # Inform the user of the remaining attempts
        print(f'You have {turns} attempts remaining to guess the number.')

        # Take the user's guess as input
        guess = int(input("Take a guess: "))

        # Check the user's guess and update the number of turns
        turns = check_answer(guess, answer, turns)

        # If the user runs out of turns, end the game
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        # If the guess is incorrect, prompt the user to guess again
        elif guess != answer:
            print("Guess again.")

# Start the game
game()