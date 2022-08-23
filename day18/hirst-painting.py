import colorgram

## Extracting the colors from the spot.jpg!
# colors = colorgram.extract('spot.jpg', 20)
#
# my_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     my_colors.append(new_color)
# print(my_colors)

from turtle import Turtle, Screen
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
              (174, 94, 97),
              (176, 192, 209)]

tim = Turtle()
screen = Screen()

screen.colormode(255)
x_position = tim.xcor() - 175
y_position = tim.ycor() - 150


def draw_line():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


def change_line():
    tim.goto(x_position, y_position + 50)


for i in range(10):
    tim.speed(7)
    tim.hideturtle()
    tim.penup()
    tim.goto(x_position, y_position)
    draw_line()
    change_line()
    x_position = tim.xcor()
    y_position = tim.ycor()
    tim.speed(7)

screen.exitonclick()
