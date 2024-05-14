from turtle import Turtle,Screen


line=Turtle()



# Side design 1
# shape1
line.color("red")
def draw_shape(side):
    angle=360/side
    for _ in range(side):
        line.forward(100)
        line.right(angle)

def shape_side():
    for shape in range(3,11):
        draw_shape(shape)

# line.left(120)
line.speed(120)
shape_side()
line.left(120)
shape_side()
# line.speed(1)
line.left(127)
shape_side()
# display
screen=Screen()
screen.exitonclick()