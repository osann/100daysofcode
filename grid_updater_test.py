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

# Main: Testing function
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

water_background = update_background_w_hit([5, 5], water_background)