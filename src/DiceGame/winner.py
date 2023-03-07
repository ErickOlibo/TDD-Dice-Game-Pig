import time

class Winner:
    """ This object will serve as a data structure to save game's winner stats
    """
    
    def __init__(self, winner: str, score: int, stamp = round(time.time())):
        self._time_stamp = stamp  # sorting Winners chronologically
        self._winner = winner
        self._score = score
        self._data = [self._time_stamp, winner, score]


    @property
    def data(self) -> list: 
        return self._data
    
    @property
    def to_string(self) -> str:
        return f'{self._time_stamp} | {self._winner} - {self._score}'