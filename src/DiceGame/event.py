
class Event:
    """ There is an event when a player has the hand in the game
        Once the ID and Name are set, they cannot be changed
    
    """
    
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._points = 0
        self._rolls = []
        pass
    
    
    def count_points(self):
        sum = 0
        for numb in self._rolls:
            if numb == 1:
                sum = 0
                break
        self._points = sum


    def add_roll(self, value):
        self._rolls.append(value)
        self.count_points()
        