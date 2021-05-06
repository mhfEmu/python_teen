# Turtle Racing
from turtle import Turtle, Screen
import random

is_race_on = False
window = Screen()
window.setup(width=600, height=400)
user_bet = window.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    rip = Turtle(shape="turtle")
    rip.color(colors[turtle_index])
    rip.penup()
    rip.goto(x=-280, y=y_positions[turtle_index])
    all_turtles.append(rip)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

window.exitonclick()
