from turtle import Turtle, Screen

the_turtle =Turtle()

for i in range(50):
    the_turtle.forward(4)
    the_turtle.pu()
    the_turtle.forward(6)
    the_turtle.pd()
    
   

screen=Screen()
screen.exitonclick()

