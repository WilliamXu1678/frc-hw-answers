age = int(raw_input("How old are you? "))

if age < 13:
    print "You're young!"
elif age < 16:
    print "You're not too young, but you can't drive :(. BUT you can join the robotics team and drive our robot!!!"
elif age < 18:
    print "Congrats, you can drive but you're still a minor!"
elif age < 35:
    print "Adult in the house!!!"
else:
    print "You could be president!!!!!!!"
