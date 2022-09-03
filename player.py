from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.color('white')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def to_start(self):
        self.goto(x=-350, y=self.ycor())
        self.goto(x=self.xcor(), y=-220)
        self.goto(STARTING_POSITION)
