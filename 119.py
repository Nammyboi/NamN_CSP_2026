# Nam's summative
import turtle as trtl
import random

wn=trtl.Screen()
wn.setup(width=1000, height=800)
wn.title("Nam's TV")

########## Clicking  ########

def fun(x,y):
    painter.hideturtle()
    painter.penup()
    wn.tracer(0)

    painter.goto(-470, 310)
    color = random.choice(bg_colors)
    painter.color(color)
    painter.begin_fill()
    painter.pendown()

    for i in range(2):
        painter.forward(940)
        painter.right(90)
        painter.forward(500)
        painter.right(90)

    painter.end_fill()
    painter.penup()
    wn.update()


################ Lists ############
bg_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink",
    "cyan", "magenta", "lime", "gold", "silver", "coral", "tomato",
    "salmon", "plum", "violet", "indigo", "navy", "teal", "turquoise",
    "maroon", "olive", "aqua", "brown", "tan", "beige", "khaki",
    "lavender", "orchid", "crimson", "scarlet", "chocolate", "firebrick",
    "darkred", "darkblue", "darkgreen", "darkorange", "darkviolet",
    "deeppink", "deepskyblue", "dodgerblue", "hotpink", "lightblue",
    "lightgreen", "lightpink", "lightyellow", "lightcyan", "lightgray",
    "lightcoral", "lightsalmon", "lightseagreen", "lightskyblue",
    "lightslategray", "lightsteelblue", "mediumblue", "mediumorchid",
    "mediumseagreen", "mediumslateblue", "mediumturquoise",
    "midnightblue", "springgreen", "steelblue", "wheat", "whitesmoke",
    "snow"]

ground_colors = ["green", "darkgreen", "forestgreen", "limegreen", "seagreen",
    "olive", "olivedrab", "yellowgreen", "brown", "saddlebrown",
    "sienna", "chocolate", "peru", "tan", "burlywood",
    "darkgoldenrod", "goldenrod", "khaki", "wheat", "beige"]

shape_list = [3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34,
    35, 36, 37, 38, 39, 40, 41, 42,
    43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58,
    59, 60, 61, 62, 63, 64, 65, 66,
    67, 68, 69, 70, 71, 72, 73, 74,
    75, 76, 77, 78, 79, 80, 81, 82,
    83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96,"stickman", "car", "stickman", "car"]

shape_colors = ["red", "blue", "green", "yellow",
    "orange", "purple", "pink", "cyan",
    "magenta", "lime", "gold", "white"]

###########################################

########## TV ########

painter = trtl.Turtle()
fun(0,0)
'''
painter.hideturtle()
painter.penup()
wn.tracer(0)

painter.goto(-470, 310)
painter.color("black")
painter.begin_fill()
painter.pendown()

for i in range(2):
    painter.forward(940)
    painter.right(90)
    painter.forward(500)
    painter.right(90)

painter.end_fill()
painter.penup()
wn.update()
'''
#####################

############ Remote

painter.goto(-100, -200)
painter.color("gray")
painter.begin_fill()
painter.pendown()

for i in range(4):
    painter.forward(115)
    painter.right(90)

painter.end_fill()
wn.update()

############## Button

button = trtl.Turtle()
button.penup()
button.shape("circle")
button.color("red")
button.shapesize(3)
button.goto(-46, -260)
################















wn.update()
wn.tracer(1)
button.onclick(fun)









wn.mainloop()