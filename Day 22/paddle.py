from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        # To change the shape size according to width and length
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        # Starting point of paddle
        self.goto(x, y)

    # use keyboard buttons to move up and down the  paddle
    # --> Paddle start
    # --> Function of each button
    #     ---> Up Key
    def go_up(self):
        # add 20 to current y-axis value
        # this only increase 20 to upward when UP key is to be pressed
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    #     ---> Down Key
    def go_down(self):
        # subtract  20 to current y-axis value
        # this only decrease 20 to downward  when Down key is to be pressed
        new_y = self.ycor() - 20    
        self.goto(self.xcor(), new_y)
    # --> Paddle end
