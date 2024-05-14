from turtle import Turtle, Screen
import random
import time


colors = [
    "red",
    "green",
    "yellow",
    "orange",
    "brown2",
    "DarkOrchid",
    "DarkGreen",
    "maroon2",
]

# Create screen of 600 by 600 size
screen = Screen()
screen.setup(width=800, height=600)
# screen.bgcolor("White ")
screen.title("Turtle Cross Game - Code With Abubakar")

# Score Board Start Here
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.Level=1
        # hide Turtle
        self.hideturtle()
        self.penup()
        self.goto(-320,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.Level}",align="left",font=("Courier",24,"normal"))

    def increase_level(self):
        self.Level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Courier",30,"normal"))

# --> Player things start here
# Create class for better syntax
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape
        self.shape("turtle")
        self.color("red")
        self.shapesize(1.3)
        self.setheading(90)
        self.penup()
        # set the place where player start to move
        self.go_to_Start()
    # move player
    def move(self ):
        self.forward(10)

    # Detect the place of finish line
    def at_finish_line(self):
        if self.ycor()>280:
            return True
        else:
            return False
    # Move the player at starting position 
    def go_to_Start(self):
        self.goto(0, -280)



screen.tracer(0)
player = Player()
score_board=Score_Board( )
# Move the player forward when UP key is press
screen.listen()
screen.onkey(player.move, "Up")

# --> Player things End here




# Creating cars Start here
class CarsManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed=5

    def create_car(self):
        # 6 times a loop run and this reduce the cars on screen
        random_chance = random.randint(1, 6)
        # create car only when chance equal to 1
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            # give random color to each car
            new_car.color(random.choice(colors))
            # give random position to each car along right to left
            random_y = random.randint(-230, 240)
            # place where cars start to move
            new_car.goto(300, random_y)
            self.all_cars.append( new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=5

# Creating cars End here

# object of car 
carsManager = CarsManager()
game_on = True


while game_on:
    time.sleep(0.1)
    screen.update()
    carsManager.create_car()
    carsManager.move_car()

    # detect collision with cars
    for car in carsManager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score_board.game_over()

# Successful crossing
    if player.at_finish_line():
        player.go_to_Start()
        carsManager.level_up()
        score_board.increase_level()
        
screen.exitonclick()
