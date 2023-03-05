import time
class Event:
    """ There is an event when a player has the hand in the game
        The event is Unix Time stamped when the hand starts
        for every roll a total point is calculated till the end of roll [Hold]
        or a roll of 1
    
    """
    
    def __init__(self, name):
        self._time_stamp = round(time.time())  # sorting event chronologically
        self._name = name # Player's name
        self._points = 0
        self._rolls = []
        pass
    
    
    @property
    def points(self) -> int:
        return self._points
        
    @property
    def name(self) -> str:
        return self._name
        

    def add_roll(self, value):
        self._rolls.append(value)
        self._count_points()


    def _count_points(self):
        sum = 0
        for numb in self._rolls:
            if numb == 1:
                sum = 0
                break
            if numb != 1:
                sum += numb
        self._points = sum
