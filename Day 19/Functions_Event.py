# Using screen events
# listen()
# onkey() | onkeyrelease()
# onkeypress()
# onclick() | onscreenclick()
# ontimer()
# mainloop() | done() 
# Settings and special methods

from turtle import Turtle ,Screen


#  make an object
tim=Turtle()
screen=Screen()
def move_back():
    tim.backward(10)


def move_forward():
    tim.forward(10)


def move_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)


def move_right():
    tim.right(10)
    # tim.color("red")
    # tim.circle(40)

def clear_Screen():
   tim.clear()
   tim.penup()
   tim.home()
   tim.pendown()

# hold the screen until  to listen the event 
screen.listen()
# Now create an event that a cmp execute 
# its take an function and a separated and key
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_back,key="s")
screen.onkey(fun=move_left,key="a")
screen.onkey(fun=move_right,key="d")
screen.onkey(fun=clear_Screen,key="c")

screen.exitonclick()


