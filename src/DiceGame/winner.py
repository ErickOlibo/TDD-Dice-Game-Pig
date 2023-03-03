

class Winner:
    """ This object will serve as a data structure to save game's winner stats
    """
    
    def __init__(self, winner: str, loser: str, score: int, game: str):
        self._winner = winner
        self._loser = loser
        self._score = score
        self._game = game
    
    
    @property
    def winner(self):
        return self._winner
    
    @winner.setter
    def winner(self, winner: str):
        self._winner = winner
    
    @property
    def loser(self):
        return self._loser
    
    @loser.setter
    def loser(self, loser: str):
        self._loser = loser