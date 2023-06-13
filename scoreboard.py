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
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.print_score()

    def print_gameover(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)


