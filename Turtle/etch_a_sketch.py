# etch a sketch
from turtle import Turtle, Screen

rip = Turtle()
rip.shape("classic")
window = Screen()
window.listen()


# TODO:1: W Forwards
def forwards():
    rip.forward(10)


# TODO:2: S Backwards
def backwards():
    rip.backward(10)


# TODO:3: A Counter-Clockwise
def counter_clock():
    rip.left(10)
    # new_heading = rip.heading() -10
    # rip.setheading(new_heading)


# TODO:4: D Clockwise
def clock():
    rip.right(10)
    # new_heading = rip.heading() +10
    # rip.setheading(new_heading)


# TODO:5: C Clear Drawing
def clear():
    rip.penup()
    rip.clear()
    rip.home()
    rip.pendown()


window.onkey(key="w", fun=forwards)
window.onkey(key="s", fun=backwards)
window.onkey(key="d", fun=clock)
window.onkey(key="a", fun=counter_clock)
window.onkey(key="c", fun=clear)
window.exitonclick()
