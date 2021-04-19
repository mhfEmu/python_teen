# Seeing python turtle in action
from turtle import Turtle, Screen

mustofa = Turtle()
print(mustofa)
mustofa.shape("turtle")
mustofa.color("red")
mustofa.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
