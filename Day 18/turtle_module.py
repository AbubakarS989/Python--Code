from turtle import Turtle ,Screen


#Assign turtle name
# QS:1 Draw a square
# tim=Turtle()
# # tim.shape("turtle")  
# # Now we will perform something with turtle
# tim.color('red')
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# QS:2 Draw a dash line

line=Turtle()
# line.left(90)
# # line.shape("turtle")  
# for _ in range(100):
#     line.forward(10)
#     line.color('black')
#     line.forward(10)
#     line.color('white')

# line.color('black')
def  dash_line(line):
    for _ in range(10):
        line.forward(10)
        # line.color('blue')
        line.penup()
        line.forward(10)
        line.pendown()
        # line.color('red')

dash_line(line)
line.right(90)
dash_line(line)
line.right(90)
dash_line(line)
line.right(90)
dash_line(line)




# display scree and stop it until we click
screen=Screen()
screen.exitonclick()
# print(timmy_turtle)