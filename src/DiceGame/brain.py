"""This module creates the illution of intelligence for the Computer."""
import random
from helpers import Turn, Tactic


class Brain:
    """
    A sort of intelligence for the computer-controlled player in the game.

    Attributes:
    -----------
    No public attibutes

    Methods:
    --------
    action(score: int, turn_points: int) -> Turn:
        Public method that determines the next move for the computer player.
    """

    def __init__(self):
        """Construct the necessary attributes for the brain object."""
        self._strategy = self._random_strategy()
        self._current_turns = 0
        self._max_turns = 4
        self._target = 100

    def _random_strategy(self) -> Tactic:
        return random.choice([Tactic.TWENTY, Tactic.TWENTY_FIVE,
                              Tactic.FOUR_TURNS])

    def action(self, score: int, turn_points: int) -> Turn:
        """Return the action to take based on strategy and mode.

        Parameters:
        -----------
        score: int
            The current score of the computer player.
        turn_points: int
            The number of points the computer player has accumulated in the
            current turn.

        Returns:
        --------
        Turn(Enum)
            The next move for the computer player (Hold or Roll).
        """
        if self._strategy in [Tactic.TEN, Tactic.TWENTY, Tactic.TWENTY_FIVE]:
            threshold = turn_points >= self._strategy.value
            return Turn.HOLD if threshold else Turn.ROLL

        if self._strategy == Tactic.FOUR_TURNS:
            if self._current_turns == 0:
                if turn_points >= 30:
                    self._current_turns += 1
                    return Turn.HOLD
                else:
                    return Turn.ROLL
            else:
                remain = self._max_turns - self._current_turns
                if remain == 0:
                    raise ZeroDivisionError('Cannot divid by Zero!')

                threshold = (self._target - score) // remain
                if turn_points >= threshold:
                    self._current_turns += 1
                    return Turn.HOLD
                else:
                    return Turn.ROLL
