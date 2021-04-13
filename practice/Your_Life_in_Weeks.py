"""
Create a software the use of maths and f-Strings that tells us how many days, weeks, months we've left if we stay until ninety years vintage.

It will take your current age as the input and output a message with our time left in this format:

    you have got x days, y weeks, and z months left.
"""


age = input("What is your current age?")
user_age = int(age)
year_left = 90-user_age
DAYS = int(365*year_left)
WEEKS = int(year_left*52)
MONTHS = int(year_left*12)
print(f"You have {DAYS} days, {WEEKS} weeks, and {MONTHS} months left.")
