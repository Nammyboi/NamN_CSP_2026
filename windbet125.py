import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.title("Wind Bet")

wind_logo = ("namcsp/Wind.gif")

wn.addshape(wind_logo)

painter = trtl.Turtle()
painter.speed(0)
painter.shape(wind_logo)
painter.penup()
painter.hideturtle()
painter.goto(0, 250)
painter.stamp()












wn.mainloop()