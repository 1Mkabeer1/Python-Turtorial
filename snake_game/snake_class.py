from turtle import Screen, Turtle
import time

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def create_snake(self):
        for snake_position in STARTING_POSITION:
            self.create_snake_length(snake_position)
        # print(self.snake_length)

    def create_snake_length(self, snake_position):
        snake_body = Turtle('square')
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(snake_position)
        self.snake_length.append(snake_body)

    def increase_length(self):
        position = self.snake_length[-1].position()
        print(position)
        self.create_snake_length(position)

    def start_moving(self):
        for sn_len_num in range(len(self.snake_length)-1, 0, -1):  
            new_x = self.snake_length[sn_len_num-1].xcor()
            new_y = self.snake_length[sn_len_num-1].ycor()
            self.snake_length[sn_len_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
       if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)         