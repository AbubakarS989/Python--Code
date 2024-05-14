import turtle,os
from turtle import Screen 

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

  

  
# Here we create turtle class and assign it to timmy var

# while True:
timmy=turtle.Turtle()
timmy.color('green')
print(timmy)
timmy.shape("turtle")
timmy.forward(200)
timmy.right(90)
print("Here we move right")
move=int(input("Enter move value:"))
timmy.forward(move)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)

# create timmy 2 var
timmy2=turtle.Turtle()
timmy2.color('coral')
timmy2.shape("turtle")
timmy.right(90)
timmy.forward(10)
timmy.circle(80)
timmy2.circle(130)
timmy2.forward(200)
timmy2.right(90)
timmy2.forward(200)
timmy2.color('red')
timmy2.circle(100)
timmy2.right(90)
timmy2.forward(200)

# object=attributes
my_screen=Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()
print(my_screen)