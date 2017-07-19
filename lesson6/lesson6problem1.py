input_array = []

while True:
    user_input = raw_input("Give me a word:")
    input_array.append(user_input)
    if user_input == "stop":
        break
      
print input_array
