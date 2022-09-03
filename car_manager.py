from player import Player
from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 2.5
MAX = 20
COLLIDER = 22


class CarManager:

    def __init__(self):
        self.car_list = []
        self.level = 0
        self.max = MAX
        for i in range(self.max):
            car = Turtle(shape='square')
            car.shapesize(stretch_wid=1, stretch_len=1.5)
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(x=randint(320, 1000), y=randint(-250, 250))
            self.car_list.append(car)
        self.car_list = tuple(self.car_list)

    def move_cars(self):

        for i in self.car_list:
            i.forward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*self.level)
            if i.xcor() < -320:
                i.goto(x=300, y=randint(-250, 250))

    def increase_level(self):
        self.level += 1

    def collision(self, player: Player):
        for i in self.car_list:
            if i.distance(player) < COLLIDER:
                return True
        return False
