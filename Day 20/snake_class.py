from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.gap = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.distance = 20

    # Todo: 1. creating a snake body
    def create_snake(self):
        for _ in range(3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            tim.goto(y=0, x=self.gap)
            self.gap -= 20
            self.snake.append(tim)


    # Todo: 2. moving the snake
    def move_snake(self):
        for num in range(len(self.snake)-1, 0 ,-1):
             new_x = self.snake[num - 1].xcor()
             new_y = self.snake[num - 1].ycor()
             self.snake[num].goto(new_x, new_y)
        self.snake[0].forward(self.distance)

    # Todo: 3. controlling the snake
    def up(self):
        if self.snake[0].heading() != DOWN:
           self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() != UP:
           self.snake[0].setheading(DOWN)
    def right(self):
        if self.snake[0].heading() != LEFT:
           self.snake[0].setheading(RIGHT)
    def left(self):
        if self.snake[0].heading() != RIGHT:
           self.snake[0].setheading(LEFT)

    def extend_snake(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(tim)


# gap = 0
# snake = []
# for _ in range(3):
#     tim = Turtle(shape="square")
#     tim.penup()
#     tim.color("white")
#     tim.goto(y= 0, x=gap)
#     gap -= 20
#     snake.append(tim)





# print(snake)
# play = True
# # for snake in snake:
# while play:
#   screen.update()
#   time.sleep(.2)
#   for num in range(len(snake)-1, 0 ,-1):
#       new_x = snake[num - 1].xcor()
#       new_y = snake[num - 1].ycor()
#       snake[num].goto(new_x, new_y)
#   snake[0].forward(10)







