from turtle import Turtle, Screen
import random
Screen=Screen()
Screen.setup(width=500,height=400)
bet=Screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
race_on=False
y=-100
turtles=[]
for i in colors:
    a=Turtle(shape="turtle")
    a.color(i)
    
    a.penup()
    a.goto(x=-230,y=y)
    y+=40
    turtles.append(a)
if bet:
    race_on=True
while race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            race_on=False
            winner=turtle.pencolor()
            if winner==bet:
                print(f"you won the bet!.The {winner} is the winner.")
            else:
                print(f"Sorry! You lost the bet.The {winner} is the winner.")
            
        distance=random.randint(0,10)
        turtle.fd(distance)
    
Screen.exitonclick()
