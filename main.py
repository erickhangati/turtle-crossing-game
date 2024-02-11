from turtle import Screen
from crossing_turtle import CrossingTurtle
from car import Car
from scoreboard import Scoreboard
from time import sleep

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# Crossing turtle instance
crossing_turtle = CrossingTurtle()

scoreboard = Scoreboard()

# Listen for movement key
screen.listen()
screen.onkey(key="Up", fun=crossing_turtle.move)

# Car instance
car = Car()

game_on = True

while game_on:
    screen.update()
    sleep(0.2)

    # Move car
    car.move()

    # Detect collision
    if crossing_turtle.distance(car) < 15:
        scoreboard.game_over()
        break

    # Update scores
    if car.xcor() < -20 and scoreboard.scores == 0:
        scoreboard.update_scores()

# Keep screen on
screen.exitonclick()
