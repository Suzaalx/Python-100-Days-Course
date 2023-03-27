
# import colorgram
# colors= colorgram.extract('D:\SAT\Python-100-Days-Course\Day-18\image.jpg',30)

# rgb_colors=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

colors=[(226, 231, 236), (58, 105, 148), (222, 234, 229), (225, 202, 110), (133, 85, 57), (220, 147, 74), (231, 224, 203), (143, 178, 201), (195, 145, 171), (235, 221, 231), (141, 78, 102), (212, 90, 65), (135, 181, 137), (64, 109, 91), (188, 82, 119), (151, 134, 66), (64, 157, 95), (43, 156, 190), (183, 191, 202), (216, 176, 191), (108, 121, 157), (7, 58, 104), (13, 68, 123), (156, 28, 38), (231, 174, 163), (173, 202, 183), (158, 203, 215), (174, 24, 17), (73, 57, 40), (78, 65, 46)]
import random
import turtle as turtle_module
the_turtle=turtle_module.Turtle()
turtle_module.colormode(255)
the_turtle.shape("circle")
the_turtle.speed("fastest")
the_turtle.penup()
the_turtle.hideturtle()
the_turtle.setheading(225)
the_turtle.forward(300)
the_turtle.setheading(0)
number_of_dots=100
for i in range(1,number_of_dots+1):
    
    the_turtle.dot(20,random.choice(colors))
    the_turtle.forward(50)
    if i%10==0:
        the_turtle.setheading(90)
        the_turtle.forward(50)
        the_turtle.setheading(180)
        the_turtle.forward(500)
        the_turtle.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()