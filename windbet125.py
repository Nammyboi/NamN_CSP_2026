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
player = ""
cash = 1000
bet = 0
leaderboard_open = False

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
        tiles[index]["turtle"].shape(Bomb_shape) #makes bomb appear
    else:
        safe += 1
        print("DIAMOND!")
        print("Safe tiles:", safe)
        print("Multiplier:", get_multiplier())
        tiles[index]["turtle"].shape(Diamond_shape)
    wn.update()

def load_account():
    global player, cash
    player = simpledialog.askstring("Wind Bet", "Enter your name:")
    if player == None or player == "":
        player = "Player"
    cash = 100
    file = open("windcash.txt", "a")
    file.close()
    file = open("windcash.txt", "r")
    for line in file:
        data = line.split()
        if len(data) == 2 and data[0] == player:
            cash = float(data[1])
    file.close()

def save_account():
    file = open("windcash.txt", "r")
    lines = file.readlines()
    file.close()
    found = False
    file = open("windcash.txt", "w")
    for line in lines:
        data = line.split()
        if len(data) == 2 and data[0] == player:
            file.write(player + " " + str(cash) + "\n")
            found = True
        else:
            file.write(line)
    if found == False:
        file.write(player + " " + str(cash) + "\n")
    file.close()

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
    save_account()
    update_balance()
    wn.update()

def cash_out():
    global cash, playing
    if playing and safe > 0:
        winnings = round(bet * get_multiplier(), 2)
        cash += winnings
        playing = False
        messagebox.showinfo("Wind Bet", "You won $" + str(winnings) + "!")
        save_account()
        update_balance()

def update_balance():
    balance_writer.clear()
    balance_writer.write("Balance: $" + str(round(cash, 2)))
    wn.update()

def show_leaderboard():
    global leaderboard_open
    leaderboard_writer.clear()
    bg_writer.clear()
    if leaderboard_open == False:
        leaderboard_open = True
        bg_writer.goto(-200, 180)
        bg_writer.color("black")
        bg_writer.begin_fill()
        for i in range(2):
            bg_writer.forward(400)
            bg_writer.right(90)
            bg_writer.forward(360)
            bg_writer.right(90)
        bg_writer.end_fill()
        file = open("windcash.txt", "r")
        players = []
        for line in file:
            data = line.split()
            if len(data) == 2:
                players.append([data[0], float(data[1])])
        file.close()
        players.sort(key=lambda x: x[1], reverse=True)
        leaderboard_writer.color("white")
        leaderboard_writer.goto(-140, 130)
        leaderboard_writer.write("WIND BET LEADERBOARD", font=("Arial", 18, "bold"))
        ranking = 0
        for i in range(len(players)):
            if players[i][0] == player:
                ranking = i + 1
        for i in range(min(5, len(players))):
            leaderboard_writer.goto(-140, 80 - i * 35)
            leaderboard_writer.write(str(i + 1) + ". " + players[i][0] + " $" + str(round(players[i][1], 2)),font=("Arial", 14, "normal"))
        leaderboard_writer.goto(-140, -110)
        leaderboard_writer.write("Your Ranking: #" + str(ranking), font=("Arial", 16, "bold"))
    else:
        leaderboard_open = False
        leaderboard_writer.clear()
        bg_writer.clear()
    wn.update()

##################### Screen
wn = trtl.Screen()
wn.title("Wind Bet")
wn.setup(width=500, height=500)
wn.tracer(0)
load_account()
###### leaderboard writer
leaderboard_writer = trtl.Turtle()
leaderboard_writer.hideturtle()
leaderboard_writer.penup()
leaderboard_writer.color("white")
#######bg writer
bg_writer = trtl.Turtle()
bg_writer.hideturtle()
bg_writer.penup()
#wn.tracer(0)

###### Balance writer
balance_writer = trtl.Turtle()
balance_writer.hideturtle()
balance_writer.penup()
balance_writer.goto(130, 200)
balance_writer.color("white")
update_balance()

######## Write instructions
Iwriter = trtl.Turtle()
Iwriter.hideturtle()
Iwriter.penup()
Iwriter.goto(-240, 180)
Iwriter.color("white")
Iwriter.write("Press 's' to start a new game\nPress 'c' to cash out your winnings\nPress 'l' to view the leaderboard", align="left", font=("Arial", 6, "bold"))

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
wn.update()

wn.listen()
wn.onkey(start_game, "s")
wn.onkey(cash_out, "c")
wn.onkey(show_leaderboard, "l")


wn.mainloop()


#p.playsound()