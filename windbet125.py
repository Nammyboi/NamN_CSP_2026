import turtle as trtl
import random as rand
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
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
playing = False
cash = 1000
bet = 0


##################### Screen
wn = trtl.Screen()
wn.title("Wind Bet")
wn.setup(width=500, height=500)






######## Defintions

def get_multiplier():
    return round((16 / (16 - safe)) * Nams_advantage, 2)

def load_shape(filename):
    if os.path.exists(filename):
        wn.addshape(filename)
        return filename
    return "square"

def click_tile(index):
    global safe, playing, cash
    if not playing:
        return
    # cant click same tile
    if tiles[index]["clicked"]:
        return
    tiles[index]["clicked"] = True
    if index == bomb:
        print("BOOM! You lost everything!")
        playing = False
        tiles[index]["turtle"].shape(Bomb_shape)
    else:
        safe += 1
        print("DIAMOND!")
        print("Safe tiles:", safe)
        print("Multiplier:", get_multiplier())
        tiles[index]["turtle"].shape(Diamond_shape)

def start_game():
    global bet, cash, playing, safe, bomb
    if playing:
        return
    bet = simpledialog.askfloat("Wind Bet", "How much would you like to bet?")
    if bet is None:
        return
    if bet <= 0 or bet > cash:
        messagebox.showerror("Wind Bet", "Invalid bet!")
        return
    cash -= bet
    safe = 0
    bomb = rand.randint(0, 15)
    playing = True
    for i in range(16):
        tiles[i]["clicked"] = False
        tiles[i]["turtle"].shape(hidden_shapes[rand.randint(0, 2)])
    update_balance()

def cash_out():
    global cash, playing
    if playing and safe > 0:
        winnings = round(bet * get_multiplier(), 2)
        cash += winnings
        playing = False
        messagebox.showinfo("Wind Bet",f"You won ${winnings:.2f}!\nBalance: ${cash:.2f}")
        update_balance()

def update_balance():
    balance_writer.clear()
    balance_writer.write(f"Balance: ${cash:.2f}",align="right",font=("Arial", 12, "bold"))


###### Balance writer
balance_writer = trtl.Turtle()
balance_writer.hideturtle()
balance_writer.penup()
balance_writer.goto(210, 210)
balance_writer.color("white")
update_balance()

    


################# Shapes
wind_logo = ("Wind.gif")
wind_bg = ("windbg.gif")
hidden_shapes = [load_shape("tile1.gif"), load_shape("tile2.gif"), load_shape("tile3.gif")]
Diamond_shape = load_shape("diamond.gif")
Bomb_shape = load_shape("bomb.gif")



####### Draw background
wn.addshape(wind_logo)
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
    tile.shape(hidden_shapes[rand.randint(0, 2)])
    tile.penup()
    tile.goto(-135 + col * 90, 125 - row * 90)
    tile.onclick(lambda x, y, i=i: click_tile(i))
    tiles.append({"turtle": tile,"clicked": False})


wn.listen()
wn.onkey(start_game, "s")
wn.onkey(cash_out, "c")


wn.mainloop()


#p.playsound()