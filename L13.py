# determine if a number is a prime number
def is_prime(number):
    name = "Cory"
    print(f"in the function: -- {name}")
    if number < 2:
        return False
    elif number % 2 == 1 or number == 2:
        return True
    else:
        return False

number = int(input("What number would you like to test as a prime number:"))

print(is_prime(number))