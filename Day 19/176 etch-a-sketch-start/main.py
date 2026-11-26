from turtle import Turtle, Screen
import random as rnd

screen = Screen()

# W = forward
# S = Backward
# A = counter-clockwise
# D = clockwise
#
# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def counter_clockwise():
#     tim.left(90)
# def clockwise():
#     tim.right(90)
# def curf():
#     tim.circle(10)
# def clear():
#     tim.home()
#     tim.clear()
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(counter_clockwise, "a")
# screen.onkey(curf, "y")
# screen.onkey(clear, "c")
# screen.onkey(clockwise, "d")





# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

#Tutle Racing Game

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
print(user_bet)
start_race = False
colours = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
space = -98
turtles = []
for num in range(1, 8):
    speed = rnd.randint(1, 8)
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=space)
    new_turtle.color(colours[num - 1])
    turtles.append(new_turtle)
    space += 28

if user_bet:
    start_race = True

while start_race:
    for turtle in turtles:
        random_distance = rnd.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 220:
            start_race = False
            winner_color = turtle.color()[0]
            if  winner_color == user_bet:
                print(f"You win!, The turtle color {winner_color} has won the race!")
            else:
                print(f"You lose!, The turtle color {winner_color} has won the race!")




screen.exitonclick()
