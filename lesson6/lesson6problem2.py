country_array = ["georgia", "laos", "cambodia", "jordan", "burundi", "paraguay", "slovenia", "honduras", "albania", "kazakhstan"]

last_index = len(country_array)-1
reverse_array = []

for i in range(last_index, -1, -1):
    reverse_array.append(country_array[i])

print reverse_array

