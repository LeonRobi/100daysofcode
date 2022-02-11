height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height1 = float(height)
weight1 = float(weight)

# sum1 = (height1 * height1)
# sum = weight1 / sum1

sum = round(weight1 / (height1 * height1))

roundedsum = int(sum)

if roundedsum < 18.5:
    print(f"Your BMI is {roundedsum}, you are underweight.")
elif roundedsum < 25:
    print(f"Your BMI is {roundedsum}, you have a normal weight.")
elif roundedsum < 30:
    print(f"Your BMI is {roundedsum}, you are slightly overweight.")
elif roundedsum < 35:
    print(f"Your BMI is {roundedsum}, you are obese.")
else:
    print(f"Your BMI is {roundedsum}, you are clinically obese.")
