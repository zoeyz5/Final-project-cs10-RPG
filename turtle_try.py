import turtle

#windows settings
screen = turtle.Screen()
turtle.setup(width=480, height=360)
screen.bgcolor("black")
turtle.title("Simple RPG for CS10 final by group 7")

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
    turtle.seth(90)
    turtle.forward(move_speed)

def move_down():
    turtle.seth(270)
    turtle.forward(move_speed)

def move_left():
    turtle.seth(180)
    turtle.forward(move_speed)

def move_right():
    turtle.seth(0)
    turtle.forward(move_speed)

#define the write function
def write(string, size, color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.write(string, font=('04b_21', size, "normal"))
    turtle.penup()

#turtle shape settings
screen.addshape(player_image)


turtle.penup()
turtle.speed(0)
turtle.home()

move_speed = 20
turn_speed = 90
start_point = (10, 10)

turtle.goto(start_point)

# associate the defs from above with certain keyboard events
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

#before start


#game start menu
turtle.bgpic(start_screen)


#start game



#load



#help



#about





turtle.mainloop()

