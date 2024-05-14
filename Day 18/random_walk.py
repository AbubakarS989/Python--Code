from turtle import Turtle ,Screen
# from random import Random
import random

colors=["red","green","yellow","orange","brown2","DarkOrchid","DarkGreen",'maroon2']
# color=()
def random_colors():
    r=random.randint(0,200)
    g=random.randint(0,200)
    b=random.randint(0,200)
    color=(r,g,b) 
    return color 


# directions=[0,90,180,270]
walk=Turtle()
# walk.pensize(12)
# walk.speed(25)
# for _ in range(300):
#     walk.color(random.choice(colors))
#     walk.forward(50)
#     walk.setheading(random.choice(directions))

walk.speed(25)
# speed=0
# n=walk.heading()
# print(walk.setheading(n))
# for _ in range(60):
#     walk.circle(100)
#     walk.color(random.choice(colors))
#     walk.forward(20)
#     walk.setheading(walk.heading()+6)

def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        walk.circle(100)
        walk.color(random.choice(colors))
        # walk.forward(20)
        walk.setheading(walk.heading()+size_of_gap)


spirograph(10)



screen=Screen()
screen.exitonclick()