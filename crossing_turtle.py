from turtle import Turtle


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("brown")
        self.penup()
        self.reset_turtle()

    def move(self):
        """
        Move the crossing turtle forward.
        :return: None
        """
        self.forward(10)

    def reset_turtle(self):
        self.goto(0, -280)
