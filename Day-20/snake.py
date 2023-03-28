from turtle import Turtle, Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
x=0
segments=[]
for i in range(3):
    snake=Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=-x,y=0)
    x+=20
    segments.append(snake)
game_loop=True
while game_loop:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    
    segments[0].fd(20)   
   











screen.exitonclick()