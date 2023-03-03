import uuid
from helpers import Textual, Mode
from player import Player
from event import Event
from winner import Winner
class Game:
    """ 
        A instance of a game played. It has all the rules, 
        More to add to the docstring
        ** --> is there a possibility to simulate the CPU playing:
            (delay, print choice same line, etc..)
    """

    
    def __init__(self):
        self._name = str(uuid.uuid4()) # initial name as universal unique ID
        self._rules = Textual.RULES.value
        self._menu = Textual.MENU.value
        self._mode = None
        self._player_one = None
        self._player_two = None
        self._participants = None
        self._hand = None # 
        self._histogram = [] # List of Events. The order is guarantee by Python
        self._state = False # (Save and Quit) OR Quit without Saving
        self._winner = None  # object of type Winner
    
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('name must be a string!')
        self._name = name
        
    @property
    def mode(self) -> Mode:
        return self._mode
    
    @mode.setter
    def mode(self, mode: Mode):
        if not isinstance(mode, Mode):
            raise TypeError('Mode must be SOLO or DUEL!')
        self._mode = mode
        # HERE SHOULD 
        

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