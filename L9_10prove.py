
menu_choice = -1
cart = []

print("Welcome to the shopping Cart Program!")

# build a menu
while menu_choice != "5":
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("5. Quit")
    menu_choice = input("Please enter an action: ")

    if menu_choice == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
    elif menu_choice == "2":
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
    elif menu_choice == "5":
        print("Thank you. Goodbye!")
    else:
        print("Invalid choice. Please try again.")


