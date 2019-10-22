import random
from enum import Enum


class Trin(Enum):
    LOW = False
    RIGHT = True
    HIGH = False


def check_number(guess: int, actual: int) -> Trin:
    if guess > actual:
        return Trin.LOW
    elif guess < actual:
        return Trin.HIGH
    else:
        return Trin.RIGHT


def main() -> None:
    number_to_guess = random.randrange(0, 101)
    guessed = False
    while not guessed:
        try:
            user_guess = int(input("Your guess please: "))
        except ValueError:
            print("That's not a valid input. Please enter an integer.")
            continue
        try:
            assert 0 <= user_guess <= 100
        except AssertionError:
            print("WRONG. Enter a number between 0 and 100.")
            continue

        guessed = check_number(user_guess, number_to_guess).value
        if not guessed:
            print("TOO %s" % check_number(user_guess, number_to_guess))
    print("You win!")
