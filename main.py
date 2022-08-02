from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia 3310s Retro Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move_forward()
    scoreboard.update_scoreboard()

    # if snake collides with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        snake.move_speed *= 0.9
        scoreboard.increase_score()

    # if snake collides with the walls
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    # if snake collides with itself
    for snake_body in snake.snake[1:]:
        if snake_body.distance(snake.head) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
