from enums import Difficulty, Turn, Tactic

class Brain:
    """ A sort of Intelligence as the engine for the game
        It is only available to the CPU during a Player vs CPU game
    """
    
    def __init__(self):
        self._level = Difficulty.EASY
        self._strategy = Tactic.TEN
        self._four_turns_counter = 0
        pass
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level: Difficulty):
        if not isinstance(level, Difficulty):
            raise TypeError('level must be of type Difficulty!')
        self._level = level
    
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Tactic):
        if not isinstance(strategy, Tactic):
            raise TypeError('strategy must be of type Tactic!')
        self._strategy = strategy
        
    
    # Actions
    def hold_20(self, turn_points: int):
        return self._hold(20, turn_points)
    

    def hold_25(self, turn_points: int):
        return self._hold(25, turn_points)
    

    def _hold(self, threshold: int, turn_points: int):
        if not isinstance(turn_points, int):
            raise TypeError('The turn points must be an Integer!')
        return Turn.HOLD if turn_points >= threshold else Turn.ROLL


    def race_pace(self):
        pass
    
    