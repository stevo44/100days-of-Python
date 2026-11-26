from turtle import Screen
from paddle import Paddle
import time
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l = Paddle((-380, 0))
r = Paddle((380, 0))

ball = Ball()
screen.listen()
screen.update()
screen.onkeypress(r.up, "Up")
screen.onkeypress(r.down, "Down")
screen.onkeypress(l.up, "w")
screen.onkeypress(l.down, "s")

play = True

while play:
    time.sleep(0.1)
    ball.move_ball()

    #Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
       ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r) < 25 and ball.xcor() > 340 or ball.distance(l) < 25 and ball.xcor() < -340 :
        ball.bounce_x()






# time.sleep(0.2)




screen.exitonclick()