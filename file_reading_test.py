# This is just a way for me to understand how to read line by line in a file
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

def store_frames_from_file(num_of_lines):
    file = open("SenseHat/Battleship.v2/Test Files/test_file_for_animated_background.txt", "r")
    colours = {}    # Stores the colours specified in the file
    frames = []     # Stores the frames, first as variables defined in the file, then as RGB values

    for i in range(0, num_of_lines):                # This loop defines the variables written in the text file into usable ones
        line = next(file)
        colours.update({line[0] : line[5:18]})      # Grabs the name of the variable as the key (1 character only) then grabs the RGB values assigned to it
        str_interp = colours[line[0]].split(", ")   # Splits the RGB values into just numbers, they are still in string format
        for index, value in enumerate(str_interp):  # Loop converts string interpretations to integers
            str_interp[index] = int(value)
        colours[line[0]] = tuple(str_interp)        # Sets the value of the current key to the integer version of the original string numbers

    next(file)
    for line in file:               # Loop adds the frames in the file
        frames.append(line[:190])

    file.close()

    for num in range(0, len(frames)):           # This loop converts the original string into lists of the variables
        frames[num] = frames[num].split(", ")

    keys = list(colours.keys())     # List to handle keys in colours dict
    values = list(colours.values()) # List to handle values in dict

    for frame in frames:                        # Loop handles converting the original variables from characters to the tuples defined in the text
        for index, colour in enumerate(frame):
            for j in range(0, num_of_lines):
                if colour == keys[j]:
                    frame[index] = values[j]

    return frames

frames = store_frames_from_file(3)

print("CTRL + C to interrupt")
while True:
    for frame in frames:
        print(frame)
        sense.set_pixels(frame)
        sleep(0.2)