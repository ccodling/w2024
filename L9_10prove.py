
menu_choice = -1
cart = []
prices = []

print("Welcome to the shopping Cart Program!")

# build a menu
while menu_choice != "5":
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Total in cart")
    print("5. Quit")
    menu_choice = input("Please enter an action: ")

    if menu_choice == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
        price = float(input(f"What is the price of {item}: "))
        prices.append(price)
    elif menu_choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(cart)):
            print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f}")
            print()
    elif menu_choice == "3":
        item_number = int(input("Which item would you like to remove? ")) - 1
        cart.pop(item_number)
        prices.pop(item_number)
    elif menu_choice == "5":
        print("Thank you. Goodbye!")
    else:
        print("Invalid choice. Please try again.")


