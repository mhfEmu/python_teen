"""Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a degree of a few's weight taking into account their peak. E.G. If a tall individual and a short man or woman both weigh the equal quantity, the quick individual is normally more obese.

The BMI is calculated by dividing someone's weight (in kg) through the rectangular of their top (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv
"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w = float(weight)
h = float(height)
print(int(w/(h**2)))
