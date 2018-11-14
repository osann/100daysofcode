from sense_hat import SenseHat
import random

sense = SenseHat()
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