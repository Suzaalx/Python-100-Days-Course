from turtle import Turtle, Screen
import random
walk=Turtle()
walk.width(6)
walk.speed(0)
deg=[90,180,270,0]
direction=[0,1]
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    walk.color(R, G, B)
for i in range(500):
    change_color()
    dir=random.choice(direction)
    if dir==0:
        walk.right(random.choice(deg))
    else:
        walk.left(random.choice(deg))
    walk.forward(20)
    
    

screen=Screen()
screen.exitonclick()