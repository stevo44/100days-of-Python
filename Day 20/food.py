from turtle import Turtle
import random as rnd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        random_x = rnd.randint(-200,200)
        random_y = rnd.randint(-200,200)
        self.goto(random_x,random_y)
    def refresh(self):
        random_x = rnd.randint(-200,200)
        random_y = rnd.randint(-200,200)
        self.goto(random_x,random_y)