from turtle import Screen
from crossing_turtle import CrossingTurtle
from time import sleep

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# Crossing turtle instance
crossing_turtle = CrossingTurtle()

# Listen for movement key
screen.listen()
screen.onkey(key="Up", fun=crossing_turtle.move)

game_on = True

while game_on:
    screen.update()
    sleep(0.2)

# Keep screen on
screen.exitonclick()
