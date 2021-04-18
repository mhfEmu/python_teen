# calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

item = 0
count = 0
for average in student_heights:
    item = item + average
    count = count + 1
print(round(item / count))
