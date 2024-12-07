# Creating the Number Guessing Game

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

def random_number():
    print("I'm thinking of a number between 1 and 100.")
    number = int(random.choice(range(1,101)))
    print(f"(Spoiler, it's {number}.)")
    return number

def guessing(attempts, number):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < 1 or guess > 100:
            print("Invalid input. Please enter a number from 1 to 100.")
            continue
        if guess > number:
            attempts -= 1
            print("Too high.\nGuess again.")
        elif guess < number:
            attempts -= 1
            print("Too low.\nGuess again.")
        else:
            print(f"You win! The number was indeed {number}!")
            return 
    print(f"You've run out of guesses. Game over. The number was {number}.")

def initialize_game():
    number = random_number()
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            attempts = 10
            break
        elif difficulty == "hard":
            attempts = 5
            break
        print("Invalid input. Please type 'easy' or 'hard'.")
    guessing(attempts, number)

initialize_game()