import time

class Winner:
    """ This object will serve as a data structure to save game's winner stats
    """
    
    def __init__(self, winner: str, loser: str, score: int):
        self._time_stamp = round(time.time())  # sorting Winners chronologically
        self._winner = winner
        self._loser = loser
        self._score = score
        self._data = [self._time_stamp, winner, loser, score]


    @property
    def data(self) -> list: 
        return self._data
        