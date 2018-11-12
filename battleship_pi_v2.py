# ==============================================================================================
# Battleship Game for Pi VERSION 2
# Another part of my #100DaysOfCode challenge. This time I'm going to use the class
# I developed earlier to make a game in which the user, moves the cursor to their
# guessed spot and if the randomly generated ship is there, they win.
# The last version got messy and I couldn't continue my thought process on it, so 
# here is a second version with a more clean layout
# Goals for this:
# - Animation for explosion
# - Animation for moving water background
# - It to WORK
# Known Bugs:
# - 
# ==============================================================================================
# Note to me: You were working on un-rendering the cursor so that the previous colour remains

from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

# ************************
# Rework of "JoystickLed"
# Goal of new version to make cursor sepereate entity
class Cursor(object):
    x_position = 0              # Stores X position
    y_position = 0              # Stores Y position
    cursor_colour = ()          # Stores cursor colour
    middle_pressed = False      # Stores if middle button pressed

    # __init__ : Initializes values
    def __init__(self, cursor_col = (255, 255, 255), start_x = 0, start_y = 0):
        self.cursor_colour = cursor_col
        self.x_position = start_x
        self.y_position = start_y
    # draw_cursor() : Turns on the LED on the SenseHat relating to the cursor postion
    def draw_cursor(self):
        sense.set_pixel(self.x_position, self.y_position, self.cursor_colour)
    # undraw_cursor() : Turns off LED on SenseHat
    def undraw_cursor(self):
        sense.set_pixel(self.x_position, self.y_position, (0, 0, 0))
    # get_position() : Returns the cursors position
    def get_position(self):
        return [self.x_position, self.y_position]
    # selector() : Loops movement methods until middle is pressed
    def selector(self):
        while self.middle_pressed != True:
            self.movement_handler()
    # middle_button() : Handles middle button input
    def middle_button(self):
        self.middle_pressed = True
    # middle_status() : Returns middle_pressed value
    def middle_status(self):
        return self.middle_pressed

    # ************************
    # LED Move Functions
    def led_up(self):
        if self.y_position > 0:
            self.y_position -= 1
    def led_down(self):
        if self.y_position < 7:
            self.y_position += 1
    def led_left(self):
        if self.x_position > 0:
            self.x_position -= 1
    def led_right(self):
        if self.x_position < 7:
            self.x_position += 1
    # movement_handler : Handles input from the user
    def movement_handler(self):
        input = sense.stick.wait_for_event()

        if (input.action == "pressed" or input.action == "held") and input.action != "released":
            sense.clear()
            if input.direction == "up":
                self.led_up()
            elif input.direction == "down":
                self.led_down()
            elif input.direction == "left":
                self.led_left()
            elif input.direction == "right":
                self.led_right()
            else:
                self.middle_button()
        self.draw_cursor()
    # End : LED Movement
    # ************************

# ************************
# Class GridMask
# Goal: Layers a grid over the background of the game
class GridMask(object):
    #Class variables
    x_list = []
    y_list = []
    colour = (255, 0, 0)

    def __init__(self, mask_colour = (255, 0, 0)):
        self.colour = mask_colour

    def change_colour(self, mask_colour):
        self.colour = mask_colour

    def add_coordinates(self, x_coordinate, y_coordinate):
        self.x_list.append(x_coordinate)
        self.y_list.append(y_coordinate)

    def reset_mask(self):
        del self.x_list[:]
        del self.y_list[:]
        print("X, Y cleaned")

    def display_mask(self):
        if len(self.x_list) > 0:
            for x in range(0, len(self.x_list)):
                sense.set_pixel(self.x_list[x], self.y_list[x], self.colour)
        else:
            print("Nothing in GridMask: x_list")
    # End : GridMask
    # ************************

# ************************
# Class Ship
# Goal: Functioning ship entity
class Ship(object):
    #Class variables
    ship = []
    # gen_ship() : Generates a ship on an 8 x 8 grid
    def gen_ship(self):
        self.ship.append([(random.randint(0, 7)), (random.randint(0,7))])
        orientation = random.randint(0, 1)

        if orientation == 1:            # X orientation
            if self.ship[0][0] >= 6:    # Lowers the random int for Y coord by 3 to prevent ship falling off matrix
                self.ship[0][1] -= 3
            for i in range(0,2):
                self.ship.append([self.ship[i][0] + 1, self.ship[0][1]])
        else:                           # Y orientation
            if self.ship[0][1] >= 6:    # Lowers the random int for Y coord by 3 to prevent ship falling off matrix
                self.ship[0][1] -= 3
            for i in range(0, 2):
                self.ship.append([self.ship[0][0], self.ship[i][1] + 1])

        print(self.ship) # <<<< Testing purpose
        return self.ship
    # display_ship() : Displays the ship on the grid
    def display_ship(self, ship_colour = (0, 255, 0)):
        for coordinate in self.ship:
            sense.set_pixel(coordinate[0], coordinate[1], ship_colour)
    # End : Ship
    # ************************

# ************************
# Main
# Init objects, variables
cursor = Cursor((255, 255, 255), 4, 4)
mask = GridMask((255, 0, 0))
ship = Ship()
hitcount = 0
guesses = []

# Functions
# hit_mark() : Adds guess coordinates to mask object
def hit_mark():
    cursor_pos = cursor.get_position()
    mask.add_coordinates(cursor_pos[0], cursor_pos[1])
# guess_loop() : Handles the loop for guesses
def guess_loop():
    for guess in range(0, 10):
        print("Guesses left: %0d" % ((10 - guess)))
    while cursor.middle_status != True:
        cursor.movement_handler()
    print("Guess at: " + str(cursor.get_position()))
    guesses.append(cursor.get_position())
    if cursor.get_position() in ship.ship:
        print("Hit at: %0d" % (cursor.get_position()))
        hitcount += 1
    hit_mark()
# check_win() : Checks to see if all the values in ship have been guessed
def check_win():
    for guess in guesses:
        if guess == ship.ship[0]:
            hit0 = True
        if guess == ship.ship[1]:
            hit1 = True
        if guess == ship.ship[2]:
            hit2 = True
    if hit0 and hit1 and hit2:
        win = True
    else:
        win = False
    return win