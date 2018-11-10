from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class GridMask(object):
    #Class variables
    x_list = []
    y_list = []

    def __init__(self, mask_colour = (255, 255, 255)):
        self.colour = mask_colour

    def change_colour(self, mask_colour):
        self.colour = mask_colour

    def add_coordinates(self, x_coordinate, y_coordinate):
        self.x_list.append(x_coordinate)
        self.y_list.append(y_coordinate)

    def reset_mask(self):
        self.x_list.clear()
        self.y_list.clear()
        print("x, y cleaned")

    def display_mask(self):
        for x in self.x_list:
            for y in self.y_list:
                sense.set_pixel(x, y, self.colour)