COUNTY_INDEX = 0
COUNTRY_ABBR_INDEX = 1
YEAR_INDEX = 2
LIFE_EXPECTANCY_INDEX = 3

lowest_life_expectancy = 110

with open("life-expectancy.csv") as file:
    for line in file:
        life_data = line.split(",")
        life_expectancy = float(life_data[LIFE_EXPECTANCY_INDEX])
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy

print("The lowest life expectancy is", lowest_life_expectancy)