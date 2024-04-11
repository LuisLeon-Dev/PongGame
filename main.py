from turtle import Screen, Turtle

screen = Screen()
paddle = Turtle()

# Setting the screen
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")

paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.setpos(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.onkey(go_up, "Up")
screen.onkey(go_down, key="Down")
screen.listen()

screen.exitonclick()
