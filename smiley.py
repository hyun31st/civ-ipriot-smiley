from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, complexion):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.my_complexion = complexion

        X = self.complexion()
        O = self.BLANK
        self.pixels = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

    def complexion(self):
        """
        Set smiley face color
        """
        if self.my_complexion == 'BLUE':
            self.my_complexion = self.BLUE

        elif self.my_complexion == 'YELLOW':
            self.my_complexion = self.YELLOW

        elif self.my_complexion == 'RED':
            self.my_complexion = self.RED

        elif self.my_complexion == 'GREEN':
            self.my_complexion = self.GREEN

        elif self.my_complexion == 'WHITE':
            self.my_complexion = self.WHITE

        return self.my_complexion