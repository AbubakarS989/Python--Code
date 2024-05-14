from turtle import Turtle

# positions of three points  where they get start on the screen
Starting_Positions = [(0, 0), (-20, 0), (-40, 0)]

# list used to store each square which is created in a second
segments = []
# distance cover by snake in each instant
Move_distance = 20
# declare x and y coordinate  which is used for change the direction of head of snake
Left = 180
Right = 0
Up = 90
Down = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        # loop for creating square and set point where they get start on each second
        for positions in Starting_Positions:
            self.add_segments(positions)

    def add_segments(self,position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        # penup for hide the line while creating each square
        snake.penup()
        # set position to where each square  start to move forward
        snake.goto(position)
        # now append each square to the segments list
        self.segments.append(snake)

    def Extend(self):
        # add one square when snake eat:
        self.add_segments(self.segments[-1].position())

    # Reset is used ,when snake cross limit or eat owns body then the body of snake become reset where the initial game start 
    def reset(self):
        # we just change their x y positions and clear all snakes after this
        for seg in self.segments:
            seg.goto(1000,100)
        # after clear we create new snake with new goto x y position
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def move(self):
        # for change the direction and coordinates of each square at each instant 
        # if snake move right ,if it move up then the 2,3 square also change own directions towards the directions of first square
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # change direction according to last square 
            # second to last
            new_x = self.segments[seg_num - 1].xcor()
            # first to last
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(Move_distance)

    # define the headings of snake if head towards right then they can't move left or also for up and down vice versa

    # for up direction
    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    # for down direction
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    # for left direction
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    # for right direction
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

