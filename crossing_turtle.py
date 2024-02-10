from turtle import Turtle


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("brown")
        self.penup()
        self.goto(0, -280)

    def move(self):
        """
        Move the crossing turtle forward.
        :return: None
        """
        self.forward(10)
