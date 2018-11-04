# ==========================================================================================
# JoystickLED Class
# This class is developed as part of my #100DaysofCode challenge
# The goal of this class is to control an LED on the Sense HAT module for the
# Raspberry Pi.
# This class simply waits for events from the Sense HAT joystick, then increases
# or decreases a coordinate for the LED matrix on the HAT.
# Known bugs to fix:
# - When held, continues being held **FIXED**
# - Cursor replaces the led underneath with default colour **FIXED**
# Left to add:
# - Ways to make the class implementable to other programs **DONE**
# ==========================================================================================

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
class JoystickLed(object):
    currentPos = [0, 0] # Starting coordinates
    highlight_col = (0, 0, 0) # Highligher colour, specified in init
    background = [] # Stores the background, specified in the init
    exit = False # Boolean to handle exit

    # Initiate, currently does nothing
    def __init__(self, highlight_col = (255, 255, 255), background = [], start_pos = [0, 0]):
        self.highlight_col = highlight_col
        self.background = background
        self.currentPos = start_pos

        sense.set_pixels(background)
        sense.set_pixel(self.currentPos[0], self.currentPos[1], highlight_col)

    # Represent, returns led position
    def __repr__(self):
        return self.currentPos

    # Code to test joystick output
    def joystick_test(self):
        for i in range(0,20):
            event = sense.stick.wait_for_event()
            print("The joystick was {} {}".format(event.action, event.direction))
            sleep(0.2)
    
    # ==========================================================================================
    # LED move functions
    def led_down(self):
        if self.currentPos[1] < 7:
            self.currentPos[1] += 1
            print(self.currentPos)
    def led_up(self):
        if self.currentPos[1] > 0:
            self.currentPos[1] -= 1
            print(self.currentPos)
    def led_right(self):
        if self.currentPos[0] < 7:
            self.currentPos[0] += 1
            print(self.currentPos)
    def led_left(self):
        if self.currentPos[0] > 0:
            self.currentPos[0] -= 1
            print(self.currentPos)
    # End of LED move functions
    # ==========================================================================================
    
    # Joystick move function
    # Work in conjunction with above functions
    def move(self):
        event = sense.stick.wait_for_event()

        if (event.action == "pressed" or event.action == "held") and event.action != "released":
            sense.set_pixels(self.background)
            if event.direction == "up":
                self.led_up()
            if event.direction == "down":
                self.led_down()
            if event.direction == "right":
                self.led_right()
            if event.direction == "left":
                self.led_left()
            if event.direction == "middle":
                self.exit = True
            print("Went %s" % event.direction)
        sense.set_pixel(self.currentPos[0], self.currentPos[1], self.highlight_col)
# ===================
# End of class


O = (0, 49, 83)
X = (70, 130, 180)
flat_background = [
    O, X, O, O, O, O, O, O,
    O, X, O, O, X, O, O, X,
    O, O, X, O, X, O, O, X,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, X, O, O, O, X, O, O,
    O, X, O, O, X, O, O, X,
    O, O, O, O, X, O, O, X
    ]

test = JoystickLed((247, 32, 32), flat_background)
while test.exit != True:
    test.move()
sense.clear()