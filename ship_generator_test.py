# Small function to generate a ship 3 lengths long on an 8 x 8 matrix

import random

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

gen_ship()