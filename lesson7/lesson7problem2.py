def divisible(dividend, divisor):
    if dividend % divisor == 0:
        return True
    else:
        return False
 
number_one = int(raw_input("Give me an integer:"))
number_two = int(raw_input("Give me another integer:"))

if number_one >= number_two:
    if divisible(number_one, number_two):
        print str(number_one) + " is divisible by " + str(number_two)
    else:
        print str(number_one) + " is not divisible by " + str(number_two)
else:
    if divisible(number_two, number_one):
        print str(number_two) + " is divisible by " + str(number_one)
    else:
        print str(number_two) + " is not divisible by " + str(number_one)
