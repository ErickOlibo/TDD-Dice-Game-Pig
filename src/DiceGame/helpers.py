from enum import Enum, auto


"""Enum to list the states of a turn in the game"""
class Turn(Enum):
    HOLD = auto()
    ROLL = auto()
    LOST = auto()
    

""" Enum listing the different strategy the brain can use during a game
    A Tactic will be randomly assigned at the creation of a Brain per Game
"""
class Tactic(Enum):
    TEN = 10 #auto() # Hold at 10  (sum >= 10)[N/A against Optimal Play]
    TWENTY = 20 #auto() # Hold at 20 (sum >= 20) [8% disavantage against Optimal Play]
    TWENTY_FIVE = 25 #auto() # Hold at 25 (sum >= 25) [4.2% disavantage against Optimal Play]
    FOUR_TURNS = auto() # special Tactic [3.3% disavantage against Optimal Play]


"""Enum to collect all Static text needed in the application"""
class Textual(Enum):
    MENU = 'MENU Gets DISPLAY NOW!'
    RULES = 'RULES Get DISPLAY NOW!'
    
    
""" Enum representing the different option of playing 2 players or
    One player against the CPU
"""
class Mode(Enum):
    DUEL = auto()  # Duel - Player One vs. Player Two
    SOLO_EASY = auto()  # Solo - You vs. CPU - [Level: Easy]
    SOLO_MEDIUM = auto()  # Solo - You vs. CPU - [Level: Medium]
    SOLO_HARD = auto()  # Solo - You vs. CPU - [Level: Hard]
    SOLO_MERCILESS = auto()  # Solo - You vs. CPU - [Level: Merciless]
    

""" Enum representing the possible players for a game
"""
class Participant(Enum):
    ONE = auto()
    TWO = auto()
    CPU = auto()
    


""" Constant for the Dice rolling faces
    Copyright Leodanis Pozo Ramos
    URL: https://realpython.com/python-dice-roll/
"""
DICE_FACES = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_FACES[1])
DIE_WIDTH = len(DICE_FACES[1][0])
DIE_SEP = " "

""" Inspired by the previous art, Score board
    It will help the GUI by providing a total display of the dice rolled so far
    And a score board of the current point for each contestant
"""

SCORE_BOARD = {
    1: (
        "         ",
        "  ┌─────┐",
        "= │ XXX │",
        "  └─────┘",
        "         ",
    ),
    2: (
        "┌──────────────┐┌─────┐ ┌──────────────┐┌─────┐",
        "│ YYY │ │ ZZZ │",
        "└──────────────┘└─────┘ └──────────────┘└─────┘",
    ), 
}