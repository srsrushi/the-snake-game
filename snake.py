from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-21, 0), (-41, 0)]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.move_speed = 0.1

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.make_snake(position)

    def make_snake(self, position):
        snake_segment = Turtle("circle")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake.append(snake_segment)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)

        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.move_speed = 0.1

    def grow(self):
        self.make_snake(self.snake[-1].position())

    def move_forward(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.head.forward(FORWARD_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
