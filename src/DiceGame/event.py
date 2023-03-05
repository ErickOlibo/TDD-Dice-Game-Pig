import time
class Event:
<<<<<<< HEAD
    """ There is an event when a player has the hand in the game
        The event is Unix Time stamped when the hand starts
        for every roll a total point is calculated till the end of roll [Hold]
        or 1 is rolled
    
=======
    """Represents an event when a player has the hand in the game.
    The event is Unix Time stamped when the hand starts for every roll. A total point
    is calculated till the end of roll [Hold] or a roll of 1.

    Args:
    name (str): The player's name.

    Attributes:
    _time_stamp (float): The Unix timestamp of the event.
    _name (str): The player's name.
    _points (int): The total points accumulated during the event.
    _rolls (list): A list of the rolls made during the event.

>>>>>>> f1b6668 (Added Docstring to classes)
    """
    
    def __init__(self, name):
        self._time_stamp = round(time.time())  # sorting event chronologically
        self._name = name # Player's name
        self._points = 0
        self._rolls = []
        pass
    
    
    @property
    def points(self) -> int:
        """The total points accumulated during the event."""
        return self._points
        
    @property
    def name(self) -> str:
        """The player's name."""
        return self._name
        

    def add_roll(self, value):
        """Adds a roll value to the event and updates the total points.
        
        Args:
        value (int): The value of the roll to add.
        
        """
        self._rolls.append(value)
        self._count_points()


    def _count_points(self):
        """Calculates the total points for the event based on the rolls made."""
        sum = 0
        for numb in self._rolls:
            if numb == 1:
                sum = 0
                break
            if numb != 1:
                sum += numb
        self._points = sum
