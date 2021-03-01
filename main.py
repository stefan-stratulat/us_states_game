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
answers = []



while len(answers) < 50:
    #promt for user to gues
    answer_state = screen.textinput(title=f'{len(answers)}/50 Guess the state',
                    prompt = "What's another state name?").title()
    #check if the guess is in the list and write it on the map
    if answer_state in state_list:
        answers.append(answer_state)
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
