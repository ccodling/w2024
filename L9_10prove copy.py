
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
    print("4. Compute total")
    print("5. Quit")
    menu_choice = input("Please enter an action: ")

    if menu_choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        cart.append(item)
        prices.append(price)
        print(f"'{item}' has been added to your cart.\n")
    elif menu_choice == "2":
        print("The contents of the shopping cart are: ")
        for i in range(len(cart)): 
            print(f"{i+1} {cart[i]} - ${prices[i]:.2f}")
        print()
    elif menu_choice == "3":
        index = int(input("Which item would you like to remove? ")) - 1
        # set the index to the value of the item to be removed
        cart.pop(index)
        prices.pop(index)
        print(f"Item {index+1} has been removed from your cart.\n")
    elif menu_choice == "4":
        # compute the total
        total = 0
        # total = sum(prices)
        for price in prices:
            total += price
        print(f"The total price of the items in your cart is ${total:.2f}.\n")
    elif menu_choice == "5":
        print("Thank you. Goodbye!")
    else:
        print("Invalid choice. Please try again.")


