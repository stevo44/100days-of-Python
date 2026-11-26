from turtle import Screen
from snake_class import Snake
import time
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
play = True
while play:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()

#Todo: 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

# Todo: 6. Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        play = False
        score.game_over()

# Todo: 7. Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            play = False
            score.game_over()


screen.exitonclick()