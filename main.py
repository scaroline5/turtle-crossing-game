from turtle import Turtle, Screen
import time

# Create Screen, set size and title
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
# Set screen animation off
screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()



