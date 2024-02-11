# Turtle Crossing Game

Guide a turtle across a busy road, dodging cars to reach safety. Score points for each successful crossing. Python-based, fun for all ages!

## How to Play

1. Run the `main.py` file.
2. Use the 'Up' arrow key to move the turtle upwards.
3. Dodge the moving cars.
4. The game ends when the turtle collides with a car.
5. The score increases each time a car passes without hitting the turtle.
6. The level increases when the turtle successfully crosses to the other side of the road. Resetting back to the starting point on a new level and the speed of cars increases.

## Files

### `crossing_turtle.py`

Contains the class `CrossingTurtle`, which represents the turtle that the player controls. This turtle is responsible for crossing the road. Now includes a `reset_turtle` method to set the turtle's position.

### `car.py`

Contains the class `Car`, representing the cars that move horizontally across the screen. These cars pose a threat to the turtle, and the player must avoid them.

### `scoreboard.py`

Contains the class `Scoreboard`, which manages and displays the player's score and level during the game. Now includes a `level` attribute and methods to display and update the level.

### `main.py`

This is the main file that orchestrates the game. It sets up the game environment, creates instances of the turtle, cars, and scoreboard, and handles game logic such as movement, collision detection, score updating, and level progression.

## Dependencies

- Python 3.x
- Turtle graphics library

## Running the Game

To play the game, simply run the `main.py` file using Python. Make sure you have the required dependencies (Turtle graphics library) installed.

```bash
python main.py
