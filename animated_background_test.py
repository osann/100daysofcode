# Animated Background Class
# This class aims to animate a background, drawn manually in the code
# =====================================
# Goal : Make the frames importable by a different file
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class Animated_Background(object):
    #Class variables
    frames = []
    play = False
    name = ""

    def __init__(self, name):
        self.name = name

    def add_frame(self, new_frame):
        self.frames.append(new_frame)

    def store_frames_from_file(self, file_path, num_of_colours):
        file = open(file_path, "r")
        colours = {}    # Stores the colours specified in the file
        frames = []     # Stores the frames, first as variables defined in the file, then as RGB values

        for i in range(0, num_of_colours):                # This loop defines the variables written in the text file into usable ones
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
                for j in range(0, num_of_colours):
                    if colour == keys[j]:
                        frame[index] = values[j]

        return frames

    def list_frames(self):
        print("Printing frames for %s..." % (self.name))
        for background in self.frames:
            split_row = [ background[0:8],
                    background[8:16],
                    background[16:24],
                    background[24:32],
                    background[32:40],
                    background[40:48],
                    background[48:56],
                    background[56:64]
                    ] #Splits 64 list to rows
            for row in split_row:
                print(str(row))

    def play_once(self, speed = 0.2):
        for frame in self.frames:
            sense.set_pixels(frame)
            sleep(speed)

    def play_loop(self):
        self.play = True
        while self.play == True:
            self.play_once()

    def clear_frames(self):
        del self.frames[:]

# ********************
# Test main
# ********************
# Frames

X = (255, 0, 0)
O = (0, 255, 0)
P = (0, 0, 255)

frame1 = [
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X,
    X, X, O, O, P, P, X, X
]
frame2 = [
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X,
    X, O, O, P, P, X, X, X
]
frame3 = [
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X,
    O, O, P, P, X, X, X, X
]
frame4 = [
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O,
    O, P, P, X, X, X, X, O
]
frame5 = [
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O,
    P, P, X, X, X, X, O, O
]
frame6 = [
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P,
    P, X, X, X, X, O, O, P
]
frame7 = [
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P,
    X, X, X, X, O, O, P, P
]
frame8 = [
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X,
    X, X, X, O, O, P, P, X
]

class_test = Animated_Background("test")

# Test case 1
class_test.add_frame(frame1)
class_test.add_frame(frame2)
class_test.list_frames()
sense.clear()

# Test case 2
class_test.clear_frames()
class_test.list_frames()
class_test.add_frame(frame1)
class_test.add_frame(frame2)
sense.clear()

# Test case 3
class_test.add_frame(frame3)
class_test.add_frame(frame4)
class_test.add_frame(frame5)
class_test.add_frame(frame6)
class_test.play_once()
sense.clear()

# Test case 4
class_test.add_frame(frame7)
class_test.add_frame(frame8)
print("Interrupt with CTRL + C")
class_test.play_loop() # Comment this for extended test cases
sense.clear()

print("In house frame test complete")

# Outside Test case 1
outside_test = Animated_Background("Outside")

outside_test.store_frames_from_file("test_file_for_animated_background.txt", 3)
print("Interrupt with CTRL + C")
outside_test.play_loop()