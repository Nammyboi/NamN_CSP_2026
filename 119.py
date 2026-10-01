# Nam's summative
battery = 100
import turtle as trtl
import random
from tkinter import messagebox
wn=trtl.Screen()
wn.setup(width=1000, height=800)
wn.title("Nam's TV")
painter = trtl.Turtle()
ground_painter = trtl.Turtle()
ground_painter.hideturtle()
ground_painter.penup()
battery_painter = trtl.Turtle()
battery_painter.hideturtle()
battery_painter.penup()
####################

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
    "midnightblue", "springgreen", "steelblue", "wheat"]

ground_colors = ["green", "darkgreen", "forestgreen", "limegreen", "seagreen",
    "olive", "olivedrab", "yellowgreen", "brown", "saddlebrown",
    "sienna", "chocolate", "peru", "tan", "burlywood",
    "darkgoldenrod", "goldenrod", "khaki", "wheat", "beige"]

######## Alien

custom_man = (
    (-5, 10), (5, 10),
    (7, 7), (5, 5),
    (5, 0), (10, -5),
    (5, -5), (2, 0),
    (2, -10), (7, -15),
    (2, -12), (0, -5),
    (-2, -12), (-7, -15),
    (-2, -10), (-2, 0),
    (-5, -5), (-10, -5),
    (-5, 0), (-5, 5),
    (-7, 7)
)
wn.register_shape("stickman", custom_man)


###############
#### Car

custom_car = (
    (-20, -8), (20, -8),
    (20, 5), (12, 5),
    (7, 12), (-7, 12),
    (-12, 5), (-20, 5)
)

wn.register_shape("car", custom_car)


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
    91, 92, 93, 94, 95, 96,"stickman", "car", "stickman", "car", "stickman", "car", "stickman", "car", "stickman", "car", "stickman", "car"]

shape_colors = ["red", "blue", "green", "yellow",
    "orange", "purple", "pink", "cyan",
    "magenta", "lime", "gold", "white"]


########################
##### Battery
def draw_battery():
    battery_painter.clear()

    battery_painter.goto(300, 330)
    battery_painter.color("black")
    battery_painter.write( "Battery: " + str(battery) + "%",)
        
    
########## Clicking  ########


def ground():
    global ground_colors
    ground_color = random.choice(ground_colors)
    ground_painter.color(ground_color)
    ground_painter.goto(-470,-140)
    ground_painter.setheading(0)
    ground_painter.begin_fill()
    ground_painter.pendown()
    for i in range(2):
        ground_painter.forward(900)
        ground_painter.left(90)
        ground_painter.forward(100)
        ground_painter.left(90)
    ground_painter.end_fill()
    ground_painter.penup()




def fun(x,y):
    global battery

    if battery <=0:
        messagebox.showinfo("TV no longer works")
        return
    battery = battery - random.randint(1,10)

    draw_battery()

    painter.hideturtle()
    painter.penup()
    wn.tracer(0)
    painter.goto(-470, 310)
    color = random.choice(bg_colors)
    painter.color(color)
    painter.begin_fill()
    painter.pendown()

    for i in range(2):
        painter.forward(900)
        painter.right(90)
        painter.forward(450)
        painter.right(90)
    
    painter.end_fill()
    painter.penup()
    ground()
 ################## Random shapes
    
    for i in range(10):
        painter.penup()
        shape = random.choice(shape_list)  

        x = random.randint(-275, 375)
        y = random.randint(-125, 175)

        painter.goto(x, y)
        painter.begin_fill()
        painter.pendown()
        painter.color(random.choice(shape_colors))
        if isinstance(shape, int):
            painter.circle(50, 360, shape)
            painter.end_fill()
        else:
            painter.shape(shape)
            painter.stamp()
    wn.update()
    
#####################

###########################################

########## TV ########




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

fun(0,0)
wn.update()

wn.mainloop()