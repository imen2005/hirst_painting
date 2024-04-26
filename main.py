#import colorgram

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #rgb_colors.append((r,g,b))

#print(rgb_colors)
import turtle
import random
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.sety(-225)
for _ in range(10):
    ycor = my_turtle.ycor()
    my_turtle.setx(-225)
    for _ in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)
    my_turtle.sety(ycor + 50)

my_screen = turtle.Screen()
my_screen.exitonclick()