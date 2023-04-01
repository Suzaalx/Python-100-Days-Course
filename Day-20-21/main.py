from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_loop=True
while game_loop:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision wuth food
    if snake.segments[0].distance(food)<15:
        print("nomnom")
        food.refresh()
        score.points()
        snake.extend()
    #detect collison with the wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()< -280 or snake.segments[0].ycor()> 280 or snake.segments[0].xcor()< -280:
        score.reset()
        snake.reset()
    #detect collision with tail.
    for segment in snake.segments[1:]:
        
        if snake.segments[0].distance(segment)<10:
            score.reset()
            snake.reset()
screen.exitonclick()