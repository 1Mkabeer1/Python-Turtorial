from turtle import Screen
import turtle as t
import random
my_turtle = t.Turtle()
t.colormode(255)

def colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

print(colours())

# my_turtle.shape('turtle')
# my_turtle.color('green')
# colors = ['blue', 'yellow', 'green', 'red', 'indigo', 'purple','pink', 'DeepSkyBlue', 'grey', 'black', 'brown']
direction = [0, 90, 180, 270]
# my_turtle.pensize(10)
my_turtle.speed(0)

#Random shapes project
# def shape_draw(shape_num):
#     angle = 360/shape_num
#     for i in range(shape_num):
#         my_turtle.forward(100)
#         my_turtle.right(-angle)

# for i in range(3,10):
#     shape_draw(i)


# random line generator with different colors
# for i in range(90):
#     my_turtle.color(colours())
#     my_turtle.forward(40)
#     my_turtle.setheading(random.choice(direction))



def spiral_shape(shape_size):
    num_rounds = int(360/shape_size)
    print(num_rounds)
    for i in range(num_rounds):
        my_turtle.color(colours())
        my_turtle.circle(100)
        current_heading = my_turtle.heading()
        my_turtle.setheading(current_heading + shape_size)

# number = int(input("Enter a Number ?"))
spiral_shape(5)











my_screen = Screen()
my_screen.exitonclick()