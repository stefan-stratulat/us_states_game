import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
#add image to the screen
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)



#read data from csv
data = pd.read_csv('50_states.csv')

state_list = data['state'].to_list()
guessed_states = []


while len(guessed_states) < 50:
    #promt for user to gues
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 Guess the state',
                    prompt = "What's another state name?").title()
    #break game is user types exit. Saves missing answers to another csv
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.csv('states_to_learn.csv')
        break
    #check if the guess is in the list and write it on the map
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_name = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_name.x), int(state_name.y))
        t.write(answer_state)





#get states coordinates from map
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()
