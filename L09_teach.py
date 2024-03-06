

new_num = -1
num_list = []

# build the list of numbers
while new_num != 0:
    new_num = int(input("Enter a number, enter 0 to stop: "))
    if new_num != 0:
        num_list.append(new_num)


# sum the number in the list
print(f"The sum is: {sum(num_list)}")

average = sum(num_list) / len(num_list)
print(f"The average is: {average}")