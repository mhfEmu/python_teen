# drawing a spirograph
from turtle import Turtle, Screen, colormode
import random

rip = Turtle()
colormode(255)
rip.pensize(1)
rip.speed(100)


def random_color():
    r = (random.randint(1, 255))
    g = (random.randint(1, 255))
    b = (random.randint(1, 255))
    my_tuple = (r, g, b)
    return my_tuple


my_angle = 0

for _ in range(1, 73):
    rip.color(random_color())
    rip.circle(100)
    rip.home()
    my_angle += 5
    rip.left(my_angle)

random_color()

myWindow = Screen()
myWindow.exitonclick()