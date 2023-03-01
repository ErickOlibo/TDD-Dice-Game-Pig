import uuid
from helpers import Textual, Mode

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
        self._brain = None
    
    
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
        
        
    def get_menu(self):
        return self._menu
    
    def get_rules(self):
        return self._rules
    
    def start(self, mode = Mode.SOLO_EASY):
        pass
