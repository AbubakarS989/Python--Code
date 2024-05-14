import turtle,pandas




screen=turtle.Screen()
screen.title("U.S. States Game")

# We use state name as a turtle image
# to prevent from backslash error we use "r" to convert string into raw string
# --> Loading image in turtle
pic=r"Projects\US Map Using CSV\Us_map.gif"

# display US Map on the screen
turtle.addshape(pic)
turtle.shape(pic)




data=pandas.read_csv(r"Projects\US Map Using CSV\50_states.csv")

#get the all state and convert into a list
all_states=data["state"].to_list()
print(all_states)

# list to store user guess state points
points=[]


#first check if user state is present in 50 state or not
    # if true then we convert the name into turtle and place into x,y position
while (len(points)<50):

    # Taking cities name from the user
    text_input=screen.textinput(title=f"{len(points)}/50 out of States Correct ",prompt="Enter a state name:").title()
    # get that row which user has input the name
    user_value=data[data.state==text_input]

    # if user write exit then what happens?
    if text_input.lower()=="exit":
        # new list for remaining states
        remaining_state =[state  for state in all_states if state not in points ]
        print(len(points))
        # Store the remaining states into the New CSV files

        new_data=pandas.DataFrame(remaining_state)
        new_data.to_csv(r"Projects\US Map Using CSV\Remaining_states.csv")
        break

    elif text_input in all_states :
        # increase points using append the user input
        points.append(text_input)
        # Create a turtle with shape of state name and place it where it is set.
        new_turtle=turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        # iloc method is used to extract data from row using index
        x,y=user_value.iloc[0,1],user_value.iloc[0,2]
        print(x,y)
        new_turtle.color("black")
        new_turtle.goto(x,y)
        new_turtle.write(text_input)


    






# print(data.state[23])
# print(value.x[30] , value.y[30])
# data[data.x==-43 and data.y==-128]
# def onclick(x,y):
#     print(x,y)

# # this event listener  give us the  x y coordinate value
# turtle.onscreenclick(onclick)


# hold the screen until we shut the window
# turtle.mainloop()
# screen.exitonclick()


