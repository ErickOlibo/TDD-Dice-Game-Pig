import random
from helpers import Mode
class Dice:
    """
    [Balanced Dice]
        A dice represents a six-sided die that produces randam value 
        from 1 to 6. When the mode = None the probability distribution of each 
        size is 1/6Meaning the change of rolling a 1 is 1/6 = 16.7%. 
        This is the only setting for a user.
    
    [Unbalanced Dice]
        Mode is only define for the CPU as player. The probability of rolling 1 
        depends on the game mode. There are 4 distinct modes:
            - Easy: probability of 1 is [16.7%]
            - Medium: probability of 1 is [9.1%]
            - Hard: probability of 1 is [5.5%]
            - Merciless: probability of 1 is [2.6%]

    Attributes:
        mode (Mode): The game mode that affects the probability of rolling 1.
    """
    def __init__(self, mode: Mode = None):
        self._mode = mode
        
        r1 = list(range(1,7))
        r2 = list(range(2,7))
        r3 = list(range(3,7))
        r4 = list(range(4,7))
        self._easy = r1
        self._medium = r1 + r2
        self._hard = r1 + r2 + r3 + r4
        self._merciless = r1 + r2 + r2 + r3 + r3 + r3 + r3 + r4 + r4
        
        
    def roll(self) -> int:
        if self._mode == None: 
            return random.randint(1, 6)
        
        if self._mode in Mode:
            return random.choice(self._items())
        

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
            ValueError: If mode is set to DUEL
        """
        if not isinstance(mode, Mode) and mode is not None:
            raise TypeError('mode must be of type Mode!')
        if mode == Mode.DUEL:
            raise ValueError('The DUEL mode does not have a special!')
        self._mode = mode


    def _items(self) -> list:
        """
        Returns a list of unbalanced distribution of dice-sizes. Depending on
        the mode, the probability of rolling a 1 goes from 16.7% to 2.6%

        Returns:
            list: A list integers from 1 to 6 with unbalanced distribution.
        """
        items = None
        if self._mode is Mode.SOLO_EASY: items = self._easy
        if self._mode is Mode.SOLO_MEDIUM: items = self._medium
        if self._mode is Mode.SOLO_HARD: items = self._hard
        if self._mode is Mode.SOLO_MERCILESS: items = self._merciless
        return items