from enums import Difficulty

class Brain:
    """ A sort of Intelligence as the engine for the game
        It is only available to the CPU during a Player vs CPU game
    """
    
    def __init__(self):
        self._level = Difficulty.EASY
        self._strategy = self.hold_20
        pass
    
    
    def hold_20(self, turn_points):
        #return Play or Hold
        pass
    

    def hold_25(self, turn_points):
        pass
    

    def race_pace(self):
        pass
    
    