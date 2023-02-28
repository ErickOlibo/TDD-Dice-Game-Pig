from enum import Enum, auto

"""Enum to determine the level of proficient of the brain"""
class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    IMPOSSIBLE = 5
    
    

"""Enum to list the states of a turn in the game """
class Turn(Enum):
    HOLD = auto()
    ROLL = auto()
    LOST = auto()