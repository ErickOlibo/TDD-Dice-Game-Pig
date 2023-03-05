from brain import Brain
from helpers import Turn

class Player:
    def __init__(self, name: str, brain: Brain = None):
        self._name = name
        self._brain = brain
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
