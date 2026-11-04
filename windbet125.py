import turtle as trtl
import random as rand
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os

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
###### Pretty self explantory no need for comments in this section

def get_multiplier():
    return round((16 / (16 - safe)) * Nams_advantage, 2)

def load_shape(filename):
    if os.path.exists(filename):
        wn.addshape(filename)
        return filename
    return "square"

def click_tile(index):
    global safe, playing
    if not playing:
        return
    if tiles[index]["clicked"]:
        return
    tiles[index]["clicked"] = True
    if index == bomb:
        #print("BOOM! You lost your bet!")
        playing = False
        tiles[index]["turtle"].shape(Bomb_shape)
        earnings_writer.clear()
        save_account()
    else:
        safe += 1
        tiles[index]["turtle"].shape(Diamond_shape)
        #print("Safe tiles:", safe)
        #print("Multiplier:", get_multiplier())
        if safe == 15:
            cash_out()
        else:
            update_earnings()
    wn.update()

def load_account():
    global player, cash
    player = simpledialog.askstring("Wind Bet", "Enter your name, use _ for spaces okay?:")
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
    bet = simpledialog.askfloat("Wind Bet", "How much can you afford to lose?")
    if bet is None:
        return
    if bet <= 0 or bet > cash:
        messagebox.showerror("Wind Bet", "Stop trying to bet what you don't have you chump!")
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
    earnings_writer.clear()
    update_earnings()
    wn.update()

def cash_out():
    global cash, playing
    if playing and safe > 0:
        winnings = round(bet * get_multiplier(), 2)
        cash += winnings
        playing = False
        earnings_writer.clear()
        save_account()
        update_balance()
        messagebox.showinfo("Wind Bet", "You got $" + str(winnings) + "!")

def update_balance():
    balance_writer.clear()
    balance_writer.write("Balance: $" + str(round(cash, 2)))
    wn.update()

def update_earnings():
    earnings_writer.clear()
    if playing:
        winnings = bet * get_multiplier()
        earnings_writer.write("Earnings: $" + str(round(winnings, 2)))
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
        leaderboard_writer.write("TOP TIER GAMBLERS", font=("Arial", 18, "bold"))
        ranking = 0
        for i in range(len(players)):
            if players[i][0] == player:
                ranking = i + 1
        for i in range(min(5, len(players))):
            leaderboard_writer.goto(-140, 80 - i * 35)
            leaderboard_writer.write(str(i + 1) + ". " + players[i][0] + " $" + str(round(players[i][1], 2)),font=("Arial", 14, "normal"))
        leaderboard_writer.goto(-140, -110)
        leaderboard_writer.write("Your Current Ranking: #" + str(ranking), font=("Arial", 16, "bold"))
    else:
        leaderboard_open = False
        leaderboard_writer.clear()
        bg_writer.clear()
    wn.update()

def reset_game():
    global playing, safe, bet
    playing = False
    safe = 0
    bet = 0
    leaderboard_writer.clear()
    bg_writer.clear()
    earnings_writer.clear()
    load_account()
    update_balance()
    for i in range(16):
        tiles[i]["clicked"] = False
        tiles[i]["turtle"].shape(hidden_shapes[rand.randint(0, 2)])
    wn.update()

def troll():
    messagebox.showinfo("Wind Bet", "😂 thx for donating to nam's hong kong buffet fund")
    global cash
    cash = 0
    save_account()
    update_balance()

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
Iwriter.goto(-240, 200)
Iwriter.color("salmon")
Iwriter.write("Press 's' to start a new game\nPress 'c' to cash out your winnings\nPress 'L' to view the leaderboard\nPress 'r' to reset the game\nPress 'z' to convert to real money", align="left", font=("Arial", 6, "bold"))

###########Current earnings writer
earnings_writer = trtl.Turtle()
earnings_writer.hideturtle()
earnings_writer.penup()
earnings_writer.goto(-240, 180)
earnings_writer.color("black")

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
wn.onkey(reset_game, "r")
wn.onkey(troll, "z")

wn.mainloop()


#p.playsound()