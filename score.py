from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

    def score_display(self, score):

        self.clear()
        self.write(f"Score : {score}", move=False, align="center", font=("Arial", 18, "normal"))

    def game_over(self):

        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("Arial", 20, "normal"))
