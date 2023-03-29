from turtle import Turtle, Screen
my=Turtle(shape="turtle")
dis=20
def fd():
    global dis
    my.fd(dis)
    dis+=20

Screen=Screen()
Screen.listen()
Screen.onkey(fd(),"up")
Screen.exitonclick()


