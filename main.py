from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Creating objects for classes
snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect Collision with Food
    if snakes.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snakes.extend()

    # Detect collision with wall
    if snakes.head.xcor() > 285 or snakes.head.xcor() < -285 or snakes.head.ycor() > 285 or snakes.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
    # Detect Collision with Tail
    # If head collides with other segments, trigger game over
    for snake in snakes.snake[1:]:
        if snakes.head.distance(snake) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
