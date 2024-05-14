# import turtle and screen modules
from turtle import Turtle, Screen

# import time
import time

# import Snake Class from the snake file
from snake import Snake

#  import Food from food
from food import Food
from Score_board import Score_Board

# Settings up the screen width , height and give title
screen = Screen()
foods = Food()
ScoreBoard = Score_Board()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Code With Abubakar")

# tracer is used to get instant calculation
screen.tracer(0)

#  make a snake object from the Snake file
snakes = Snake()

# Listen is used for listening the keyboard actions
screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.right, "Right")
screen.onkey(snakes.left, "Left")

# used while loop for move snake for infinite
game_on = True
while game_on:
    # update is used for update the screen after each changes by user who play game
    # if user move the snake left side this update method update that action on the screen
    screen.update()
    # decrease the execution process for a while
    # which helps us to move slow the snake
    time.sleep(0.1)
    snakes.move()

    # Collision with food
    if snakes.head.distance(foods.position()) < 15:
        foods.Refresh()
        snakes.Extend()
        ScoreBoard.Increase_score()

    # Collision with wall
    if (
        snakes.head.xcor() > 280
        or snakes.head.xcor() < -280
        or snakes.head.ycor() > 280
        or snakes.head.ycor() < -280
    ):
        ScoreBoard.reset()
        ScoreBoard.board()
        snakes.reset()    

    # Collision with tail
    for segment in snakes.segments[1:]:
        if snakes.head.distance(segment) < 10:
            ScoreBoard.reset()  
            ScoreBoard.board()
            snakes.reset()

# Read 
# with open("Projects\Snake Game\Store Score .txt",mode="r") as f:
#     print(f.read())

# # Write
# with open("Projects\Snake Game\Store Score .txt",mode="w") as f:
#     f.write("pakistan")

# #add 
# # with open("Projects\Snake Game\Store Score .txt",mode="a") as f:
# #     f.write("\npakistan")

screen.exitonclick()

