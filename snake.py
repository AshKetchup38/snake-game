from turtle import Turtle
STARTING = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create()

    def create(self):
        for pos in STARTING:
            self.add_body(pos)

    def add_body(self, pos):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setposition(pos)
        self.turtles.append(new_turtle)

    def add_tail(self):
        position = self.turtles[-1].pos()
        self.add_body(position)

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            self.turtles[num].setposition(self.turtles[num - 1].xcor(), self.turtles[num - 1].ycor())
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(0)

    def reset(self):
        for t in self.turtles:
            t.goto(1000,1000)
        self.turtles.clear()
        self.create()
        
