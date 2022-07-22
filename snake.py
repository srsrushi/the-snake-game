from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-21, 0), (-41, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.snake.append(snake_segment)

    def move_forward(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(20)
