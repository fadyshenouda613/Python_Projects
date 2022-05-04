import time
import turtle
from turtle import Screen, Turtle

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        score.game_over()
    # detect collision with tail
    # trigger game_over
    for segment in snake.snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    snake.move()

screen.exitonclick()
