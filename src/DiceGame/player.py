from brain import Brain
from dice import Dice
from helpers import Turn

class Player:
<<<<<<< HEAD
    """
    A Player is a participant to the game. There are 2 types:
        - user: played by an person through the keyboard input
        - cpu: played internally by the computer
    Depending on the type, few properties are available
    
    Attributes:
        name: the name of the player.
        brain (Brain): This brain is available only to the computer to similate
            an sort of intelligent behaviour
        dice (Dice): each player rolls with their own dice. A user has a balanced
            dice, while the computer has an unbalanced one
    
    """
    def __init__(self, name: str, brain: Brain = None, dice: Dice = Dice()):
        self._name = name
        self._brain = brain
        self._dice = dice
        self._score = 0


    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
=======
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
>>>>>>> f1b6668 (Added Docstring to classes)
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
