from enum import Enum, auto

"""Enum to determine the level of proficient of the brain"""
class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    IMPOSSIBLE = 5
    
    

"""Enum to list the states of a turn in the game"""
class Turn(Enum):
    HOLD = auto()
    ROLL = auto()
    LOST = auto()
    

"""Enum listing the different strategy the brain can use during a game"""
class Tactic(Enum):
    TEN = auto() # Hold at 10  (sum >= 10)[N/A against Optimal Play]
    TWENTY = auto() # Hold at 20 (sum >= 20) [8% disavantage against Optimal Play]
    TWENTY_FIVE = auto() # Hold at 25 (sum >= 25) [4.2% disavantage against Optimal Play]
    FOUR_TURNS = auto() # special Tactic [3.3% disavantage against Optimal Play]
    RACE_PACE = auto() # Special Tactic [0.9% disavantage against Optimal Play]