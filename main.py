from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time


screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_score = 0
l_score = 0

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball((0,0))


screen.listen(screen.onkey(r_paddle.go_up, "Up"))
screen.listen(screen.onkey(r_paddle.go_down, "Down"))

screen.listen(screen.onkey(l_paddle.go_up, "w"))
screen.listen(screen.onkey(l_paddle.go_down, "s"))

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #score and restart
    if ball.xcor() > 350:
        l_score +=1
        ball.position_reset()
        time.sleep(1)

    if ball.xcor() < -350:
        r_score +=1
        ball.position_reset()
        time.sleep(1)

screen.exitonclick()