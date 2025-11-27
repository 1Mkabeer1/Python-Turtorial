from turtle import Screen
import time
from player import Player
from car import Car_management
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.tracer(0)

player = Player()
car_manager = Car_management()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    #Detect collision with car
    for car in car_manager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect succefull crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        
        scoreboard.increase_level()

screen.exitonclick()