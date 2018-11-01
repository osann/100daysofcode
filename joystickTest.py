# ==========================================================================================
# JoystickLED Class
# This class is developed as part of my #100DaysofCode challenge
# The goal of this class is to control an LED on the Sense HAT module for the
# Raspberry Pi.
# This class simply waits for events from the Sense HAT joystick, then increases
# or decreases a coordinate for the LED matrix on the HAT.
# ==========================================================================================

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
class JoystickLed(object):
    currentPos = [1, 1] # Coordinates

    # Initiate, currently does nothing
    def __init__(self):
        pass

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
        else:
            print("Hit bottom") # Remove this before final version
    def led_up(self):
        if self.currentPos[1] > 0:
            self.currentPos[1] -= 1
            print(self.currentPos)
        else:
            print("Hit top") # Remove this before final version
    def led_right(self):
        if self.currentPos[0] < 7:
            self.currentPos[0] += 1
            print(self.currentPos)
        else:
            print("Hit right side") # Remove this before final version
    def led_left(self):
        if self.currentPos[0] > 0:
            self.currentPos[0] -= 1
            print(self.currentPos)
        else:
            print("Hit left side") # Remove this before final version
    # End of LED move functions
    # ==========================================================================================
    
    # Joystick move function
    # Work in conjunction with above functions
    def move(self):
        event = sense.stick.wait_for_event()
        if (event.action == "pressed" or event.action == "held") and event.action != "released":
            if event.direction == "up":
                self.led_up()
            if event.direction == "down":
                self.led_down()
            if event.direction == "right":
                self.led_right()
            if event.direction == "left":
                self.led_left()
            print("Went %s" % event.direction)
            sleep(0.3)

test = JoystickLed()
for i in range(0, 20):
    test.move()