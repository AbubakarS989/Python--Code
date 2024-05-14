# import colorgram 
from random import Random
from turtle import Turtle,Screen
import turtle,random
# Extract colors from the images
# color_list=[]
# image_path = r"C:\Users\saab3\OneDrive\Python\Projects\Hirst Painting Project\test_pic.jpg"
# colors = colorgram.extract(image_path, 30)
# # f_color=colors[4]
# for color in color    s:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     color_list.append(new_color)

# print(color_list)
# print(len(colors))
turtle.colormode(255 )
color_pale=[(246, 244, 238), (248, 240, 245), (239, 241, 247), (237, 246, 242), (208, 151, 94), (200, 142, 173), (225, 217, 97), (113, 186, 152), (221, 59, 107), (150, 56, 105), (54, 22, 15), (145, 176, 194), (162, 21, 49), (137, 89, 57), (22, 108, 166), (17, 33, 28), (30, 15, 31), (29, 29, 60), (164, 208, 188), (151, 28, 20), (172, 182, 30), (53, 170, 100), (27, 132, 93), (17, 175, 203), (234, 159, 182), (200, 217, 7), (222, 97, 58), (168, 200, 210), (233, 173, 162), (188, 186, 208)]


line=Turtle()
line.speed('fastest')
line.penup()
line.hideturtle()
line.setheading(225)
line.forward(300)
line.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    line.dot(20,random.choice(color_pale))
    line.forward(50)    
        
        # line.left(2)
    if dot_count%10==0:
        line.setheading(90)
        line.forward(50)
        line.setheading(180)
        line.forward(500)
        line.setheading(0)  

    # line.forward(10)
    # line.setheading(990)
    # line.forward(10)
screen=Screen()
screen.exitonclick()
