import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title='Guess the state', prompt = "What's another state name?")
print(answer_state)

#read data from csv
data = pd.read_csv('50_states.csv')

#create a state list
state_list = data['state'].to_list()
print(state_list)






#get states coordinates from map
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()
