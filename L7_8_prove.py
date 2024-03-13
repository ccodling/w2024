# CSE 110 Lesson 7 and 8 Prove Activity
# Cory Codling

# Milestone steps
# Store a secret word in a variable
secret_word = "mosiah"

# initialize the user's guess
guess = ""

# Loop until the user guesses the secret word
# Ask the user to guess the secret word
# Calculate the number of guesses
guess_count = 0  # Initialize the guess counter

# Print the welcome message and the hint

while guess != secret_word:
    print("Your hint is: _ _ _ _ _ _")
    guess = input("What is your guess? ").lower()
    guess_count += 1  # Increment the guess counter

    # get the length of the secret word and the guess
    length_of_secret = len(secret_word)
    length_of_guess = len(guess)
    # check if the guess is the same length as the secret word
    if length_of_secret != length_of_guess:
        print("Your guess is not the correct length")
        # print success message if the guess is the same as the secret word
    elif secret_word == guess:
        print("You guessed the secret word.")
        # loop through the length of the secret word
    else:
        for i in range(length_of_secret):
            # check if the letters in the guess are in the secret word
             # check if the position matches
            if guess[i] == secret_word[i]:
                print(guess[i].upper(), end=" ")
            # check if the letter is in the secret word
            elif guess[i] in secret_word:
                print(guess[i].lower(), end=" ")
            # print a blank space if the letter is not in the secret word
            else:
                print("_", end=" ")
    print()


