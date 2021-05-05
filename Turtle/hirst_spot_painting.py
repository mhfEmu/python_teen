# Hirst Spot Painting
import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 35)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

extracted_color = [(61, 103, 147), (224, 202, 110), (218, 146, 77), (126, 89, 62), (137, 175, 201), (195, 146, 171),
                   (145, 76, 99), (193, 80, 112), (216, 91, 65), (69, 110, 92), (136, 181, 138), (154, 135, 64),
                   (58, 158, 105), (41, 157, 188), (184, 191, 203), (217, 176, 190), (113, 123, 148), (18, 58, 89),
                   (20, 66, 119), (232, 172, 158), (169, 206, 178), (154, 32, 47), (161, 203, 213), (75, 57, 42),
                   (221, 206, 19), (137, 42, 35), (81, 65, 43), (52, 72, 65), (45, 67, 59), (14, 77, 111)]

rip = t.Turtle()
# rip.shape("classic")
rip.hideturtle()
t.colormode(255)
my_window = t.Screen()
my_window.title("Hirst Spot Painting")
rip.speed("fastest")

rip.penup()
x_coordinates = -250
y_coordinates = -200
rip.goto(x_coordinates, y_coordinates)

for _ in range(1, 101):
    rip.goto(x_coordinates, y_coordinates)

    # TODO: 2: Dot size should in between 20
    rip.dot(20, (random.choice(extracted_color)))
    x_coordinates += 50

    # TODO: 1: 10x10 pace of Art
    if x_coordinates == 250:
        x_coordinates = -250

        # TODO: 3: Dot spaces should be within 50 distance
        y_coordinates += 50

my_window.exitonclick()
