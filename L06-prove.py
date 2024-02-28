print("Welcome to the Text-Based Adventure Game!")

# Level 1
print("\nYou find yourself standing in front of a mysterious cave entrance.")
print("The air is cool, and the only sound you hear is the gentle rustling of leaves.")
choice = input("Do you ENTER the cave, or turn BACK? ").upper()

if choice == "ENTER":
    # Level 2
    print("\nYou enter the cave, ready to explore its mysteries.")
    print("\nAs you venture deeper into the cave, you encounter two paths diverging.")
    choice = input("Do you take the LEFT path, or CONTINUE straight ahead? ").upper()
    if choice == "LEFT":
        print("\nYou take the left path and find yourself in a chamber filled with glittering gems.")
        print("Congratulations! You've found treasure.")
        # TODO: Add at least one more level to the scenario
        # Level 3 code goes here
    elif choice == "CONTINUE":
        print("\nYou continue straight ahead and stumble into a pit, falling to your demise.")
        print("Game Over! You fell into a trap.")
    else:
        print("\nInvalid choice. Please enter either 'TAKE' or 'CONTINUE'.")

elif choice == "BACK":
    # Level 2
    print("\nYou turn around and walk away from the cave, deciding it's best not to venture into the unknown.")
    print("\nAs you walk away from the cave, you encounter a crossroads.")
    # Scenario must have more thant 2 choices
    choice = input("Do you go LEFT or RIGHT OR go BACK? ").upper()
    if choice == "LEFT":
        print("\nYou go left and find a hidden cave with a treasure chest.")
        # Level 3
        print("Congratulations! You found treasure.")
    elif choice == "RIGHT":
        print("\nYou go right and encounter a group of bandits. They capture you.")
        print("Game Over! You were captured by bandits.")
    elif choice == "BACK":
        print("\nYou turn around and walk away from the crossroads, deciding it's best not to venture into the unknown.")
    else:
        print("\nInvalid choice. Please enter either 'LEFT' or 'RIGHT'.")

else:
    print("\nInvalid choice. Please enter either 'ENTER' or 'TURN BACK'.")

