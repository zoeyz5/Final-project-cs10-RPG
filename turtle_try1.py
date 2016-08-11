from turtle import *
import time

#windows settings
screen = Screen()
setup(width=480, height=360)
screen.bgcolor("black")
title("Simple RPG for CS10 final by group 7")

#define & import graphic files
player_image = "systems/player.gif"
start_screen = "systems/START SCREEN.gif"
game_over_screen = "systems/GAME OVER SCREEN.gif"
item = "systems/item.gif"
menu = "systems/menu.gif"
shop = "systems/SHOP.gif"
player_status = "systems/stat.gif"
selection_frame1 = "systems/selection square1.gif"
selection_frame2 = "systems/selection square2.gif"
selection_frame3 = "systems/selection square3.gif"

# these defs control the movement of our "turtle"
def move_up():
    seth(90)
    forward(move_speed)

def move_down():
    seth(270)
    forward(move_speed)

def move_left():
    seth(180)
    forward(move_speed)

def move_right():
    seth(0)
    forward(move_speed)

#define the write function
def write(string, size, color, x, y):
    penup()
    goto(x, y)
    pendown()
    pencolor(color)
    write(string, font=('04b_21', size, "normal"))
    penup()

#some function definition
def shine():
    while shine == 0:
        ht()
        time.sleep(0.5)
        st()
        time.sleep(0.5)
    ht()



#define selection square function





#turtle shape settings
screen.addshape(player_image)
screen.addshape(selection_frame1)
screen.addshape(selection_frame2)
screen.addshape(selection_frame3)


penup()
speed(0)
home()

move_speed = 20
turn_speed = 90
start_point = (10, 10)

goto(start_point)

# associate the defs from above with certain keyboard events
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

#before start


#game start menu
bgpic(start_screen)
shape(selection_frame1)
home()



#start game



#load



#help



#about





mainloop()

