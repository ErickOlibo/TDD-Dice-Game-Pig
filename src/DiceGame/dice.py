import random
from helpers import Mode
class Dice:
    """
    Represents a dice that can be rolled to produce a random value from 1 to 6.

    Attributes:
        value (int): The value of the last roll.
    """
    def __init__(self):
        self.value = None

    def roll(self):
        """
        Rolls the dice and returns the result.

        Returns:
            int: The value of the roll.
        """
        self.value = random.randint(1, 6)
        return self.value

class CPUDice:
    """
    Represents a dice that the computer can use in the game.
    The probability of rolling 1 depends on the game mode.

    Attributes:
        mode (Mode): The game mode that affects the probability of rolling 1.
    """   
    def __init__(self, mode: Mode) -> None:
        """
        Initializes the CPUDice with the given mode.

        Args:
            mode (Mode): The game mode that affects the probability of rolling 1.

        Raises:
            TypeError: If the mode is not of type Mode.
            ValueError: If the mode is DUEL, which does not have a CPU Dice.
        """
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
        """
        Gets the game mode that affects the probability of rolling 1.

        Returns:
            Mode: The game mode.
        """
        return self._mode
    
    @mode.setter
    def mode(self, mode: Mode):
        """
        Sets the game mode that affects the probability of rolling 1.

        Args:
            mode (Mode): The game mode that affects the probability of rolling 1.

        Raises:
            TypeError: If the mode is not of type Mode.
        """
        if not isinstance(mode, Mode):
            raise TypeError('mode must be of type Mode!')
        self._mode = mode
    

    def roll(self) -> int:
        """
        Rolls the dice and returns the result, using the current game mode.

        Returns:
            int: The value of the roll.
        """
        return random.choice(self._items())
    

    def _items(self) -> list:
        """
        Returns a list of possible values for the dice, based on the current game mode.

        Returns:
            list: A list of possible values for the dice.
        """
        items = None
        if self._mode is Mode.SOLO_EASY: items = self._easy
        if self._mode is Mode.SOLO_MEDIUM: items = self._medium
        if self._mode is Mode.SOLO_HARD: items = self._hard
        if self._mode is Mode.SOLO_MERCILESS: items = self._merciless
        return items
