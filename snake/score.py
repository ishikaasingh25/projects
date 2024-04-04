from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} HighScore : {self.highscore}", align="center",
                   font=("Arial", 14, "normal"))
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()


    """def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center",
                   font=("Arial", 14, "normal"))"""
