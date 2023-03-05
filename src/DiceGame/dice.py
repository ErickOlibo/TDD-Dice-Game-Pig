import random
from helpers import Mode
class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value


""" This class is a special dice for the computer to use
    It has a different probability of rolling 1. It depends on the Mode
    when playing against the CPU
"""
class CPUDice:
    
    def __init__(self, mode: Mode) -> None:
        if not isinstance(mode, Mode):
            raise TypeError('mode must be of type Mode!')
        
        if mode == Mode.DUEL:
            raise ValueError('The DUEL mode does not have a CPU Dice!')
        
        r1 = list(range(1,7))
        r2 = list(range(2,7))
        r3 = list(range(3,7))
        r4 = list(range(4,7))
        self._mode = mode
        self._easy = r1  # same probability of rolling 1 as player [16.7%]
        self._medium = r1 + r2  # probability of rolling 1 is [9.1%]
        self._hard = r1 + r2 + r3 + r4  # probability of rolling 1 is [5.5%]
        self._merciless = r1 + r2 + r2 + r3 + r3 + r3 + r3 + r4 + r4  #  [2.6%]

    @property
    def mode(self) -> Mode:
        return self._mode
    
    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('mode must be of type Mode!')
        self._mode = mode
    

    def roll(self) -> int:
        return random.choice(self._items())
    

    def _items(self) -> list:
        items = None
        if self._mode is Mode.SOLO_EASY: items = self._easy
        if self._mode is Mode.SOLO_MEDIUM: items = self._medium
        if self._mode is Mode.SOLO_HARD: items = self._hard
        if self._mode is Mode.SOLO_MERCILESS: items = self._merciless
        return items
