"""US STATES GUESSING GAME"""

import turtle
import pandas
from tkinter import messagebox


screen = turtle.Screen()
screen.title("US-STATES-GUESSING-GAME by:Deeba Adithya")

# DECLARING THE GIF FILE NAME.
file_name = "states_img.gif"

# Declaring the shape of screen and turtle as same. And the Gif file was Declared.
screen.addshape(file_name)
turtle.shape(file_name)


# Function which Creates Turtles That was used as name of states in specified locations.
class Creator():
    def __init__(self):
        self.val = turtle.Turtle()

    def turt_creat(self):
        return self.val


# reading and storing the states names into the variable file.
file = pandas.read_csv("50_us_states.csv")


# List which Stores the states names
state_list = [i for i in file["state"]]


# storing the length of the X row into xl variable.
xl = len(file['x'])

# turts used to store all turtles which is used as states.
turts = []

# list which play part of storing finded states into it.
finded_cities = []

for i in range(xl):

    # obtain input from user

    city = screen.textinput(title="States in US", prompt=f"SCORE : {len(finded_cities)}\nGuess Another State Name")
    cap_city = city.title()

    # condition checks whether the given input is within state_list or already found.
    if (cap_city not in state_list) or (cap_city in finded_cities):
        # displays game over .
        messagebox.showinfo(title="Guessing Game", message=f"SCORE : {len(finded_cities)}\nGame Over")
        # bye used to close the turtle.
        turtle.bye()
        break
    finded_cities.append(cap_city)
    # the x and y values can be found using its city name as reference by loc().
    x_loc = file.loc[file['state'] == cap_city, 'x']
    x_position = int(x_loc.iloc[0])
    y_loc = file.loc[file['state'] == cap_city, 'y']
    y_position = int(y_loc.iloc[0])
    x = (x_position, y_position)

    # Creator class which creates turtle and stores into turt variable.
    turt = Creator().turt_creat()
    turt.penup()
    turt.goto(x)

    # To hide the turtle while displaying the name of the state
    turt.hideturtle()
    turts.append(turt)
    turt.write(cap_city)
# Keeps the screen unclosed even whle clicking with turtle screen.
if i >=49:
    messagebox.showinfo(title="Guessing Game", message=f"SCORE : {len(finded_cities)}\nYOU WON!")
    turtle.bye()
screen.mainloop()