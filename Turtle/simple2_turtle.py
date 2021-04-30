# Drawing a square
from turtle import Turtle, Screen

mustofa_the_turtle = Turtle()
mustofa_the_turtle.shape("turtle")
mustofa_the_turtle.color("ForestGreen")

for _ in range(4):
    mustofa_the_turtle.forward(100)
    mustofa_the_turtle.right(90)
# mustofa_the_turtle.forward(100)
# mustofa_the_turtle.right(90)
# mustofa_the_turtle.forward(100)
# mustofa_the_turtle.right(90)
# mustofa_the_turtle.forward(100)
# mustofa_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
