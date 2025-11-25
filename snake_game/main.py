from turtle import Screen
from snake_class import Snake
from snake_food import Food
from snake_score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#0f0f0f")
screen.title("MK Snake Game")
screen.tracer(0)

snake = Snake()
snake_food = Food()
snake_score = Scoreboard() 

screen.listen()

screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_moving()
    # for s_len_num in snake_length:
    #     s_len_num.forward(50)

    #Detect collosion with food
    if snake.head.distance(snake_food) < 15:
        snake_food.change_food_location()
        snake.increase_length()
        snake_score.increase_score()

    #Detect collosion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        snake_score.game_over()

    #Detect collosion with wall
    for length in snake.snake_length[1:]:
        
        if snake.head.distance(length) < 10:
            game_is_on = False
            snake_score.game_over()
        

    


screen.exitonclick()