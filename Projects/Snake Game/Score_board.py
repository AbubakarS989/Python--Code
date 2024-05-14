from turtle import Turtle


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("Projects\Snake Game\Store Score .txt",mode="r") as data:
            self.high_score=int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.board()
        self.hideturtle()

    def board(self):
        self.clear()    
        self.write( f"Score : {self.score} High Score : {self.high_score} ",align='center',font=("Courier",20,"normal"))

    def Increase_score(self):
        self.score+=1
        self.board()
        
    def reset(self):
        if self.score> self.high_score:
            self.high_score=self.score
            with open("Projects\Snake Game\Store Score .txt",mode="w") as data:
                data.write(f"{self.high_score}")  
        self.score=0
    

    # def game_over(self):
    #     self.clear()
    #     self.goto(-70,20)
    #     self.write(f"GAME OVER!",align='left',font=("Courier",20,"normal"))
    #     self.goto(5,-40)
    #     self.board()