from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)


screen.listen()
screen.onkey(move_forward, "space")

screen.exitonclick()