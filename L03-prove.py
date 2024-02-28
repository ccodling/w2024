# Lesson 3/4 Prove Assignment
# Cory Codling

# Ask the user for the price of a child and an adult
# meal and store these values properly into variables as floating point numbers.
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask the user for the number of adults and children and store these values
# properly into variables as integers.

num_children = int(input("How many children are there? "))
num_adult = int(input("How many adult are there? "))

# Ask the user for the sales tax rate and store the value properly as a floating point number.
tax_rate = float(input("What is the sales tax rate? "))

# Compute and display the subtotal (don't worry about rounding to two decimals at this point).
child_total = child_meal_price * num_children
adult_total = adult_meal_price * num_adult

# Calculate totals
sub_total = child_total + adult_total
sales_tax = sub_total * tax_rate / 100
total_sale = sub_total + sales_tax

# print subtotal
print()
print(f"Subtotal: ${sub_total}")
print(f"Sales Tax ${sales_tax:.2f}")
print(f"Total ${total_sale:.2f}")

# Payment and change
print()
payment = float(input("What is the payment amount? "))
change_amount = payment - total_sale
print(f"Change ${change_amount:.2f}")