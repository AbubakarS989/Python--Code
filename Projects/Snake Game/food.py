from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.Refresh()
        
    def Refresh(self):

        # creating random x and y coordinates values where our dot print each second 
        # on different places 
        ran_x=random.randint( -280,280  )
        ran_y=random.randint( -280,280  )
        self.goto(ran_x,ran_y)

