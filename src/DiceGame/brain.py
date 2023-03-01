import random
from helpers import  Turn, Tactic

class Brain:
    
    """A sort of Intelligence for the Player when it represent the Computer
    
    """
    def __init__(self):
        self._strategy = self._random_strategy()
        self._current_turns = 0
        self._max_turns = 4
        self._target = 100


    def _random_strategy(self) -> Tactic:
        return random.choice(list(Tactic))
        
        
    # Actions are defined for the Brain playing as the CPU
    def action(self, score, turn_points) -> Turn:

        if self._strategy in [Tactic.TEN, Tactic.TWENTY, Tactic.TWENTY_FIVE]:
            return Turn.HOLD if turn_points >= self._strategy.value else Turn.ROLL
        
        if self._strategy == Tactic.FOUR_TURNS:
            if self._current_turns == 0:
                if turn_points >= 25:
                    self._current_turns += 1
                    return Turn.HOLD
                else:
                    return Turn.ROLL
            else:
                remain = (self._max_turns - self._current_turns)
                if remain == 0:
                    raise ZeroDivisionError('Cannot divid by Zero!')
                
                threshold = (self._target - score) // remain
                return Turn.HOLD if turn_points >= threshold else Turn.ROLL
