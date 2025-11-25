from turtle import Screen
import turtle as t
# import random

my_turtle = t.Turtle()
my_screen = Screen()

#sketch project using turtle
def move_foward():
    my_turtle.forward(20)
def move_backward():
    my_turtle.backward(20)
def move_left():
    my_turtle.left(10)
def move_right():
    my_turtle.right(10)
def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen.listen()

my_screen.onkey(move_foward, 'w')
my_screen.onkey(move_backward, 's')
my_screen.onkey(move_left, 'a')
my_screen.onkey(move_right, 'd')
my_screen.onkey(clear, "c")




my_screen.exitonclick()