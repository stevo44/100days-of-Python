from turtle import Turtle, Screen, colormode
import random as rnd
tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
tim.speed(1)

#square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

#
# for _ in range(3):
#     # tim.color('red')
#     tim.forward(50)
#     tim.left(120)


# for _ in range(10):
#      tim.fd(10)
#      tim.up()
#      tim.fd(10)
#      tim.down()
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

# for number in range(3, 11):
#      side = round(360 / number)
#      random_colors = rnd.choice(colors)
#      for _ in range(number):
#        tim.color(random_colors)
#        tim.fd(100)
#        tim.rt(side)

colormode(255)

def random_colors():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    return (r, g, b)

# tim.pensize(10)
# directions = [0, 90, 180, 270]
# play = True
# while play:
#    # random_colors = rnd.choice(colors)
#    randon_direction = rnd.choice(directions)
#    for _ in range(1):
#        tim.color(random_colors())
#        tim.speed("fastest")
#        tim.forward(20)
#        tim.right(randon_direction)

# tim.speed("fastest")
# for _ in range(72):
#     tim.circle(100)
#     tim.left(5)
#     tim.color(random_colors())



tim.pensize(10)
tim.up()
tim.setheading(225)
tim.forward(100)
tim.setheading(0)
for num in range(10):
    for _ in range(10):
        tim.down()
        tim.color(random_colors())
        tim.forward(1)
        tim.up()
        tim.forward(20)
        tim.down()
    tim.up()
    tim.back(210)
    tim.left(-270)
    tim.forward(20)
    tim.right(90)
    tim.down()





screen = Screen()
screen.exitonclick()