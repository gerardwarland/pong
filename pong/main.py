from turtle import Screen
from paddle import Paddle
from paddle2 import Paddle2
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle = Paddle()
paddle2 = Paddle2()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up2, "w")
screen.onkey(paddle2.down2, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.distance(paddle) < 30:
        if ball.heading() == 180:
            new_heading = 0
        elif ball.heading() < 180:
            new_heading = 180 - ball.heading()
        else:
            new_heading = 360 - (ball.heading() - 180)
        ball.setheading(new_heading)

    if ball.distance(paddle2) < 30:
        if ball.heading() == 180:
            new_heading = 0
        elif ball.heading() < 180:
            new_heading = 180 - ball.heading()
        else:
            new_heading = 360 - (ball.heading() - 180)
        ball.setheading(new_heading)

    # detect collision with top wall
    if ball.ycor() > 280:
        if ball.heading() < 90:
            new_heading = 360 - ball.heading()
        else:
            new_heading = 180 + (180 - ball.heading())
        ball.setheading(new_heading)

    # detect collision with bottom wall
    if ball.ycor() < -280:
        if ball.heading() < 270:
            new_heading = 180 - (ball.heading() - 180)
        else:
            new_heading = 360 - ball.heading()
        ball.setheading(new_heading)

    # detect collision with top wall
    if ball.xcor() > 290:
        if ball.heading() < 90:
            new_heading = 360 - ball.heading()
        else:
            new_heading = 180 + (180 - ball.heading())
        ball.setheading(new_heading)

    # player 2 scores
    if ball.xcor() < -280:
        ball.start()
        paddle.start()
        paddle2.start()
        scoreboard.increase_score2()

    # player 1 scores
    if ball.xcor() > 280:
        ball.start()
        paddle.start()
        paddle2.start()
        scoreboard.increase_score()

    if scoreboard.score > 6:
        game_is_on = False
        scoreboard.game_over()
        print("Player 1 wins!")

    if scoreboard.score2 > 6:
        game_is_on = False
        scoreboard.game_over()
        print("Player 2 wins!")







screen.exitonclick()
