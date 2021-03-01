import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title='Guess the state', prompt = "What's another state name?")

#read data from csv
data = pd.read_csv('50_states.csv')

#create a state list with all states lower case
state_list = data['state'].to_list()
state_list = [state.lower() for state in state_list]

#check if the guess is in the list and write it on the map
if answer_state.lower() in state_list:
    state_name = data[data.state == answer_state.capitalize()]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.write(answer_state.capitalize())
    t.goto(int(state_name.x), int(state_name.y))



#get states coordinates from map
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()
