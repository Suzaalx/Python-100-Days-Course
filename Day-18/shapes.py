from turtle import Turtle, Screen

shapes=Turtle()
# length=200
# Traingle=360/3
# Square=360/4
# Pentagon=360/5
# Hexagon=360/6
# Heptagon=360/7
# Octagon=360/8
# Nonagon=360/9
# Decagon=360/10

# def traingle():
#     for i in range(3):
#         shapes.forward(length)
#         shapes.right(Traingle)
# def square():
#     for i in range(4):
#         shapes.forward(length)
#         shapes.right(Square)   

# def pentagon():
#     for i in range(5):
#         shapes.forward(length)
#         shapes.right(Pentagon)
        
# def hexagon():
#     for i in range(6):
#         shapes.forward(length)
#         shapes.right(Hexagon)
# def heptagon():
#     for i in range(7):
#         shapes.forward(length)
#         shapes.right(Heptagon)
# def octagon():
#     for i in range(8):
#         shapes.forward(length)
#         shapes.right(Octagon)
# def nonagon():
#     for i in range(9):
#         shapes.forward(length)
#         shapes.right(Nonagon)
# def decagon():
#     for i in range(10):
#         shapes.forward(length)
#         shapes.right(Decagon)
        
# traingle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

def shape(sides):
    angle=360/sides
    for i in range(sides):
        shapes.forward(100)
        shapes.right(angle)
for i in range(3,11):
    
    shape(i)
screen=Screen()
screen.exitonclick()