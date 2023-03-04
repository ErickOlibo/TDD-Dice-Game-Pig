

class Winner:
    """ This object will serve as a data structure to save game's winner stats
    """
    
    def __init__(self, winner: str, loser: str, score: int):
        self._winner = winner
        self._loser = loser
        self._score = score

    
    
    def get_name_score(self) -> list:
        return [self._winner, self._score]
        