import uuid
from helpers import *
from player import Player
from event import Event
from winner import Winner
from gui import GUI
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
        self._gui = GUI()
        self._codename = None # Only for game in a suspended state
        self._mode = Mode.SOLO_EASY  # default
        self._participants = list[Player]
        self._hand = None # (name of the player)
        self._histogram = list[Event] # List of Events. The order is guarantee by Python
        self._is_game_over = False # set once a winner is declared
        self._winner = None  # object of type Winner
        self._startup_options = [['1', 'New game'], ['2', 'Resume game'],
                                 ['3', 'High-score'], ['4', 'Rules'], ['E', 'Exit']]
        self._new_game_options = [
            ['1', 'Duel'], ['2', 'Solo - Easy'], ['3', 'Solo - Medium'], 
            ['4', 'Solo - Hard'], ['5', 'Solo - Merciless'], ['B', '↩ Back']]
        

    
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
        self._gui.clear_terminal()
        self._gui.insert_line_breaks(1)
        self._gui.display_info(Textual.RULES.value, 'RULES', 70)
 

    
    def show_highscore(self, scores, size = 10):
        self._gui.clear_terminal()
        self._gui.display_highscore(scores, size)

    def show_startup_menu(self) -> str:
        self._gui.clear_terminal()
        title = 'START UP'
        legend = ['Option', 'Actions']
        question = 'What would you like to do? Pick an option: '
        options = self._startup_options
        return self._get_input_from_user(title, question, options, legend)
    
    
    def show_new_game_menu(self) -> str:
        self._gui.clear_terminal()
        title = 'NEW GAME'
        legend = ['Option', 'Actions']
        question = 'Pick an option: '
        options = self._new_game_options
        return self._get_input_from_user(title, question, options, legend)
        
    
    def _get_input_from_user(self, title, ask, options, legend) -> str:
        choices = [k[0] for k in options]
        choices = set(choices + [ k[0].lower() for k in options])
        while True:
            try:
                choice = self._gui.get_input_from_shown_menu(
                    title, ask, options, legend)
                if choice not in choices: raise ValueError()
            except ValueError:
                print('\nThis is not a valid option. Please try again!\n')
                time.sleep(2)
                self.menu_transition()
            else:
                return choice
    
    def menu_transition(self):
        self._gui.clear_terminal()
        time.sleep(0.5)
    
    def press_any_keys_to_continue(self):
        self._gui.display_any_key_continues()
        self.menu_transition()


    def set_duel_players(self):
        self.menu_transition()
        self._mode = Mode.DUEL
        ask = 'Enter Player One name: '
        one = Player(self._gui.get_simple_answer_from_user(ask, 'PLAYER ONE'))
        self.menu_transition()
        ask = 'Enter Player Two name: '
        two = Player(self._gui.get_simple_answer_from_user(ask, 'PLAYER TWO'))
        self._participants = list([one, two])
        

    def set_solo_player(self, mode: Mode):
        self.menu_transition()
        self._mode = Mode.DUEL

    def play(self, codename = None):
        if codename is None:
            #play new Game
            print('NO CODENAME - NEW PARTY')
        else:
            print(f'CODE NAME IS {codename}')
        time.sleep(2)
        
    
    
    
    # def exit(self) -> bool:
    #     return self._state
    
    
    # def display_entry_menu(self) -> int:
    #     while True:
    #         try:
    #             entry_choice = input('1 - New Game, 2 - Resume Game, E - Exit: ')
    #             if entry_choice not in ['1', '2', 'e']: raise ValueError()
    #         except ValueError:
    #             print('Must be an intege between 1 and 3. Please try again!')
    #         except TypeError:
    #             print('Must be an intege between 1 and 3. Please try again!')
            
    #         return entry_choice
    
    # def rules_text(self):
    #     rules = ""