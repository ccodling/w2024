# CSE 110 Lesson 7 and 8 Prove Activity
# Cory Codling

# Milestone steps
# Store a secret word in a variable
secret_word = "python"

# initialize the user's guess
guess = ""

# Loop until the user guesses the secret word
# Ask the user to guess the secret word
# Calculate the number of guesses
guess_count = 0  # Initialize the guess counter

# Print the welcome message and the hint

while guess != secret_word:
    guess = input("What is your guess? ")
    guess_count += 1  # Increment the guess counter

    # get the length of the secret word and the guess
    # check if the guess is the same length as the secret word
        # print success message if the guess is the same as the secret word
    # loop through the length of the secret word
        # check if the letters in the guess are in the secret word
            # check if the position matches
            # check if the letter is in the secret word
            # print a blank space if the letter is not in the secret word
    
    if guess == secret_word:
        print("You guessed the secret word!")
    else:
        print("Your guess is incorrect.")

print("Number of guesses:", guess_count)
