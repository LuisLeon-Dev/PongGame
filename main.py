from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard


screen = Screen()
r_paddle = Paddle(x=350)
l_paddle = Paddle(x=-350)


# Setting the screen
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()
score_board = Scoreboard()

# right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, key="Down")

# left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, key="s")

screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() > -330:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
