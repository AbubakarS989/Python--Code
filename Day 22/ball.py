from turtle import Turtle

class Ball(Turtle):
    def  __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()    
        self.x_move=10
        self.y_move=10
    # speed of ball
        self.ballSpeed=0.1

    #  Move ball by increasing 10 at each refresh
    def move(self):
        new_x=self.xcor()+ self.x_move
        new_y=self.ycor()+self.y_move

        # print values to check what really happens in background
        print(f"x={new_x}")
        print(f"y={new_y}")
        # move ball to new position
        self.goto(new_x,new_y)
    
    # bounce the ball after collision with wall on +ev -ev y-axis
    def bounce_y(self):
        self.y_move *=-1  
        # self.ballSpeed*=0.9
        print(f"{self.y_move}")

    # bounce the ball after collision with wall on +ev -ev x-axis 
    def bounce_x(self):
        self.x_move *=-1  
        # self.ballSpeed*=0.9
        print(f"{self.x_move}")

    #  Reset position after  ball cross both axis  
    def reset_position(self):
        self.goto(0,0)
        self.ballSpeed=0.1
        self.bounce_x()
