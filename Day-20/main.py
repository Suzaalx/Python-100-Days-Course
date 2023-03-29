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
   
screen.exitonclick()