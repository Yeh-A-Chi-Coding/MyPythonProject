"""
File: StepUp.py
Name: Ricky Yeh
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

def TR():
    """
    Karel turn clockwise
    """
    for i in range(3):
        turn_left()
def put99beeperdown():
    """
    pre-condition:Karel was holding thousands of beepers
    post-condition:Karel put down 99 beepers
    """
    for i in range(99):
        put_beeper()
def main():
    # algorithm
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    TR()
    move()
    put99beeperdown()
    move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
