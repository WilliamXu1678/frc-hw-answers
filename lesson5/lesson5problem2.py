user_info = []

name = raw_input("What is your name? ")
user_info.append(name)

fav_color = raw_input("What is your favorite color? ")
user_info.append(fav_color)

num_pets = raw_input("How many pets do you have? ")
user_info.append(num_pets)

print user_info[0] + "'s favorite color is " + user_info[1] + ". They have " + user_info[2] + " pets."
