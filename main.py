from turtle import Screen

from paddle import Paddle

screen = Screen()
r_paddle = Paddle(x=350)
l_paddle = Paddle(x=-350)

# Setting the screen
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)


# right paddle 
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, key="Down")

# left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, key="s")
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
