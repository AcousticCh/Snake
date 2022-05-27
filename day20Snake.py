#!usr/bin/env python3
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()

screen.title("Snake Clone")
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score = ScoreBoard()
snake_head = snake.segment[0:1]
	
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.segment[0]) <= 17:
        food.move()
        snake.extend()
        score.add_point()
    if snake.segment[0].xcor() >= 300 or snake.segment[0].ycor() >= 300:
        snake.reset()
        score.reset()
    if snake.segment[0].xcor() <= -300 or snake.segment[0].ycor() <= -300:
        snake.reset()
        score.reset()
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
	
    # detect collision with tail
    for s in snake.segment[1:]:
        if snake.segment[0].distance(s) < 10:
            snake.reset()
            score.reset()
			
		
	
		


screen.exitonclick()
