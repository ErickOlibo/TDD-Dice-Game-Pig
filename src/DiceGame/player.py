from brain import Brain
from dice import Dice
from helpers import Turn

class Player:
    """A class representing a player in a game.

    Attributes:
        name (str): The name of the player.
        score (int): The total score of the player.
        turn_points (int): The points accumulated by the player in the current turn.

    """

    def __init__(self, name):
        """Initializes a new player with the given name."""
        self.name = name
        self.score = 0       # Needed in my brain implementation
        self.turn_points = 0 # each player is aware of his/her hand running points

    @property
    def name(self):
        """Returns the player's name."""
        return self._name
    
    @name.setter
    def name(self, name):
        """Sets the player's name to the given value."""
        self._name = name


    @property
    def brain(self) -> Brain:
        return self._brain
    
    @brain.setter
    def brain(self, brain: Brain):
        if not isinstance(brain, Brain):
            raise TypeError('brain must be of instance Brain!')
        self._brain = brain
    
    
    @property
    def score(self) -> int:
        return self._score
    
    
    def playing_choice(self, score, turn_points) -> Turn:
        if self._brain != None:
            return self._brain.action(score, turn_points)
        else:
            return None
    
    
    def add_points_to_score(self, points: int):
        self._score += points
        
    def roll_dice(self) -> int:
        return self._dice.roll()
