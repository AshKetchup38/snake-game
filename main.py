from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_over = False

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_over is False:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtles[0].distance(food) < 15:
        score_board.score += 1
        snake.add_tail()
        score_board.update_score()
        food.move_food()
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -280:
        game_over = True
        score_board.print_gameover()
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            game_over = True
            score_board.print_gameover()

screen.exitonclick()
