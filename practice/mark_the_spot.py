# Mark The Treasure Spot
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

num1 = int((position[0]))
num2 = int((position[1]))

map[num2-1][num1-1] = "X"

print(f"{row1}\n{row2}\n{row3}")