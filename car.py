from turtle import Turtle, colormode
from random import randint

colormode(255)


def generate_colors():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=1)
        self.color(generate_colors())
        self.setheading(180)
        self.penup()
        self.goto(310, randint(-250, 270))
        self.counted = False

    def move(self):
        self.forward(10)

