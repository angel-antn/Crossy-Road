import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cont = 0

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_down, 's')
screen.onkey(player.move_right, 'd')

screen.onkey(player.move_up, 'W')
screen.onkey(player.move_left, 'A')
screen.onkey(player.move_down, 'S')
screen.onkey(player.move_right, 'D')

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    time.sleep(0.075)
    screen.update()
    if player.ycor() > 270:
        player.to_start()
        car_manager.increase_level()
        scoreboard.level_up()
    if car_manager.collision(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
