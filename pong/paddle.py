from turtle import Turtle
PADDLE_SPEED = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=0.3)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")
        self.start()

    def start(self):
        self.goto(-280, 0)

    def up(self):
        self.setheading(90)
        self.forward(PADDLE_SPEED)

    def down(self):
        self.setheading(270)
        self.forward(PADDLE_SPEED)