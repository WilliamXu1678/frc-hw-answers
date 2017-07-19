country_array = ["georgia", "laos", "cambodia", "jordan", "burundi", "paraguay", "slovenia", "honduras", "albania", "kazakhstan"]

last_index = len(country_array)-1
reverse_array = []

for i in range(last_index, -1, -1): #The parameters for range() are (number to count from, number to end at (not including that number), step to count through range). For the last parameter, if it is two, it means to go up by two every time. In this case, it is -1, so range() will go down one every time.
    reverse_array.append(country_array[i])

print reverse_array

