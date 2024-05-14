from turtle import Turtle ,Screen
import random


screen=Screen()
# taking bet from the user
# text-input used to take input from the user
user_input=screen.textinput(title="Make your bet !",prompt="Which Turtle win the race? Enter a color:  ")
color=['red','green','yellow','blue','orange','purple']

# store Y positions where each turtle start their race
y_positions=[-70,-40,-10,20,50,80]

# print user input
print(user_input)

# here we declare the size of our screen
screen.setup(width=500,height=400)

# store all the turtle which is created by the for loop , one by one
all_turtle=[]

# creating for loop to make 6 turtles
for Y_position in range( 0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    # timmy.shape('turtle')
    # declare different positions to each turtle that we store in Y_positions list
    new_turtle.goto(x=-230,y=y_positions[Y_position])
    # give different color to each turtle
    new_turtle.color(color[Y_position])
    # last add all creating turtles one by one to the all_turles list
    all_turtle.append(new_turtle)

# checks if user enter something or not
if user_input:
    is_race=True

while is_race:
    for turtles in all_turtle:
        # set limit to the length of race track 
        # if any turtle reach 230 of x-axis then race stop
        if turtles.xcor()>  230:
            is_race=False
            # here we get the each turtle color
            winning_turtle=turtles.pencolor()
            # check the user input equal to wining turtle then print the turtle name and stop the program
            if winning_turtle==user_input:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost ! The {winning_turtle} is the winner!")

        # rand int is used to assign different values to each turtle to cover different distance each time the loop run
        rand_distance=random.randint(0,10)
        # here the each turtle moves forward
        turtles.forward(rand_distance)
    


screen.exitonclick()


