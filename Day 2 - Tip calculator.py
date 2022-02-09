print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip_percentage = input("How much tip would you like give? 0, 10, 15 or 20? ")
split = input("How many people to split the bill ")

float_total = float(total)
float_tip_percentage = float(tip_percentage)
int_split = int(split)

sum = (float_tip_percentage / 100) + 1
sum1 = float_total * sum
# sum1 is total amount including bill

sum2 = sum1 / int_split
sum3 = round(sum2, 2)

print(f"Each person should pay: {sum3}")
