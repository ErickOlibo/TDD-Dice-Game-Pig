from brain import Brain
from dice import Dice
from helpers import Turn

class Player:
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
