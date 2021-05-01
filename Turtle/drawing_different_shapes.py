# drawing different shapes
from turtle import Turtle, Screen
import random

rip = Turtle()
rip.shape("turtle")
rip.setpos(x=0, y=0)

shape_part = 2

# TODO: 2: Need to art 8 Shapes
for _ in range(8):
    color_code = random.randint(100000, 285078)
    rip.color(f"#{color_code}")
    shape_part += 1

    # TODO: 3: Need to move the turtle based on angle
    myAngle = int(round(360 / shape_part))

    # TODO: 1: Need to mark a starter position for further uses
    if not rip.home():
        for _ in range(shape_part):
            rip.forward(100)
            rip.right(myAngle)
    else:
        pass

myWindow = Screen()
myWindow.exitonclick()
