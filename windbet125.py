import turtle as trtl
import random as rand
import tkinter as tk
from tkinter import messagebox
import os
import playsound3 as ps

########### Varibles
os.chdir(os.path.dirname(os.path.abspath(__file__))) #makes the gifs work in any folder


grid = 4
tile = grid * grid
windcash = "windcash.txt"
Nams_advantage = 0.99 
bomb = rand.randint(0, 15)
tiles = []
safe = 0
playing = True


wn = trtl.Screen()
wn.title("Wind Bet")
wn.setup(width=500, height=500)



######## Defintions

def get_multiplier():
    return round(16 / (16 - safe), 2)


def load_shape(filename):
    if os.path.exists(filename):
        wn.addshape(filename)
        return filename
    return "square"

def click_tile(index):

    global safe, playing, cash

    if not playing:
        return

    if index == bomb:
        print("BOOM! You lost everything!")
        cash = 0
        playing = False

    else:
        safe += 1

        print("DIAMOND!")
        print("Safe tiles:", safe)
        print("Multiplier:", get_multiplier())


#def check_tile():



wind_logo = ("Wind.gif")
wind_bg = ("windbg.gif")
hidden_shapes = [load_shape("tile1.gif"), load_shape("tile2.gif"), load_shape("tile3.gif")]



wn.addshape(wind_logo)

####### Draw background
#bgpainter= trtl.Turtle()

wn.bgpic("windbg.gif")



######## Draw Wind bet logo
wpainter = trtl.Turtle()
wpainter.speed(0)
wpainter.shape(wind_logo)
wpainter.penup()
wpainter.hideturtle()
wpainter.goto(0, 210)
wpainter.stamp()
########

######## draw grid

for i in range(16):
    row = i // 4
    col = i % 4

    tile = trtl.Turtle()
    tile.shape(hidden_shapes[rand.randint(0, 2)])  # randomly choose one of the three hidden shapes
    tile.shapesize(3.5, 3.5)           # change size of tile
    tile.color("gray")
    tile.penup()
    tile.goto(-135 + col * 90, 125 - row * 90)

    tile.onclick(lambda x, y, i=i: click_tile(i))
    tiles.append(tile)


wn.mainloop()


#p.playsound()