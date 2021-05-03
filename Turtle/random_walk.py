# Random Walk
from turtle import Turtle, Screen
import random

rip = Turtle()
rip.shape("classic")
rip.pensize(5)

# TODO: 2: Need to initialize chosen COLORS
colours = ["wheat", "DarkOrchid", "SeaGreen", "IndianRed", "CornflowerBlue", "LightSeaGreen", "DeepSkyBlue", "SlateGray"]

# TODO: 1: Need to initialize angles
myAngle = [0, 90, 180, 270, 360]

# TODO: 4: Need to make Random Walk
for _ in range(1, 1001):
    rip.color(random.choice(colours))
    angle = (random.choice(myAngle))
    rip.forward(25)
    rip.right(angle)


myWindow = Screen()
myWindow.exitonclick()
