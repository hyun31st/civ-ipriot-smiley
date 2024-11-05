"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), 
you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
from sad import Sad
from angry import Angry

def main():
    '''
    The Happy class accepts a color name as a parameter(e.g. smiley = Happy('WHITE'))
    The Sad and Angry classes don't accept any parameters, as their colors are set to default values.
    '''
    # smiley = Angry()
    smiley = Happy()
    # smiley = Happy('WHITE')
    # smiley = Sad()

    for i in range(3):
        smiley.show()

        time.sleep(1)

        smiley.blink()

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

