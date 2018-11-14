from sense_hat import SenseHat
sense = SenseHat()

class Cursor(object):
    x_position = 0              # Stores X position
    y_position = 0              # Stores Y position
    cursor_colour = ()          # Stores cursor colour
    middle_pressed = False      # Stores if middle button pressed

    # __init__ : Initializes values
    def __init__(self, cursor_col = (255, 255, 255), start_x = 0, start_y = 0):
        self.cursor_colour = cursor_col
        self.x_position = start_x
        self.y_position = start_y
    # draw_cursor() : Turns on the LED on the SenseHat relating to the cursor postion
    def draw_cursor(self):
        sense.set_pixel(self.x_position, self.y_position, self.cursor_colour)
    # undraw_cursor() : Turns off LED on SenseHat
    def undraw_cursor(self):
        sense.set_pixel(self.x_position, self.y_position, (0, 0, 0))
    # get_position() : Returns the cursors position
    def get_position(self):
        return [self.x_position, self.y_position]
    # selector() : Loops movement methods until middle is pressed
    def selector(self):
        while self.middle_pressed != True:
            self.movement_handler()
    # middle_button() : Handles middle button input
    def middle_button(self):
        self.middle_pressed = True
    # middle_status() : Returns middle_pressed value
    def middle_status(self):
        return self.middle_pressed

    # ************************
    # LED Move Functions
    def led_up(self):
        if self.y_position > 0:
            self.y_position -= 1
    def led_down(self):
        if self.y_position < 7:
            self.y_position += 1
    def led_left(self):
        if self.x_position > 0:
            self.x_position -= 1
    def led_right(self):
        if self.x_position < 7:
            self.x_position += 1
    # movement_handler : Handles input from the user
    def movement_handler(self):
        input = sense.stick.wait_for_event()

        if (input.action == "pressed" or input.action == "held") and input.action != "released":
            if input.direction == "up":
                self.led_up()
            elif input.direction == "down":
                self.led_down()
            elif input.direction == "left":
                self.led_left()
            elif input.direction == "right":
                self.led_right()
            else:
                self.middle_button()
    # End : LED Movement
    # ************************