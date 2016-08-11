from turtle import *
from pygame import *
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

#import map to dictionary map
map = {}
for i in range(1, 19):
    map["map"+str(i)] = "maps/map_"+str(i)+".gif"

#import monster image to dictionary monster
monsters = {}
monsters["Arch Demon Scepter"] = "monsters\Arch Demon Scepter.gif"
monsters["Balrog"] = "monsters\Balrog.gif"
monsters["Cyclops"] = "monsters\Cyclops.gif"
monsters["Float Eye"] = "monsters\Float Eye.gif"
monsters["Gargoyle"] = "monsters\Gargoyle.gif"
monsters["Greater Demon Silver"] = "monsters\Greater Demon Silver.gif"
monsters["Green Slime"] = "monsters\Green Slime.gif"
monsters["Hag"] = "monsters\Hag.gif"
monsters["Mad Taus Revenge"] = "monsters\Mad Taus Revenge.gif"
monsters["Mad Taus Revenge2"] = "monsters\Mad Taus Revenge2.gif"
monsters["Mad Taus"] = "monsters\Mad Taus.gif"
monsters["Minotaur"] = "monsters\Minotaur.gif"
monsters["Skeleton"] = "monsters\Skeleton.gif"
monsters["Treant"] = "monsters\Treant.gif"
monsters["Water Holger"] = "monsters\Water Holger.gif"
monsters["Winter Wolf"] = "monsters\Winter Wolf.gif"
monsters["Zombie"] = "monsters\Zombie.gif"


# these defs control the movement of our "turtle"
def move_up():
    if position_report()[1] > 2:
        seth(90)
        forward(move_speed)

def move_down():
    if position_report()[1] < 17:
        seth(270)
        forward(move_speed)

def move_left():
    if position_report()[0] > 2:
        seth(180)
        forward(move_speed)

def move_right():
    if position_report()[0] < 23:
        seth(0)
        forward(move_speed)

def player_move(player_x, player_y):
    goto(int(player_x * 20 - 250), int(190 - player_y * 20))

def position_report():
    return (int((pos()[0] + 250) / 20), int((190-pos()[1]) / 20))

#define the write function
def print_string(string, size, color, x, y):
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
start_point = (1, 1)

player_move(8, 10)

# associate the defs from above with certain keyboard events
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

#before start


#game start menu
bgpic(map["map1"])
shape(player_image)



#start game



#load



#help



#about





mainloop()

