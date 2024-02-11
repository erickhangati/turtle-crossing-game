from turtle import Screen
from crossing_turtle import CrossingTurtle
from car import Car
from scoreboard import Scoreboard
from time import sleep
from random import randint

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
cars = []

game_on = True


# Function to create a car at a random interval
def create_car():
    car = Car()
    cars.append(car)
    interval = randint(1000, 2000)  # Random interval between 1 and 3 seconds

    if game_on:
        screen.ontimer(create_car, interval)


create_car()

while game_on:
    screen.update()
    sleep(0.2)

    for vehicle in cars:

        # Move car
        vehicle.move()

        # Detect collision
        if crossing_turtle.distance(vehicle) < 15:
            scoreboard.game_over()
            game_on = False
            break

        # Update scores
        if vehicle.xcor() < -20 and not vehicle.counted:
            scoreboard.update_scores()
            vehicle.counted = True

# Keep screen on
screen.exitonclick()
