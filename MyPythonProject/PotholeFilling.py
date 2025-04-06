"""
File: PotholeFilling.py
Name: Ricky Yeh
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def fall():
    """
    pre-condition:Karel is at the upper left of the pothole,facing East
    post-condition:Karel is in the pothole,facing South
    """
    move()
    TR()
    move()

def climb():
    """
    pre-condition:Karel is in the pothole,facing South
    post-condition:Karel is at upper left of the pothole,facing East
    """
    for i in range(2):
        turn_left()
    move()

def main():
    """
    Ricky Yeh
    """
    for i in range(3):
        fall()
        put99beeperdown()
        climb()
        TR()
        move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
