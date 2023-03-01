import random
from helpers import  Turn, Tactic
from player import Player

class Brain:
    """ 
        A sort of Intelligence as the engine for the game
        It is only available to the CPU during a Player vs CPU game
        and for the Cheat option
        Each instance of a Brain only controls 1 game.
        This instance of Brain must be save with the game when paused
    """
    
    def __init__(self):
        self._mode = None
        self._strategy = self._random_strategy()  # random enum selection
        self._cpu = Player('CPU')
        self._game_name = None
        self._current_turns = 0
        self._max_turns = 4
        self._target = 100


    def _random_strategy(self) -> Tactic:
        return random.choice(list(Tactic))
        
        
    # Actions are defined for the Brain playing as the CPU
    def action(self) -> Turn:

        if self.strategy in [Tactic.TEN, Tactic.TWENTY, Tactic.TWENTY_FIVE]:
            return Turn.HOLD if self._cpu.turn_points >= self.strategy.value else Turn.ROLL
        
        if self.strategy == Tactic.FOUR_TURNS:
            if self._current_turns == 0:
                if self._cpu.turn_points >= 25:
                    self._current_turns += 1
                    return Turn.HOLD
                else:
                    return Turn.ROLL
            else:
                remain = (self._max_turns - self._current_turns)
                if remain == 0:
                    raise ZeroDivisionError('Cannot divid by Zero!')
                
                threshold = (self._target - self._cpu.score) // remain
                return Turn.HOLD if self._cpu.turn_points >= threshold else Turn.ROLL
