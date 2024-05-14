from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score_Board
# Steps to create a png game

# Create Screen 
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game - Code With Abubakar")

#  off the animation
screen.tracer(0)


# TODO Create a Paddle that responds to Key Presses
#  I create a class object of paddle to generate number of paddle
# input x and y values to place paddle where we want to

paddle_right = Paddle(350, 0)

# TODO Create another paddle for 2nd player
# do same for 2nd paddle

paddle_left = Paddle(-350, 0)


# here screen listen our keyboard buttons
screen.listen()

# Right Paddle Keys
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.  go_down, "Down")

# Left Paddle Keys
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

# TODO create the ball and move it
ball=Ball()

# TODO Keep the score up-to-date
Score_board=Score_Board()


# On the animation and update screen after instant and place the paddle right side
game_on = True
while game_on:
    # time.sleep(ball.ballSpeed)
    time.sleep(0.1)
    screen.update()
    ball.move()
# TODO Detect collision with wall and make it bounce back

#  detect y coordinates and set condition 
    if ball.ycor() > 280 or ball.ycor()<-280:
        # needs to bounce
        ball.bounce_y()

#  TODO Detect collision with both Paddle
    if ball.distance(paddle_right)<50  and ball.xcor()>310 or  ball.distance(paddle_left)<50 and  ball.xcor()<-320:
        ball.bounce_x()
        ball.speed()
        print("Collision Detects")


# TODO Detect when Right paddle missis the ball
    if  ball.xcor()>380: 
        ball.reset_position()
        Score_board.L_point()
    
# TODO Detect when Left paddle missis the ball
    if  ball.xcor()<-380: 
        ball.reset_position()
        Score_board.R_point()















screen.exitonclick()
