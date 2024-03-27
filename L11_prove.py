#CSE 110 Prove 11

COUNRTY_INDEX = 0
COUNRTY_CODE_INDEX = 1
YEAR_INDEX = 2
LIFE_EXPECTANCY_INDEX = 3


lowest_life = 120
highest_life = 0

with open("life-expectancy.csv") as file:
    for line in file:
        life_data = line.split(",")
        life_exp_in_file = float(life_data[LIFE_EXPECTANCY_INDEX])

        # overall min and max
        if life_exp_in_file < lowest_life:
            lowest_life = life_exp_in_file
            
        if life_exp_in_file > highest_life:
            highest_life = life_exp_in_file



print(f"The overall max life expectancy is: {highest_life}")
print(f"The overall min life expectancy is: {lowest_life}")
