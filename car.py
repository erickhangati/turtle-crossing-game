from turtle import Turtle, colormode
from random import randint

# Set color mode
colormode(255)


def generate_colors():
    """
    Generate tuple of the RGB colors
    :return: type - tuple: RGB colors
    """
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
        """
        Move car forwards.
        :return: None
        """
        self.forward(10)
