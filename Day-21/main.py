from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
#creates a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")


#closes the animation 
screen.tracer(0)
# two paddle is created
l_paddle = Paddle((-375,0))
r_paddle= Paddle((375,0))
ball = Ball() 
score=Score()

#movement of paddle
screen.listen()
#movement of right paddle with arrow keys
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

#movement of left paddle with w and s .
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on=True
while game_is_on:
    
    time.sleep(ball.move_speed)
    # all the animation will now take place
    screen.update()
    ball.move()
    if ball.ycor()>=285 or ball.ycor()<=-285:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)<63 and ball.xcor()>330:
        ball.bounce_xr()
    elif ball.distance(l_paddle)<63 and ball.xcor()<-330:
        ball.bounce_xl()
    #detect R paddle miss
    if ball.xcor()>385:
        ball.new()
        score.l_point()
    #detect L paddle miss
    if ball.xcor()<-385:
        ball.new()
        score.r_point()









screen.exitonclick()
