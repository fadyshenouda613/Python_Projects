import turtle
import pandas
# Creating Screen With Image Filling it.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Creating the turtle that is going to write city names.
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# reading CSV file
data = pandas.read_csv("50_states.csv")

# Creating a list of all states from the CSV
all_states = data.state.to_list()

guessed_states = []

# Checking the answer if it is a valid answer
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's a state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)

screen.exitonclick()
