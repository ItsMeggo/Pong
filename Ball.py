from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.xmove = 10
        self.ymove = 10

    def move(self):

        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *=  -1

    def position_reset(self):
        ball.goto(0, 0)
        ball.bounce_x()