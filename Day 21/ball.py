from turtle import Turtle, Screen

screen = Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # self.shapesize(stretch_wid=.8, stretch_len=.8)

    def move_ball(self):
        screen.tracer(1)
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        screen.tracer(1)
        self.y_move *= -1

    def bounce_x(self):
        screen.tracer(1)
        self.x_move *= -1