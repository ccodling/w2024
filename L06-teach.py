# CSE 110 L06
# Cory Codling

# can't ride - default
can_ride = False

# Prompt the user for the age and height of the first person. Then, ask whether there is a second rider,
# and if so, ask for their age and height.
rider1_age = int(input("Enter the age of the first rider: "))
rider1_height = int(input("Enter the height of the first rider in inches: "))
is_second_rider = input("Is there a second rider? (yes/no) ").lower()

# if there is a second rider get their info
if is_second_rider == "yes":
    rider2_age = int(input("Enter the age of the second rider: "))
    rider2_height = int(input("Enter the height of the second rider in inches: "))
    if rider1_age >= 18 or rider2_age >= 19:
        can_ride = True

elif is_second_rider == "no":
    # is the first rider able to ride alone
    if rider1_age >= 18 and rider1_height >= 62:
        can_ride = True
else:
    print("in correct value I don't know what to do.")



# print the result
if can_ride == True:
    print("You can ride, have fun")
else:
    print("You can't ride, sorry.")



