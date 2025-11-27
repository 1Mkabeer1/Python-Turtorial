from turtle import Screen
from players import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#0f0f0f")
screen.title("Pond Game")
screen.tracer(0)

player_one = Player((-370, 0))
player_two = Player((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_one.go_up, 'Up')
screen.onkey(player_one.go_down, 'Down')
screen.onkey(player_two.go_up, 'w')
screen.onkey(player_two.go_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
#detect collision with player
    if ball.distance(player_two) < 50 and ball.xcor() > 350 or ball.distance(player_one) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    

#detect player 0ne misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_1_point()

#detect player two misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player_2_point()



screen.exitonclick()