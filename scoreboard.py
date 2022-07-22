from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_score()

    def get_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align='center', font=('Arial', 21, 'normal'))
        self.hideturtle()
        self.score += 1

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 21, 'normal'))
        self.hideturtle()


