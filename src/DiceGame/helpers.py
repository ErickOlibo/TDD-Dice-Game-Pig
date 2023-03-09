"""This module is a collection of constant and enums needed."""
from enum import Enum, auto


class Turn(Enum):
    """Enum listing the state of the hand in the game."""

    HOLD = 'H'
    ROLL = 'R'
    LOSS = 'L'
    SETTINGS = 'S'


class Tactic(Enum):
    """Enum listing different strategy the brain can use during a game.

    A Tactic will be randomly assigned at the creation of a Brain per Game
    """

    TEN = 10
    TWENTY = 20
    TWENTY_FIVE = 25
    FOUR_TURNS = auto()


class Mode(Enum):
    """Enum representing the different option of playing the game.

    Select between One player against the CPU or a duel.
    """

    DUEL = ['1', 'Duel']
    SOLO_EASY = ['2', 'Solo - Easy']
    SOLO_MEDIUM = ['3', 'Solo - Medium']
    SOLO_HARD = ['4', 'Solo - Hard']
    SOLO_MERCILESS = ['5', 'Solo - Merciless']
    BACK = ['B', '↩ Back']
    MENU = auto()


class Start_Up(Enum):
    """The Start Up menu as the user to make an initial choice.

    Args:
        Enum (list[str]): Used to display the Start_up menu to the user
    """

    NEW_GAME = ['1', 'New Game']
    RESUME_GAME = ['2', 'Resume Game']
    HIGH_SCORE = ['3', 'High-score']
    RULES = ['4', 'Rules']
    EXIT = ['E', 'Exit']
    MENU = auto()


class Settings(Enum):
    """Show the settings view to the user.

    Args:
        Enum (list[str]): Used to display the Start_up menu to the user
    """

    NAME = ['1', 'Change Name']
    PAUSE = ['2', 'Pause Game']
    QUIT = ['3', 'Quit Game']
    CHEAT = ['4', 'Enter Cheat Mode']
    BACK = ['B', '↩ Back']
    MENU = auto()


class Data_Path(Enum):
    """The collection of paths to pickled files."""

    WINNERS = 'db/winners.pkl'
    GAMES = 'db/games.pkl'


"""Constant for the Dice rolling faces. Copyright Leodanis Pozo Ramos
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

CODE_NAMES = ["Taja", "Baby", "Walt", "Dana", "Barb", "Vida", "Hana", "Foch",
              "Bret", "Vena", "Cori", "Eula", "Theo", "Kobe", "Elin", "Noel",
              "Yoel", "Jean", "Kami", "Zayn", "Wade", "Jaye", "Nery", "Irva",
              "Dior", "Lise", "Mena", "Tito", "Matt", "Wirt", "Reva", "Nick",
              "Hali", "Gael", "Rand", "Wess", "Geno", "Zela", "Harl", "Hill",
              "Ella", "Fawn", "Olan", "Amil", "Opal", "Lyle", "Sada", "Ferd",
              "Deon", "Lone", "Zena", "Bree", "Case", "Adel", "Zayd", "Ford",
              "Murl", "Fran", "Vada", "Iver", "Vicy", "Baby", "Gary", "Keli",
              "Wava", "Purl", "Ivey", "Neil", "Sing", "Kane", "Dino", "Faye",
              "Vina", "Knox", "Tobi", "John", "Darl", "Jael", "Xavi", "Jett",
              "Oley", "Nila", "Pink", "Less", "Verl", "Gena", "Wong", "Irma",
              "Rolf", "Aron", "Crew", "Jade", "Zack", "Kyle", "Lita", "Yair",
              "Zada", "Phil", "Ruie", "Lola", "Kirt", "Ares", "Pink", "Burk",
              "Pete", "Olof", "Tyra", "Rube", "Kira", "Myra", "Yara", "Elna",
              "Fate", "Adda", "Bose", "Burl", "Chad", "Star", "Vito", "Zoya",
              "Sage", "Rudy", "Jody", "Shea", "Naya", "Jody", "Niko", "Tory",
              "Nola", "Geri", "Alta", "Otha", "Cena", "Omer", "Zeke", "Carl",
              "Hamp", "Tana", "Iker", "Chet", "Bama", "Anna", "Edna", "Cali",
              "Mimi", "Aili", "Xena", "Gene", "Halo", "Etta", "Neva", "Mack",
              "Ivah", "Dani", "Wren", "Hays", "Isom", "Greg", "Maud", "Shay",
              "Page", "Olar", "Iola", "Mima", "Yael", "Lula", "Joan", "Hedy",
              "Keri", "Fern", "Gale", "Elmo", "Rita", "Cody", "Jose", "Tera",
              "Zeno", "York", "Kory", "Roma", "Will", "Brea", "Paul", "Gwen",
              "Asha", "Zula", "Vera", "Gigi", "Hope", "Dell", "Omie", "Male",
              "Shad", "Vick", "Etha", "Thor", "Shan", "Rosy", "Dona", "Tony",
              "Octa", "Luka", "Ivan", "Vern", "Dora", "Floy", "Flem", "Luke",
              "Ella", "Dick", "Isam", "Cuba", "Andy", "Macy", "Shay", "Harm",
              "Sade", "Nona", "Lesa", "Rock",
              ]


class Textual(Enum):
    """Enum to collect all Static text needed in the application."""

    MENU = 'MENU Gets DISPLAY NOW!'
    RULES = """
Pig is a simple dice game.
Players take turns to roll a single dice as many times as they wish,
adding all roll results to a running total, but losing their gained score
for the turn if they roll a 1.

GAMEPLAY:
Each turn, a player repeatedly rolls a die until either a 1 is rolled
or the player decides to "hold":
  ⏺ The player rolls a [1], they score 0 points. The hand changes.
  ⏺ The player rolls [2] to [6], they continues to ROLL or HOLD.
  ⏺ The player chooses to "hold", the total dice count is added to their score.

The first player to score at least 100 points wins.

MODES:
The game has various playing modes reflecting the difficulty.
  ⏺ DUEL, You battle agaisnt a friend.
  ⏺ SOLO-EASY
  ⏺ SOLO-MEDIUM
  ⏺ SOLO-HARD
  ⏺ SOLO-MERCILESS

    Good Luck!
    """
    NEW_START = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome to the Start of this Game of PIG. It is simple:


        ⏺ First player to reach 100 or more points, WINS!

        ⏺ [ 🟩 ] <-- Means it is your turn to play.

        ⏺ [ 🟥 ] <-- Means it is not your turn...

        ⏺ ROLL [2]-[3]-[4]-[5]-[6], you are safe!

        ⏺ ROLL [1], you loose all cummulated points of your turn.

        ⏺ HOLD before getting [1] and you add points to your total


    Good Luck..!
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    """
