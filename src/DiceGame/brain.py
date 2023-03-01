from enums import Difficulty, Turn, Tactic
from player import Player
from dice import Dice

class Brain:
    """ A sort of Intelligence as the engine for the game
        It is only available to the CPU during a Player vs CPU game
        and for the Cheat option
        Each instance of a Brain only controls 1 game.
        This instance of Brain must be save with the game when paused
    """
    
    def __init__(self):
        self._level = Difficulty.EASY
        self._strategy = Tactic.TEN
        self._cpu = Player('CPU')
        self._game_name = None
        self._current_turns = 0
        self._cpu_dice = Dice()
        self._max_turns = 4
        self._target = 100

    
    @property
    def level(self) -> Difficulty:
        return self._level
    
    @level.setter
    def level(self, level: Difficulty):
        if not isinstance(level, Difficulty):
            raise TypeError('level must be of type Difficulty!')
        self._level = level
    
    
    @property
    def strategy(self) -> Tactic:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Tactic):
        if not isinstance(strategy, Tactic):
            raise TypeError('strategy must be of type Tactic!')
        self._strategy = strategy
        
    
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


    # Helpers functions
    def ceiling_division(self, n: int, d: int) -> int:
        if d == 0:
            raise ZeroDivisionError('Cannot divid by Zero!')
        return -(n // -d)
    
    def floor_division(self, n: int, d: int) -> int:
        if d == 0:
            raise ZeroDivisionError('Cannot divid by Zero!')
        return n // d
