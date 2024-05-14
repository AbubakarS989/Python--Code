from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # score for paddles
        self.L_score=0
        self.R_score=0
        self.Update_ScoreBoard()


    def Update_ScoreBoard(self):
        self.clear()
        self.goto( -100,200)
        self.write(self.L_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.R_score,align="center",font=("Courier",80,"normal"))

    # add +1 point when the right paddle misses the ball
    # give that +1 point to the left paddle 
    def L_point(self):
        self.L_score+=1
        self.Update_ScoreBoard()

    def R_point(self):
        self.R_score+=1
        self.Update_ScoreBoard()
