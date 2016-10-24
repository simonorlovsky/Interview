import sys
data = sys.stdin.readlines()
mealCost = float(data[0][:-1])
tip = float(data[1][:-1])*.01
tax = float(data[2])*.01
totalCost = mealCost * tip + mealCost * tax + mealCost

print("The total meal cost is {} dollars.".format(round(float(totalCost))))