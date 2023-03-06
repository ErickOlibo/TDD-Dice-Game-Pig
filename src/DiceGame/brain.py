import random
from helpers import  Turn, Tactic

class Brain:
    """
    A sort of intelligence for the computer-controlled player in the game.

    Attributes:
    -----------
    _strategy: Tactic
        The current tactic being used by the computer player.
    _current_turns: int
        The number of turns the computer player has taken in a round.
    _max_turns: int
        The maximum number of turns a computer player can take in a round.
    _target: int
        The target score for the game.

    Methods:
    --------
    _random_strategy() -> Tactic:
        Private method that returns a random tactic from the Tactic enum.

    action(score: int, turn_points: int) -> Turn:
        Public method that determines the next move for the computer player.

    """
    def __init__(self):
        self._strategy = self._random_strategy()
        self._current_turns = 0
        self._max_turns = 4
        self._target = 100


    def _random_strategy(self) -> Tactic:
        """
        Returns a random tactic from the Tactic enum.
        """
        return random.choice(list(Tactic))
        
        
    # Actions are defined for the Brain playing as the CPU
    def action(self, score, turn_points) -> Turn:
        """
        Determines the next move for the computer player based on its current strategy and the game state.

        Parameters:
        -----------
        score: int
            The current score of the computer player.
        turn_points: int
            The number of points the computer player has accumulated in the current turn.

        Returns:
        --------
        Turn
            The next move for the computer player (Hold or Roll).
        """
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
