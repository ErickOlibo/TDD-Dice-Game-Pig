import uuid
from helpers import Textual, Mode
from player import Player

class Game:
    """ 
        A instance of a game played. It has all the rules, 
        More to add to the docstring
    """

    
    def __init__(self):
        self._name = str(uuid.uuid4()) # initial name as universal unique ID
        self._rules = Textual.RULES.value
        self._menu = Textual.MENU.value
        self._mode = None
        self._player_one = None
        self._player_two = None
        self._participants = None
    
    
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
        
        self._start_menu()
        self._prepare_participants()


    def _start_menu(self):
        print(self._menu)
        
    
    def _prepare_participants(self):
        # depending on the mode, prepare the GUI-InOut question/Answers
        # Set the player type and initialize
        
        pass
