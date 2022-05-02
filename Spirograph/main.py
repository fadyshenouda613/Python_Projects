from turtle import Turtle, Screen, colormode
from turtle import *
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.pensize(2)

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(4)

screen = Screen()
screen.exitonclick()
