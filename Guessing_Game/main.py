import random
from art import logo


def random_number():
    return random.randint(1, 100)


def check_guess(guess, number):
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        return 0


def check_difficulty():
    attempts = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    return attempts


def main():
    print(logo)
    attempts = check_difficulty()
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random_number()
    end = False
    while not end:
        user_guess = int(input("Make a guess: "))
        if check_guess(user_guess, number) == 0:
            print(f"You are right the number is {number}")
            end = True
        elif attempts == 0:
            print(f"You are out of attempts the number is {number}")
            end = True
        else:
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
            print("Guess again.")


main()
