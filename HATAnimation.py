from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class HATAnimation(object):
    # Class variables
    frames = []
    play = False

    def __init__(self):
        pass

    def add_frame(self, frame = []):
        self.frames.append(frame)

    def define_colour(self, colour_num = 0, colour = (0, 0, 0)):
        if colour_num == 0:
            self.X = colour
        elif colour_num == 1:
            self.O = colour
        else:
            print("Error: ColourNum")
            return

    def play_animation(self):
        self.play = True
        if len(self.frames) >= 0:
            while self.play == True:
                for frame in self.frames:
                    sense.set_pixels(frame)
                    sleep(0.4)

O = (0, 49, 83)
X = (70, 130, 180)
frame1 = [
    O, X, O, O, O, O, O, O,
    O, X, O, O, X, O, O, X,
    O, O, X, O, X, O, O, X,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, X, O, O, O, X, O, O,
    O, X, O, O, X, O, O, X,
    O, O, O, O, X, O, O, X
]
frame2 = [
    O, O, X, O, O, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, X, O, X, O, O,
    O, O, O, X, O, O, X, O,
    X, O, O, X, O, O, X, O,
    X, O, X, O, O, O, X, O,
    X, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O
]
frame3 = [
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, X, O,
    X, O, O, O, X, O, X, O,
    X, O, O, O, X, O, O, X,
    O, X, O, O, X, O, O, X,
    O, X, O, X, O, O, O, X,
    O, X, O, X, O, O, X, O,
    X, O, O, O, O, O, X, O
]

animation_test = HATAnimation()
animation_test.add_frame(frame1)
animation_test.add_frame(frame2)
animation_test.add_frame(frame3)
animation_test.play_animation()