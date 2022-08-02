from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_score()
        self.highest_score = self.get_high_score()

    def get_high_score(self):
        with open('highscore.txt') as file:
            return int(str(file.read()))

    def write_high_score(self):
        with open('highscore.txt', 'w') as file:
            file.write(f"{self.highest_score}")

    def get_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align='center', font=('Arial', 21, 'normal'))
        self.hideturtle()

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            self.write_high_score()

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highest score: {self.highest_score}", align='center', font=('Arial', 21, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

