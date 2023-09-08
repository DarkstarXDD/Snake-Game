from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
current_score = 0
speed = 0.25

while is_game_on:

    time.sleep(speed)
    snake.move()
    screen.update()
    score.score_display(current_score)

    # Detect Food Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        speed -= 0.01
        current_score += 1
        score.score_display(current_score)

    # Detect Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect Snake Tail Collision
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
