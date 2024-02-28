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
print("\nWelcome to the word guessing game!")
print("\nYour hint is: _ _ _ _ _ _")

while guess != secret_word:
    guess = input("\nWhat is your guess? ").lower()
    guess_count += 1  # Increment the guess counter

    # get the length of the secret word and the guess
    len_of_secret_word = len(secret_word)
    len_of_guess = len(guess)

    # check if the guess is the same length as the secret word
    if len(guess) != len(secret_word):
        print("Your guess is incorrect. The secret word has 6 letters.")
    elif guess == secret_word: # check if the guess is the same as the secret word
        print("You guessed the secret word!")
    else:
        print("Your hint is: ", end="")
        # loop through the length of the secret word
        for i in range(0, len_of_secret_word):
            # check if the letters in the guess are in the secret word
            # check if the position matches
            if guess[i] == secret_word[i]:
                print(guess[i].upper(), end="")
            elif guess[i] in secret_word: # check if the letter is in the secret word
                print(guess[i].lower(), end="")
            else: # print a blank space if the letter is not in the secret word
                print("_  ", end="")

print("\nNumber of guesses:", guess_count)