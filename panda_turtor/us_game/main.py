import pandas
import turtle

# Screen settings
screen = turtle.Screen()
# screen.setup(width=725, height=491)
screen.title("Us States Game")
image = "img.gif"
screen.register_shape(image)

my_turtle = turtle.Turtle()
my_turtle.shape(image)

data = pandas.read_csv("states.csv")
all_state = data.state.to_list()


correct_answered = []


# print(user_answer)
# print(all_state)

while len(correct_answered) < 50:
    user_answer = screen.textinput(title=f"{len(correct_answered)}/50 States Correct", prompt="What's another state's name?")
    user_answer = user_answer.title()

    if user_answer == "Exit":
        missing_state = []
        for state in all_state:
            if state not in correct_answered:
                missing_state.append(state)
        new_data = pandas.DataFrame.from_dict(missing_state)
        new_data.to_csv("user_report.csv")       
        break
    if user_answer in all_state:
        correct_answered.append(user_answer)
        new_write = turtle.Turtle()
        new_write.penup()
        new_write.hideturtle()
        state_data = data[data.state == user_answer]
        x = int(state_data.x)
        y = int(state_data.y)
        # print(f'{x} - {y}')
        new_write.goto(x, y)
        new_write.write(user_answer)
   


# screen.exitonclick()