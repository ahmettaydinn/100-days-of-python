import random
import turtle
from turtle import Turtle, Screen


DIRECTIONS = [0, 90, 180, 270]
timmy_the_turtle = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color


timmy_the_turtle.hideturtle()

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
for i in range(200):
    timmy_the_turtle.setheading(random.choice(DIRECTIONS))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.color(random_color())


screen = Screen()
screen.exitonclick()
