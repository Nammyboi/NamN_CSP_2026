import turtle as trtl
import random as rand
import tkinter as tk
from tkinter import messagebox

########### Varibles

grid = 4
tile = grid * grid
windcash = "windcash.txt"
Nams_advantage = 0.99 



wn = trtl.Screen()
wn.title("Wind Bet")

wind_logo = ("namcsp/Wind.gif")

wn.addshape(wind_logo)

######## Draw Wind bet logo
wpainter = trtl.Turtle()
wpainter.speed(0)
wpainter.shape(wind_logo)
wpainter.penup()
wpainter.hideturtle()
wpainter.goto(0, 250)
wpainter.stamp()
########

######## draw grid

gridpainter = trtl.Turtle()
gridpainter.speed(0)
gridpainter.penup()
gridpainter.hideturtle()



    
    









######## Defintions

#def multiplier():



    














wn.mainloop()