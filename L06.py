states = ["ID", "AZ", "AK"]

print(states)

states.append("UT")
print(states)

num_list = []
num_list.append(10)
num_list.append(30)

sum = 0
for num in num_list:
    sum += num

print(sum)

print(sum(num_list))