# Choosing number
import random

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(user_guess, actual_answer):
    if user_guess < actual_answer:
        return "Too low!"
    elif user_guess > actual_answer:
        return "Too high!"
    else:
        return "Correct!"

def set_dif():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


print("Welcome to the number guessing game!")
print("I have chosen a number between 1 and 100.")

answer = random.randint(1, 100)


turns = set_dif()
print(f'You have {turns} attempts remaining to guess the number.')


guess = int(input("Take a guess: "))

check_answer(guess, answer)

