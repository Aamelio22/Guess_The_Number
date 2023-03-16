from art import logo
import random

answer = random.choice(range(1, 101))


def compare(guess, attempts):
    '''Compares guess with answer and outputs hint or win message.'''
    right_guess = False
    if guess < answer:
        message = "Too low."
    elif guess > answer:
        message = "Too high."
    else:
        message = f"You got it! The answer was {answer}."
        right_guess = True
    attempts -= 1
    return {"attempts": attempts, "message": message, "right_guess": right_guess}


def game_start():
    '''Starts code to run the game'''
    print(logo)
    print("Welcome to 'Guess The Number'!\nI'm thinking of a number between 1 and 100.")
    difficulty = "null"
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            attempts = 10
            break
        elif difficulty == "hard":
            attempts = 5
            break
        else:
            print("Please enter one of the two options.")
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        while True:
            guess = input("Guess the number:hard ")
            if not guess.isnumeric():
                print("Please only type numbers.")
            else:
                guess = int(guess)
                break
        info = compare(guess, attempts)
        attempts = info["attempts"]
        message = info["message"]
        print(message)
        if info["right_guess"] == True:
            break
        elif attempts == 0:
            print(f"You have {attempts} attempts remaining. The answer was {answer}.\nYou Lose.")
        else:
            print("Guess again.")


game_start()