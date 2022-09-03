from turtle import Turtle
FONT = ("consolas", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color('white')
        self.write(arg=f'Level {self.level}', align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f'Level {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(x=0, y=250)
        self.write(arg='Game Over', align='center', font=FONT)
