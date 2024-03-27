#CSE 110 Prove 11

COUNRTY_INDEX = 0
COUNRTY_CODE_INDEX = 1
YEAR_INDEX = 2
LIFE_EXPECTANCY_INDEX = 3


lowest_life = 120
highest_life = 0
country_max = ""
country_min = ""
year_max = ""
year_min = ""
max_life_exp_by_year = 0
min_life_exp_by_year = 120
max_country_by_year = ""
min_country_by_year = ""
total_life_exp = 0
counter = 0

year_of_interest = input("Enter a year of interest: ")

with open("life-expectancy.csv") as file:
    for line in file:
        life_data = line.split(",")
        life_exp_in_file = float(life_data[LIFE_EXPECTANCY_INDEX])

        # overall min and max
        if life_exp_in_file < lowest_life:
            lowest_life = life_exp_in_file
            country_min = life_data[COUNRTY_INDEX]
            year_min = life_data[YEAR_INDEX]
            
        if life_exp_in_file > highest_life:
            highest_life = life_exp_in_file
            country_max = life_data[COUNRTY_INDEX]
            year_max = life_data[YEAR_INDEX]

        # min and max for a specific year
        if life_data[YEAR_INDEX] == year_of_interest:
            if life_exp_in_file < min_life_exp_by_year:
                min_life_exp_by_year = life_exp_in_file
                min_country_by_year = life_data[COUNRTY_INDEX]
        
            if life_exp_in_file > max_life_exp_by_year:
                max_life_exp_by_year = life_exp_in_file
                max_country_by_year = life_data[COUNRTY_INDEX]

            #sum of all life expectancies
            counter += 1
            total_life_exp += life_exp_in_file

#life expectancy average
average_life_exp = total_life_exp / counter

print(f"The overall max life expectancy is: {highest_life} from {country_max} in {year_max}")
print(f"The overall min life expectancy is: {lowest_life} from {country_min} in {year_min}")
print()
print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was: {average_life_exp:.2f}")
print(f"The max life expectancy was in {max_country_by_year} with {max_life_exp_by_year}")
print(f"The min life expectancy was in {min_country_by_year} with {min_life_exp_by_year}")