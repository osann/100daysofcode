# Animated Background Class
# This class aims to animate a background, drawn manually in the code
# =====================================
# Goal : Make the frames importable by a different file
from sense_hat import SenseHat

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

    def play_once(self):
        for frame in self.frames:
            sense.set_pixels(frame)

    def play_loop(self):
        self.play == True
        while self.play == True:
            for frame in self.frames:
                sense.set_pixels(frame)

    def play_loop_from_file(self, file_path, num_of_colours):
        frame_file = open(file_path, "r")
        colour = {}
        for index, text in enumerate(frame_file):
            if index > 0 and index < num_of_colours:
                colour.append(frame_file.read(1))
                value = frame_file
        for num in num_of_colours:
            colour.append(frame_file.read(1))
            

        for line in frame_file:
            sense.set_pixels(line)

    def loop_from_file(self, file_path, num_of_colours):
        frame_file = open(file_path, "r")
        colour = {}
        for index, line in enumerate(frame_file):
            line = frame_file.readline()
            select_colour = tuple(line[5:8], line[11:14], line[17:20])

            colour[frame_file.read(1)] = select_colour

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
class_test.play_loop()
sense.clear()