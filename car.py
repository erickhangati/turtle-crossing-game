from turtle import Turtle
from random import randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.7, stretch_len=1)
        self.setheading(180)
        self.penup()
        self.goto(310, randint(-250, 270))

    def move(self):
        self.forward(10)
