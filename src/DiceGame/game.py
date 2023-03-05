import uuid
from helpers import Textual, Mode
from player import Player
from event import Event
from winner import Winner
import time
class Game:
    """ 
        A instance of a game played. It has all the rules, 
        More to add to the docstring
        ** --> is there a possibility to simulate the CPU playing:
            (delay, print choice same line, etc..)
    """

    
    def __init__(self):
        self._time_stamp = round(time.time())  # sorting Games chronologically
        self._codename = None # Only for game in a suspended state
        self._mode = Mode.SOLO_EASY  # default
        self._participants = [] # Can be 2 players or 1 player and cpu
        self._hand = None # (name of the player)
        self._histogram = list[Event] # List of Events. The order is guarantee by Python
        self._is_game_over = False # set once a winner is declared
        self._winner = None  # object of type Winner
    
    
    @property
    def winner(self) -> Winner:
        return self._winner
    
    @winner.setter
    def winner(self, winner: Winner):
        if not isinstance(winner, Winner):
            raise TypeError('name must be a string!')
        self._winner= winner
        
    @property
    def mode(self) -> Mode:
        return self._mode
    
    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('Mode must be SOLO or DUEL!')
        self._mode = mode


    def display_rules(self):
        print(self._rules)
 
    
    def start(self):
        if self._mode == None:
            raise TypeError('Mode must be initialized before starting the game!')

        mode = self._start_menu()
        self._prepare_participants()


    def _start_menu(self):
        print(self._menu)
        # choice from user ()
        
    
    def add_to_histogram(self, event: Event):
        self._histogram.append(event)
    
    
    def _prepare_participants(self):
        # depending on the mode, prepare the GUI-InOut question/Answers
        # Set the player type and initialize
        
        pass


    def exit(self) -> bool:
        return self._state