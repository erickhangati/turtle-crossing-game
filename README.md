# Turtle Crossing Game

This is a simple Python game where a turtle tries to cross a road filled with moving cars. The player controls the turtle using the 'Up' arrow key to move it upwards. The objective is to cross the road without getting hit by any cars. The game ends when the turtle collides with a car.

## How to Play

1. Run the `main.py` file.
2. Use the 'Up' arrow key to move the turtle upwards.
3. Dodge the moving cars.
4. The game ends when the turtle collides with a car.
5. The score increases each time the car crosses without hitting the turtle.

## Files

### `crossing_turtle.py`

Contains the class `CrossingTurtle`, which represents the turtle that the player controls. This turtle is responsible for crossing the road.

### `car.py`

Contains the class `Car`, representing the cars that move horizontally across the screen. These cars pose a threat to the turtle, and the player must avoid them.

### `scoreboard.py`

Contains the class `Scoreboard`, which manages and displays the player's score during the game. The score increases each time the turtle successfully crosses the road without getting hit by a car.

### `main.py`

This is the main file that orchestrates the game. It sets up the game environment, creates instances of the turtle, cars, and scoreboard, and handles game logic such as movement, collision detection, and score updating.

## Dependencies

- Python 3.x
- Turtle graphics library

## Running the Game

To play the game, simply run the `main.py` file using Python. Make sure you have the required dependencies (Turtle graphics library) installed.

```bash
python main.py
