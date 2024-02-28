# CSE 110 Lesson 7 Teach Activity
# Cory Codling

# library imports
import random

# As for magic number and the guess
# magic_number = input("What is the magic number? ")
magic_number = random.randint(1, 100)
guess = -1

# keep asking for the guess until the user guesses the magic number
while guess != magic_number:
    guess = int(input("What is your guess? "))
    # Check if the guess is correct
    if guess == magic_number:
        print("You guessed the magic number!")
    elif guess < magic_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")