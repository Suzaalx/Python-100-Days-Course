from turtle import Turtle, Screen
import random
the_turtle =Turtle()
the_turtle.speed("fastest")
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    the_turtle.color(R, G, B)

for i in range(int(360/5)):
    change_color()
    the_turtle.circle(100)
    the_turtle.left(5)

screen=Screen()
screen.exitonclick()