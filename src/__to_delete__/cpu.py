from brain import Brain
from helpers import Turn

# CLASS TO DELETE
class CPU_Player:

    """A class representing the CPU player in the Pig Dice game.

    This class is responsible for handling the CPU player's actions during a turn.

    Attributes:
        _name (str): The name of the CPU player, which is always 'CPU'.
        _score (int): The total score of the CPU player.
        _turn_points (int): The number of points the CPU player has accumulated during the current turn.
        _brain (Brain): An instance of the Brain class, which is used to determine the CPU player's actions.

    """

    def __init__(self):
        """Initializes a new instance of the CPU_Player class."""
        self._name = 'CPU'
        self._score = 0
        self._turn_points = 0
        self._brain = Brain()
        
    
    def action_choice(self, score, turn_points) -> Turn:
        """Determines the CPU player's next action during a turn.

        Args:
            score (int): The current score of the CPU player.
            turn_points (int): The number of points the CPU player has accumulated during the current turn.

        Returns:
            Turn: The CPU player's chosen action, which is either Roll or Hold.

        """
        return self._brain.action(score, turn_points)


    @property
    def score(self):
        """int: The total score of the CPU player."""

        return self._score
    
    def add_to_score_points(self, points):
        """Adds points to the CPU player's total score.

        Args:
            points (int): The number of points to add to the CPU player's score.

        """
        self._score += points
    
    def add_to_turn_points(self, points):
        """Adds points to the CPU player's turn score.

        Args:
            points (int): The number of points to add to the CPU player's turn score.

        """
        self._turn_points += points