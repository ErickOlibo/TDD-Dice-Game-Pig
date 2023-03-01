import random
from helpers import Difficulty
class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


""" This class is a special dice for the computer to use
    It has a different probability of rolling 1. It depends on the Difficulty
    when playing against the CPU
"""
class CPUDice:
    
    def __init__(self, level: Difficulty) -> None:
        r1 = list(range(1,7))
        r2 = list(range(2,7))
        r3 = list(range(3,7))
        r4 = list(range(4,7))
        self._level = level
        self._easy = r1  # same probability of rolling 1 as player [16.7%]
        self._medium = r1 + r2  # probability of rolling 1 is [9.1%]
        self._hard = r1 + r2 + r3 + r4  # probability of rolling 1 is [5.5%]
        self._impossible = r1 + r2 + r2 + r3 + r3 + r3 + r3 + r4 + r4  #  [2.6%]

    @property
    def level(self) -> Difficulty:
        return self._level
    
    @level.setter
    def level(self, level: Difficulty):
        if not isinstance(level, Difficulty):
            raise TypeError('level must be of type Difficulty!')
        self._level = level
    
    
    def roll(self) -> int:
        return random.choice(self._items())
    

    def _items(self) -> list:
        items = None
        if self._level is Difficulty.EASY: items = self._easy
        if self._level is Difficulty.MEDIUM: items = self._medium
        if self._level is Difficulty.HARD: items = self._hard
        if self._level is Difficulty.IMPOSSIBLE: items = self._impossible
        return items
