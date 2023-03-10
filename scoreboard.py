from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.hideturtle()
        self.color("White")
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", False, "center", ("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over. Your Score is {self.score}", False, "center", ("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
