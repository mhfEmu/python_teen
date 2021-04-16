# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
rand = len(names)
host = random.randint(0, rand-1)
print(f"{names[host]} is going to buy the meal today!")