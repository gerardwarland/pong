from turtle import Turtle
import random
BALL_SPEED = 15

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.start()

    def start(self):
        self.goto(0, 0)
        STARTING_HEADING = random.randint(115, 225)
        self.setheading(STARTING_HEADING)

    def move(self):
        self.forward(BALL_SPEED)

