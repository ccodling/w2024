# Loop over a list
states = ["Idaho", "Utah", "Washington"]
for state in states:
    print(state)

# Loop over a string
# A string is a list of characters
my_name = "Cory"
for letter in my_name:
    letter = letter + "_"
    print(letter.lower(), end="")

# what does the range function do?
# generates a list of numbers
numbers = range(5, 80, 5)
print()

# simple range
# loop through the values the range function generates
length_of_states = len(states)
length_of_name = len(my_name)
for i in numbers:
    print(i)

print("-------------------")
print(length_of_states)
print(length_of_name)

# get a value from a specific location in the list
# Use square brackets to access a specific location in the list
# The location is called an index
print()
print(numbers[4])

# test if a value exists in a list
if "Idaho" in states:
    print("found it")
else:
    print("not found")
# Use the in operator to test if a value exists in a list
# if it exists, the result is True