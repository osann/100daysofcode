# ==========================================================================================
# Battleship Game for Pi
# Another part of my #100DaysOfCode challenge. This time I'm going to use the class
# I developed earlier to make a game in which the user, moves the cursor to their
# guessed spot and if the randomly generated ship is there, they win.
# Goals for this:
# - Animation for explosion
# - Animation for moving water background
# - It to WORK
# ==========================================================================================

from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
class JoystickLed(object):
    currentPos = [0, 0] # Starting coordinates
    highlight_col = (0, 0, 0) # Highligher colour, specified in init
    background = [] # Stores the background, specified in the init
    guessed = False # Boolean to handle guessed action

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
    def led_up(self):
        if self.currentPos[1] > 0:
            self.currentPos[1] -= 1
    def led_right(self):
        if self.currentPos[0] < 7:
            self.currentPos[0] += 1
    def led_left(self):
        if self.currentPos[0] > 0:
            self.currentPos[0] -= 1
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
                self.guessed = True
        sense.set_pixel(self.currentPos[0], self.currentPos[1], self.highlight_col)

    def get_pos(self):
        return self.currentPos
# ===================
# End of class
# ===================
# Start main method

def gen_ship():
    ship = []
    ship.append([(random.randint(0, 7)), (random.randint(0, 7))])
    orientation = random.randint(0, 1)
    print(orientation) # Testing purposes
    if orientation == 1:        # X orientation
        if ship[0][0] >= 6:     # Lowers the random int for X coord by 3 to prevent ship falling off matrix
            ship[0][0] -= 3

        for i in range(0, 2):
            ship.append([ship[i][0] + 1, ship[0][1]])
    else:                       # Y orientation
        if ship[0][1] >= 6:     # Lowers the random int for Y coord by 3 to prevent ship falling off matrix
            ship[0][1] -= 3

        for i in range(0, 2):
            ship.append([ship[0][0], ship[i][1] + 1])
    print(ship) # Testing purposes
    return ship

def update_background_w_hit(coordinates, background, colour = (0, 0, 0)):
    grid = [background[0: 8],
            background[8: 16],
            background[16: 24],
            background[24: 32],
            background[32: 40],
            background[40: 48],
            background[48: 56],
            background[56: 64]
            ] # Splits the list of 64 tuples into an 8 x 8 matrix of tuples
            # This is how to make the grid addressable by coordinates

    grid[coordinates[1]][coordinates[0]] = colour
    return grid

def hit_marker(coordinates):
    guessed_coordinates = []

    if coordinates in guessed_coordinates:
        print("Already guessed here!")
    else:
        guessed_coordinates.append(coordinates)
        water_background = update_background_w_hit(coordinates, water_background, (127, 42, 73))


def start_game():
    #sense.show_message("Welcome to battleship! Place your guess.") << Uncomment this before final version
    ship = gen_ship()
    hitcount = 0
    cursor = JoystickLed((255, 0, 0), water_background, [3, 3])
    win = False

    for guess in range(0, 10):
        while cursor.guessed != True:
            cursor.move()
        print("Guess at: " + str(cursor.get_pos()))
        if cursor.currentPos in ship:
            print("Hit")
            hitcount += 1
        if hitcount == 3:
            sleep(1)
            win = True
            break
        cursor.guessed = False
    
    if win == True:
        sense.show_message("You win!")
    else:
        sense.show_message("Good try! You got %s hits!" % (str(hitcount)))

# ==========================================================================================
# Main
O = (0, 49, 83)
X = (70, 130, 180)
water_background = [
    O, X, O, O, O, O, O, O,
    O, X, O, O, X, O, O, X,
    O, O, X, O, X, O, O, X,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, X, O, O, O, X, O, O,
    O, X, O, O, X, O, O, X,
    O, O, O, O, X, O, O, X
    ]
start_game()