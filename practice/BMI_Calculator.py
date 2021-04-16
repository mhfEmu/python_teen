"""Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a degree of a few's weight taking into account their peak. E.G. If a tall individual and a short man or woman both weigh the equal quantity, the quick individual is normally more obese.

The BMI is calculated by dividing someone's weight (in kg) through the rectangular of their top (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = round(float(weight/ (height**2)))

if BMI < 18.5:
 print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
 print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
 print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
 print(f"Your BMI is {BMI}, you are obese.")
else:
 print(f"Your BMI is {BMI}, you are clinically obese.")