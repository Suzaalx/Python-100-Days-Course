from turtle import Turtle, Screen
sketch=Turtle()
sketch.speed("fastest")
def f():
    sketch.fd(10)
def b():
    sketch.backward(10)
def c():
    sketch.left(10)
    sketch.fd(10)
def cc():
    sketch.right(10)
    sketch.fd(10)
def clear():
    sketch.clear()
    sketch.penup()
    sketch.home()
    sketch.pendown()
screen=Screen()

screen.listen()
screen.onkey(f,"w")
screen.onkey(b,"s")
screen.onkey(c,"a")
screen.onkey(cc,"d")
screen.onkey(clear,'c')
screen.exitonclick()