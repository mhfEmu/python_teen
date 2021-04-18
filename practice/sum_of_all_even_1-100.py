# calculates the sum of all the even numbers from 1 to 100, including 2 and 100.

even_plus = 0
for number in range(2, 101, 2):
    even_plus += number
print(even_plus)

total2 = 0
for number in range(1, 101):
    if (number % 2) == 0:
        total2 += number
print(total2)
