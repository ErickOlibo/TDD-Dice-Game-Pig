from enum import Enum, auto


"""Enum to list the states of a turn in the game"""
class Turn(Enum):
    HOLD = auto()
    ROLL = auto()
    LOST = auto()
    

""" 
Enum listing the different strategy the brain can use during a game
A Tactic will be randomly assigned at the creation of a Brain per Game
"""
class Tactic(Enum):
    TEN = 10 #auto() # Hold at 10  (sum >= 10)[N/A against Optimal Play]
    TWENTY = 20 #auto() # Hold at 20 (sum >= 20) [8% disavantage against Optimal Play]
    TWENTY_FIVE = 25 #auto() # Hold at 25 (sum >= 25) [4.2% disavantage against Optimal Play]
    FOUR_TURNS = auto() # special Tactic [3.3% disavantage against Optimal Play]



""" 
Enum representing the different option of playing 2 players or
One player against the CPU
"""
class Mode(Enum):
    DUEL = ['1', 'Duel']
    SOLO_EASY = ['2', 'Solo - Easy']
    SOLO_MEDIUM = '3'
    SOLO_HARD = '4'
    SOLO_MERCILESS = '5'
    

class New_Game(Enum):
    DUEL = '1'
    EASY = '2'
    MEDIUM = '3'
    HARD = '4'
    MERCILESS = '5'
    BACK = ['B', 'b']
    

class Start_Up(Enum):
    NEW_GAME = '1'
    RESUME_GAME = '2'
    HIGH_SCORE = '3'
    RULES = '4'
    EXIT = ['E', 'e']

""" 
Constant for the Dice rolling faces
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


CODE_NAMES = [
    "Taja", "Baby", "Walt", "Dana", "Barb", "Vida", "Hana", "Foch", "Bret", "Vena",
    "Cori", "Eula", "Theo", "Kobe", "Elin", "Noel", "Yoel", "Jean", "Kami", "Zayn",
    "Wade", "Jaye", "Nery", "Irva", "Dior", "Lise", "Mena", "Tito", "Matt", "Wirt",
    "Reva", "Nick", "Hali", "Gael", "Rand", "Wess", "Geno", "Zela", "Harl", "Hill",
    "Ella", "Fawn", "Olan", "Amil", "Opal", "Lyle", "Sada", "Ferd", "Deon", "Lone",
    "Zena", "Bree", "Case", "Adel", "Zayd", "Ford", "Murl", "Fran", "Vada", "Iver",
    "Vicy", "Baby", "Gary", "Keli", "Wava", "Purl", "Ivey", "Neil", "Sing", "Kane",
    "Dino", "Faye", "Vina", "Knox", "Tobi", "John", "Darl", "Jael", "Xavi", "Jett",
    "Oley", "Nila", "Pink", "Less", "Verl", "Gena", "Wong", "Irma", "Rolf", "Aron",
    "Crew", "Jade", "Zack", "Kyle", "Lita", "Yair", "Zada", "Phil", "Ruie", "Lola",
    "Kirt", "Ares", "Pink", "Burk", "Pete", "Olof", "Tyra", "Rube", "Kira", "Myra",
    "Yara", "Elna", "Fate", "Adda", "Bose", "Burl", "Chad", "Star", "Vito", "Zoya",
    "Sage", "Rudy", "Jody", "Shea", "Naya", "Jody", "Niko", "Tory", "Nola", "Geri",
    "Alta", "Otha", "Cena", "Omer", "Zeke", "Carl", "Hamp", "Tana", "Iker", "Chet",
    "Bama", "Anna", "Edna", "Cali", "Mimi", "Aili", "Xena", "Gene", "Halo", "Etta",
    "Neva", "Mack", "Ivah", "Dani", "Wren", "Hays", "Isom", "Greg", "Maud", "Shay",
    "Page", "Olar", "Iola", "Mima", "Yael", "Lula", "Joan", "Hedy", "Keri", "Fern",
    "Gale", "Elmo", "Rita", "Cody", "Jose", "Tera", "Zeno", "York", "Kory", "Roma",
    "Will", "Brea", "Paul", "Gwen", "Asha", "Zula", "Vera", "Gigi", "Hope", "Dell",
    "Omie", "Male", "Shad", "Vick", "Etha", "Thor", "Shan", "Rosy", "Dona", "Tony",
    "Octa", "Luka", "Ivan", "Vern", "Dora", "Floy", "Flem", "Luke", "Ella", "Dick",
    "Isam", "Cuba", "Andy", "Macy", "Shay", "Harm", "Sade", "Nona", "Lesa", "Rock",
]


"""Enum to collect all Static text needed in the application"""
class Textual(Enum):
    MENU = 'MENU Gets DISPLAY NOW!'
    RULES = """

Pig is a simple dice game. Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1.
    
    GAMEPLAY:
    Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
        ⏺ If the player rolls a 1, they score nothing and it becomes the next player's turn.
        ⏺ If the player rolls any other number, it is added to their turn total and the player's turn continues.
        ⏺ If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
        
    The first player to score 100 or more points wins.
    
    MODES:
    The game has various playing modes. They each have their difficulties:
        ⏺ DUEL, where you battle with a friend.
        ⏺ SOLO-EASY, where you compete against the Computer in an even playing field
        ⏺ SOLO-MEDIUM, where the odds are slightly against you
        ⏺ SOLO-HARD, where the odds are definitly against you
        ⏺ SOLO-MERCILESS, Well I'll be honest, your chances of winning are ridiculously low.
    
    Good Luck!
    """
    