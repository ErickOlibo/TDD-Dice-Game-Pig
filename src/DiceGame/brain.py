from enums import Difficulty, Turn

class Brain:
    """ A sort of Intelligence as the engine for the game
        It is only available to the CPU during a Player vs CPU game
    """
    
    def __init__(self):
        self._level = Difficulty.EASY
        self._strategy = self.hold_20
        pass
    
    
    def hold_20(self, turn_points: int):
        return self._hold(20, turn_points)
    

    def hold_25(self, turn_points: int):
        return self._hold(25, turn_points)
    

    def _hold(self, threshold: int, turn_points: int):
        if not isinstance(turn_points, int):
            raise ValueError('The turn points must be an Integer!')
        return Turn.HOLD if turn_points >= threshold else Turn.ROLL


    def race_pace(self):
        pass
    
    