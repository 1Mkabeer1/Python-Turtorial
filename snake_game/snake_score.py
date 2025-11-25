from turtle import Turtle
TEXT_ALIGN = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_snake_score()
    
    def update_snake_score(self):
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=TEXT_ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_snake_score()