from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-240, 265)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "bold"))
