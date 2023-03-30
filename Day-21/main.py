from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
#creates a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")


#closes the animation 
screen.tracer(0)
# two paddle is created
l_paddle = Paddle((-380,0))
r_paddle= Paddle((380,0))
ball = Ball() 
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
    
    time.sleep(0.1)
    # all the animation will now take place
    screen.update()
    ball.move()
    if ball.ycor()>=300 or ball.ycor()<=-285:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>350 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()
screen.exitonclick()








screen.exitonclick()
