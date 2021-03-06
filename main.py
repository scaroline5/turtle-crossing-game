from scoreboard import Scoreboard
from turtle import Screen
from player import Player
from car import Car
import time

# Create Screen, set size and title
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
# Set screen animation off
screen.tracer(0)

# Listen to keyboard
screen.listen()

# Create the Turtle
turtle = Player()

# Move Turtle
screen.onkeypress(key="Up", fun=turtle.move)

# Create Scoreboard
scoreboard = Scoreboard()

# Create Car
cars = []

# Control the game state
game_is_on = True
counter = 0

while game_is_on:

    # Refresh screen every 0.1 seconds
    time.sleep(0.1)
    screen.update()
    counter += 1

    # Create new cars
    if counter == 4:
        new_car = Car()
        cars.append(new_car)
        counter = 0

    # Keep the cars moving
    for car in cars:
        car.move()

    # Detect if turtle reached the finish line
    if turtle.ycor() > 280:
        turtle.reset()
        scoreboard.update_score()
        for car in cars:
            car.increase_speed()

    # Detect Collision of a car with the Turtle
    for car in cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()