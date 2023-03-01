from brain import Brain
from helpers import Turn

class CPU_Player:
    
    def __init__(self):
        self._name = 'CPU'
        self._score = 0
        self._turn_points = 0
        self._brain = Brain()
        
    
    def action_choice(self, score, turn_points) -> Turn:
        return self._brain.action(score, turn_points)


    @property
    def score(self):
        return self._score
    
    def add_to_score_points(self, points):
        self._score += points
    
    def add_to_turn_points(self, points):
        self._turn_points += points