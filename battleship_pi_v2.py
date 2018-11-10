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
            self.undraw_cursor()
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

cursor = Cursor()
cursor.selector()