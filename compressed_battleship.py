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
import grid_mask
import sense_cursor
import ship_generator

sense = SenseHat()

# ************************
# Main
# Init objects, variables
cursor = sense_cursor.Cursor((255, 255, 255), 4, 4)
mask = grid_mask.GridMask((255, 0, 0))
ship = ship_generator.Ship()
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
        draw_game()
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
# draw_game() : Renders the game on the HAT
def draw_game():
    mask.display_mask()
    cursor.draw_cursor()
# start_game() : Plays the game
def start_game():
    pass