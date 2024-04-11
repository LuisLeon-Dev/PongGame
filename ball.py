from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")

    def move(self):
        self.penup()
        x_cor = self.xcor() + 2
        y_cor = self.ycor() + 2
        self.goto(x_cor, y_cor)
