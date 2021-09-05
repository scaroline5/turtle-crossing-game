from turtle import Turtle

MOVEMENT_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(MOVEMENT_DISTANCE)

    def reset(self):
        self.clear()
        self.goto(0, -280)


