#CSE 110 Prove 11

COUNRTY_INDEX = 0
COUNRTY_CODE_INDEX = 1
YEAR_INDEX = 2
LIFE_EXPECTANCY_INDEX = 3

max_country = ""
min_country = ""
max_year = ""
min_year = ""

lowest_life = 120
highest_life = 0

max_country_by_year = ""
min_country_by_year = ""

min_life_by_year = 0
max_life_by_year = 120


year_of_interest = input("Enter a year of interest: ")

with open("life-expectancy.csv") as file:
    for line in file:
        life_data = line.split(",")
        life_exp_in_file = float(life_data[LIFE_EXPECTANCY_INDEX])

        # overall min
        if life_exp_in_file < lowest_life:
            lowest_life = life_exp_in_file
            min_country = life_data[COUNRTY_INDEX]
            min_year = life_data[YEAR_INDEX]
            
        # overall max
        if life_exp_in_file > highest_life:
            highest_life = life_exp_in_file
            max_country = life_data[COUNRTY_INDEX]
            max_year = life_data[YEAR_INDEX]

        # by year given
        if life_data[YEAR_INDEX] == year_of_interest:
            # min by year
            if life_exp_in_file < min_life_by_year:
                min_country_by_year = life_data[COUNRTY_INDEX]
                min_life_by_year = life_exp_in_file

            #max by year
            if life_exp_in_file > max_life_by_year:

            




print(f"The overall max life expectancy is: {highest_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {lowest_life} from {min_country} in {min_year}")
