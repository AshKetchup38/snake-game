from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 15, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.color("white")
        self.setposition(0, 270)
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score} High score: {self.highscore}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.print_score()
    
    def check_score(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


