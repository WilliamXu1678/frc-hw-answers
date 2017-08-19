def change(cents):
  quarters = 0 
  dimes = 0
  nickles = 0
  pennies = 0
  while cents >= 25:
    cents -= 25
    quarters += 1
  while cents >= 10:
    cents -= 10
    dimes += 1
  while cents >= 5:
    cents -= 5
    nickles += 1
  while cents >= 1:
    cents -= 1
    pennies += 1
  return "quarters: " + str(quarters) + "\ndimes: " + str(dimes) + "\nnickles: " + str(nickles) + "\npennies: " + str(pennies)
print change(int(raw_input("Number in cents: ")))
