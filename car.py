from turtle import Turtle
import random

COLORS = ["#DC143C", "#FFD700", "#3CB371", "#4169E1", "#9932CC", "#FF1493", "#FF6347"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(280, random.randint(-250, 250))

    def move(self):
        self.forward(10)
